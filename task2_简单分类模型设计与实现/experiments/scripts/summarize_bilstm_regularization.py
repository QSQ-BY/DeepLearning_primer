"""核对六组早停实验，以验证集选方案，并导出 WD / Dropout 对比图。"""

import csv
import hashlib
import json
from pathlib import Path
import shutil
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.ticker import PercentFormatter
import numpy as np
import torch

PROJECT = Path(__file__).resolve().parents[2]
ROOT = PROJECT.parent
sys.path.insert(0, str(PROJECT))
from news_classifier.experiments.bilstm_regularization import SETTINGS
from news_classifier.evaluation.analysis import infer_checkpoint, write_json

OUTPUT = PROJECT / "experiments/bilstm/regularization"
HANDOFF = Path("D:/codex/BiLSTM_regularization_20261103")
LABELS = {"baseline": "早停基线", "wd3e4": "WD=3e-4", "wd1e3": "WD=1e-3",
          "dropout01": "Embedding Dropout=0.1", "dropout02": "Embedding Dropout=0.2", "dropout03": "Embedding Dropout=0.3"}
COLORS = {"baseline": "#2563A6", "wd3e4": "#C18A18", "wd1e3": "#D76F26",
          "dropout01": "#D76F26", "dropout02": "#C18A18", "dropout03": "#B9558A"}


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def read_history(path):
    with path.open(encoding="utf-8", newline="") as stream:
        return [{key: float(value) for key, value in row.items()} for row in csv.DictReader(stream)]


def collect():
    records, histories, configs = {}, {}, {}
    root_suite = read_json(ROOT / ".build/task2/bilstm_regularization_20261103/suite.json")
    if root_suite["status"] != "completed":
        raise RuntimeError("六组正式训练全部完成后才能生成最终对比")
    for run_id, (wd, dropout) in SETTINGS.items():
        folder = ROOT / f".build/task2/runs/bilstm_es_{run_id}_20261103"
        execution = read_json(folder / "execution.json")
        assert execution["status"] == "completed" and execution["vocabulary_matches_baseline"]
        config = read_json(folder / "config.json")
        rows = read_history(folder / "metrics.csv")
        assert all(np.isfinite(value) for row in rows for value in row.values())
        assert [int(row["epoch"]) for row in rows] == list(range(1, len(rows) + 1))
        assert len(rows) == execution["summary"]["completed_epochs"] <= 20
        assert config["training"]["weight_decay"] == wd and config["model"]["embedding_dropout"] == dropout
        for source, digest in execution["source_sha256"].items():
            assert hashlib.sha256((ROOT / source).read_bytes()).hexdigest() == digest, source
        # 独立重放早停状态，不调用被测试的实现。
        reference, failures, expected_stop = float("inf"), 0, 20
        for row in rows:
            if reference - row["val_loss"] > 0.001:
                reference, failures = row["val_loss"], 0
            else:
                failures += 1
            if failures >= 3:
                expected_stop = int(row["epoch"])
                break
        assert len(rows) == expected_stop
        accuracy_row = max(rows, key=lambda row: (row["val_accuracy"], -row["val_loss"]))
        loss_row = min(rows, key=lambda row: row["val_loss"])
        for name, expected in [("best_accuracy.pt", accuracy_row), ("best_loss.pt", loss_row)]:
            saved = torch.load(folder / name, map_location="cpu", weights_only=True)
            assert saved["epoch"] == expected["epoch"]
            assert saved["val_loss"] == expected["val_loss"] and saved["val_accuracy"] == expected["val_accuracy"]
        records[run_id] = dict(run_id=run_id, label=LABELS[run_id], weight_decay=wd, embedding_dropout=dropout,
                              completed_epochs=len(rows), selected_epoch=int(accuracy_row["epoch"]),
                              val_accuracy=accuracy_row["val_accuracy"], selected_val_loss=accuracy_row["val_loss"],
                              min_val_loss=loss_row["val_loss"], train_accuracy_at_selected=accuracy_row["train_accuracy"],
                              initial_parameter_sha256=execution["summary"]["initial_parameter_sha256"],
                              elapsed_seconds=execution["elapsed_seconds"], checkpoint=str(folder / "best_accuracy.pt"))
        histories[run_id], configs[run_id] = rows, config
    assert len({record["initial_parameter_sha256"] for record in records.values()}) == 1
    baseline = configs["baseline"]
    for config in configs.values():
        assert config["seed"] == baseline["seed"] and config["data"] == baseline["data"]
        model = dict(config["model"], embedding_dropout=0.0)
        training = dict(config["training"], weight_decay=0.0001)
        assert model == baseline["model"] and training == baseline["training"]
    return records, histories


def style_axis(ax):
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_color("#94A3B8")
    ax.grid(axis="y", color="#E2E8F0", linewidth=0.8)
    ax.set_axisbelow(True)


def save(fig, name):
    for extension in ("png", "svg"):
        fig.savefig(OUTPUT / "assets" / f"{name}.{extension}", dpi=180, facecolor="white")
    plt.close(fig)


def overview(records):
    fig, axes = plt.subplots(2, 3, figsize=(17, 10), layout="constrained")
    fig.suptitle("BiLSTM 单因素实验：WD 与词嵌入 Dropout", fontsize=22, weight="bold")
    rows = [("WD", ["baseline", "wd3e4", "wd1e3"], ["1e-4\n基线", "3e-4", "1e-3"]),
            ("Embedding Dropout", ["baseline", "dropout01", "dropout02", "dropout03"], ["0\n基线", "0.1", "0.2", "0.3"])]
    for row_index, (factor, ids, labels) in enumerate(rows):
        for col, (key, title) in enumerate([("val_accuracy", "最高验证准确率"), ("min_val_loss", "最低验证损失"), ("completed_epochs", "实际训练轮次")]):
            ax = axes[row_index, col]
            values = [records[run_id][key] for run_id in ids]
            bars = ax.bar(labels, values, width=0.55, color=[COLORS[run_id] for run_id in ids], edgecolor="white")
            for bar, run_id in zip(bars, ids):
                if run_id != "baseline":
                    bar.set_hatch("//")
            if key == "val_accuracy":
                ax.set_ylim(0, 1.08)
                ax.yaxis.set_major_formatter(PercentFormatter(1))
                formatted = [f"{value:.3%}" for value in values]
            elif key == "min_val_loss":
                ax.set_ylim(0, max(values)*1.35)
                formatted = [f"{value:.4f}" for value in values]
            else:
                ax.set_ylim(0, 23)
                ax.set_yticks([0, 5, 10, 15, 20])
                ax.axhline(20, color="#64748B", linestyle="--", linewidth=1)
                formatted = [str(value) for value in values]
            ax.bar_label(bars, labels=formatted, padding=5, fontsize=11)
            ax.set_title(f"{factor}：{title}", loc="left", fontsize=13.5, pad=17)
            ax.set_xlabel(factor)
            style_axis(ax)
    fig.supxlabel("固定 seed=42、同一训练/验证划分；最大 20 轮；早停 patience=3、min_delta=0.001；分类层 Dropout=0.5。", fontsize=10.5, color="#475569")
    save(fig, "bilstm_regularization_overview")


def curves(histories, ids, factor, name):
    fig, axes = plt.subplots(1, 2, figsize=(16, 6), layout="constrained")
    fig.suptitle(f"BiLSTM {factor} 单因素实验：验证曲线", fontsize=21, weight="bold")
    for ax, key, title in zip(axes, ("val_accuracy", "val_loss"), ("验证准确率", "验证损失")):
        for run_id in ids:
            rows = histories[run_id]
            x, y = [row["epoch"] for row in rows], [row[key] for row in rows]
            label = LABELS[run_id].replace("Embedding ", "")
            ax.plot(x, y, color=COLORS[run_id], linewidth=2, label=label)
            ax.scatter(x[-1], y[-1], color=COLORS[run_id], marker="s", s=35, edgecolor="white", zorder=3)
        upper = max(len(histories[run_id]) for run_id in ids)
        ax.set_xlim(1, upper + 0.3)
        ticks = sorted(set([1, upper] + list(range(3, upper, 3))))
        ax.set_xticks(ticks)
        ax.set_xlabel("训练轮次")
        ax.set_title(title, loc="left", fontsize=15)
        if key == "val_accuracy":
            ax.yaxis.set_major_formatter(PercentFormatter(1))
        else:
            ax.set_ylim(bottom=0)
        ax.legend(frameon=False, fontsize=10)
        style_axis(ax)
    fig.supxlabel("曲线在实际停止轮次结束，方点表示停止位置；未补齐或外推后续轮次。", fontsize=11, color="#475569")
    save(fig, name)


def early_stopping_curve(histories):
    original = read_history(ROOT / ".build/task2/runs/bilstm_baseline_20261103/metrics.csv")
    baseline = histories["baseline"]
    fig, axes = plt.subplots(1, 2, figsize=(16, 6), layout="constrained")
    fig.suptitle("BiLSTM：原 20 轮基线与新增早停基线", fontsize=21, weight="bold")
    for ax, key, title in zip(axes, ("val_accuracy", "val_loss"), ("验证准确率", "验证损失")):
        ax.plot([row["epoch"] for row in original], [row[key] for row in original], color="#64748B", linestyle="--", linewidth=2, label="原基线：固定 20 轮")
        ax.plot([row["epoch"] for row in baseline], [row[key] for row in baseline], color=COLORS["baseline"], linewidth=2, label="新增早停基线")
        ax.axvline(len(baseline), color="#D76F26", linestyle=":", linewidth=1.5, label=f"第 {len(baseline)} 轮停止")
        ax.set_xlim(1, 20)
        ax.set_xticks([1, 5, 10, 15, 20])
        ax.set_xlabel("训练轮次")
        ax.set_title(title, loc="left", fontsize=15)
        if key == "val_accuracy":
            ax.yaxis.set_major_formatter(PercentFormatter(1))
        else:
            ax.set_ylim(bottom=0)
        ax.legend(frameon=False, fontsize=10)
        style_axis(ax)
    fig.supxlabel("两次均从头训练；早停只控制停止时机，最佳权重仍按验证指标保存。", fontsize=11, color="#475569")
    save(fig, "bilstm_early_stopping_comparison")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    torch.set_num_threads(4)
    records, histories = collect()
    original_history = read_history(ROOT / ".build/task2/runs/bilstm_baseline_20261103/metrics.csv")
    prefix_difference = max(abs(old[key] - new[key]) for old, new in zip(original_history, histories["baseline"]) for key in old)
    OUTPUT.mkdir(parents=True, exist_ok=True)
    (OUTPUT / "assets").mkdir(exist_ok=True)
    (OUTPUT / "data").mkdir(exist_ok=True)
    # 在读取任何新测试结果之前固定唯一最终方案。
    winner = max(records, key=lambda name: (records[name]["val_accuracy"], -records[name]["selected_val_loss"]))
    selection_path = OUTPUT / "data/selection.json"
    selection = dict(rule="max validation accuracy; ties choose lower validation loss", selected_run_id=winner,
                     selected_checkpoint=records[winner]["checkpoint"], test_used_for_selection=False)
    if selection_path.exists():
        assert read_json(selection_path) == selection
    write_json(selection_path, selection)
    folder = Path(records[winner]["checkpoint"]).parent / "final_evaluation"
    checkpoint_digest = hashlib.sha256(Path(records[winner]["checkpoint"]).read_bytes()).hexdigest()
    if not (folder / "metrics.json").exists():
        infer_checkpoint(records[winner]["checkpoint"], folder)
    final_test = read_json(folder / "metrics.json")
    assert final_test["checkpoint_sha256"] == checkpoint_digest
    baseline_test = read_json(PROJECT / "experiments/bilstm/data/comparison_summary.json")["models"]["BiLSTM"]
    with np.load(folder / "predictions.npz") as arrays, np.load(ROOT / ".build/task2/runs/bilstm_baseline_20261103/comparison_evaluation/predictions.npz") as original:
        assert np.array_equal(arrays["labels"], original["labels"])
        assert int(np.sum(arrays["labels"] == arrays["predictions"])) == final_test["correct"]
    font = Path("C:/Windows/Fonts/msyh.ttc")
    if font.exists():
        font_manager.fontManager.addfont(str(font))
        plt.rcParams["font.family"] = font_manager.FontProperties(fname=str(font)).get_name()
    plt.rcParams.update({"font.size": 11, "axes.unicode_minus": False, "svg.fonttype": "none"})
    overview(records)
    curves(histories, ["baseline", "wd3e4", "wd1e3"], "WD", "bilstm_wd_curves")
    curves(histories, ["baseline", "dropout01", "dropout02", "dropout03"], "Embedding Dropout", "bilstm_dropout_curves")
    early_stopping_curve(histories)
    summary = dict(runs=records, selection=selection, final_test=final_test, original_bilstm_test=baseline_test,
                   early_stopping_baseline_prefix_max_metric_difference=prefix_difference,
                   test_accuracy_delta_percentage_points=(final_test["accuracy"]-baseline_test["accuracy"])*100,
                   controls=dict(seed=42, train_samples=108000, validation_samples=12000, test_samples=7600,
                                 common_initial_parameters=True, dropout_location="after embedding before packing",
                                 classifier_dropout=0.5, monitor="val_loss", patience=3, min_delta=0.001,
                                 max_epochs=20, max_concurrent_processes=2))
    wd_best = max(["baseline", "wd3e4", "wd1e3"], key=lambda name: (records[name]["val_accuracy"], -records[name]["selected_val_loss"]))
    dropout_best = max(["baseline", "dropout01", "dropout02", "dropout03"], key=lambda name: (records[name]["val_accuracy"], -records[name]["selected_val_loss"]))
    summary["factor_best"] = {"weight_decay": wd_best, "embedding_dropout": dropout_best}
    write_json(OUTPUT / "data/summary.json", summary)
    write_json(OUTPUT / "data/histories.json", histories)
    with (OUTPUT / "data/validation_comparison.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(next(iter(records.values()))))
        writer.writeheader()
        writer.writerows(records.values())
    contents = ["# BiLSTM：早停、WD 与词嵌入 Dropout 实验", "",
                "固定原 AG-news 划分、词表、初始权重和随机种子 42，每次只改变一个正则化因素。所有组采用相同的验证损失早停规则：patience=3、min_delta=0.001，最多 20 轮。分类层 Dropout 固定为 0.5。", "",
                "| 实验 | WD | 词嵌入 Dropout | 实际轮次 | 最佳准确率轮次 | 最高验证准确率 | 最低验证损失 |",
                "| --- | ---: | ---: | ---: | ---: | ---: | ---: |"]
    for record in records.values():
        contents.append(f"| {record['label']} | {record['weight_decay']:g} | {record['embedding_dropout']:g} | {record['completed_epochs']} | {record['selected_epoch']} | {record['val_accuracy']:.4%} | {record['min_val_loss']:.6f} |")
    contents += ["", f"WD 单因素比较中，验证集最优设置为 **{records[wd_best]['weight_decay']:g}**；"
                 f"词嵌入 Dropout 单因素比较中，最优设置为 **{records[dropout_best]['embedding_dropout']:g}**，"
                 f"最高验证准确率相对早停基线变化 {(records[dropout_best]['val_accuracy']-records['baseline']['val_accuracy'])*100:+.4f} 个百分点。", ""]
    contents += ["", f"依据验证准确率、同准确率时的验证损失，最终选中 **{LABELS[winner]}**。选择规则和方案先写入 `data/selection.json`，之后才评估该方案的官方测试集；其他新配置不评估测试集。", "",
                 f"早停基线实际训练 {records['baseline']['completed_epochs']} 轮，保留第 {records['baseline']['selected_epoch']} 轮权重。"
                 f"与原始 20 轮基线的共同轮次相比，各项指标最大绝对差为 {prefix_difference:g}，用于核对新增早停没有改变停止前的训练过程。", "",
                 "| 测试指标 | 原始 BiLSTM 基线 | 本次验证集选定方案 |", "| --- | ---: | ---: |",
                 f"| 准确率 | {baseline_test['accuracy']:.4%} | {final_test['accuracy']:.4%} |",
                 f"| Macro-F1 | {baseline_test['macro_f1']:.4%} | {final_test['macro_f1']:.4%} |",
                 f"| 损失 | {baseline_test['loss']:.6f} | {final_test['loss']:.6f} |",
                 f"| 错误数 / 7600 | {baseline_test['errors']} | {final_test['errors']} |", "",
                 f"本次测试准确率相对原 BiLSTM 变化 **{summary['test_accuracy_delta_percentage_points']:+.4f} 个百分点**。结果来自单个随机种子；验证集上的调参收益需要多种子复核，测试结果不用于反向调整本次选择。", "",
                 "## 对比图", "", "![验证指标与停止轮次](assets/bilstm_regularization_overview.png)", "",
                 "![WD 验证曲线](assets/bilstm_wd_curves.png)", "",
                 "![词嵌入 Dropout 验证曲线](assets/bilstm_dropout_curves.png)", "",
                 "![早停与原基线](assets/bilstm_early_stopping_comparison.png)", "",
                 "## 复现与来源", "",
                 "在 Task 2 目录运行 `python -m news_classifier.experiments.bilstm_regularization --run-id baseline`；其他 run-id 为 `wd3e4`、`wd1e3`、`dropout01`、`dropout02`、`dropout03`。已有输出会拒绝覆盖，复现实验需修改对应配置的输出目录。", "",
                 "原始运行记录位于 `.build/task2/runs/bilstm_es_<run-id>_20261103/`，含 config.json、metrics.csv、两种最佳权重、training_summary.json、execution.json 和 console.log。执行记录保留代码哈希，六组初始化参数摘要一致。", "",
                 "训练最多同时运行两个独立 GPU 进程，因此记录的用时受并发影响，不作为各组计算效率的比较依据。早停仅影响何时结束训练，最小改善量不影响真实最佳权重的保存。", "",
                 "本表的最低验证损失与最高验证准确率可能来自不同轮次；最终测试使用最高验证准确率权重。图中曲线只到实际停止位置，不对缺失轮次补零或外推。", ""]
    (OUTPUT / "README.md").write_text("\n".join(contents), encoding="utf-8")
    HANDOFF.mkdir(parents=True, exist_ok=True)
    for path in (OUTPUT / "assets").iterdir():
        if path.suffix in (".png", ".svg"):
            shutil.copy2(path, HANDOFF / path.name)
    for filename in ("summary.json", "validation_comparison.csv"):
        shutil.copy2(OUTPUT / "data" / filename, HANDOFF / filename)
    print(json.dumps({"winner": winner, "test_accuracy": final_test["accuracy"], "output": str(OUTPUT), "handoff": str(HANDOFF)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
