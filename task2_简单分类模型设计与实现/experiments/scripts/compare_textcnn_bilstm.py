"""训练完成后，对比验证集选出的 TextCNN 与 BiLSTM，并生成静态图。"""

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
from news_classifier.data import LABEL_NAMES
from news_classifier.evaluation.analysis import classification_metrics, error_groups, infer_checkpoint, write_json

EXPERIMENT = PROJECT / "experiments/bilstm"
RUN = ROOT / ".build/task2/runs/bilstm_baseline_20261103"
TEXTCNN_RUN = ROOT / ".build/task2/runs/textcnn_k237_plateau20"
TEXTCNN_DATA = PROJECT / "experiments/textcnn/error_analysis/data/kernel_comparison/k237"
HANDOFF = Path("D:/codex/BiLSTM_vs_TextCNN_20261103")
COLORS = {"TextCNN": "#2563A6", "BiLSTM": "#D77A22"}


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def read_history(path):
    with path.open(encoding="utf-8", newline="") as stream:
        return [{key: float(value) for key, value in row.items()} for row in csv.DictReader(stream)]


def validate_predictions(folder, metrics):
    with np.load(folder / "predictions.npz") as values:
        labels = values["labels"].copy()
        predictions = values["predictions"].copy()
        logits = values["logits"].copy()
    assert labels.shape == predictions.shape == (7600,)
    assert np.isfinite(logits).all()
    assert np.array_equal(logits.argmax(1), predictions)
    assert np.bincount(labels, minlength=4).tolist() == [1900] * 4
    independent_cm = np.zeros((4, 4), dtype=np.int64)
    for actual, predicted in zip(labels, predictions):
        independent_cm[actual, predicted] += 1
    assert independent_cm.tolist() == metrics["confusion_matrix"]
    assert int(np.sum(labels == predictions)) == metrics["correct"]
    actual_loss = torch.nn.functional.cross_entropy(torch.tensor(logits), torch.tensor(labels)).item()
    assert abs(actual_loss - metrics["loss"]) < 1e-6
    recalculated = classification_metrics(labels, predictions)
    assert abs(recalculated["macro_f1"] - metrics["macro_f1"]) < 1e-12
    return labels, predictions


def prediction_identity(folder):
    with (folder / "all_predictions.csv").open(encoding="utf-8", newline="") as stream:
        return [(row["sample_id"], row["true_label"], row["text"]) for row in csv.DictReader(stream)]


def save_figure(fig, assets, name):
    for extension in ("png", "svg"):
        fig.savefig(assets / f"{name}.{extension}", dpi=180, facecolor="white")
    plt.close(fig)


def style_axis(ax, *, grid=True):
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_color("#94A3B8")
    ax.set_axisbelow(True)
    if grid:
        ax.grid(axis="y", color="#E2E8F0", linewidth=0.8)


def plot_overview(metrics, assets):
    fig, axes = plt.subplots(2, 2, figsize=(15, 10.5), layout="constrained")
    fig.suptitle("TextCNN 与 BiLSTM：AG-news 测试集对比", fontsize=22, weight="bold")
    names = list(metrics)
    x = np.arange(2)
    ax = axes[0, 0]
    for offset, name in zip((-0.18, 0.18), names):
        values = [metrics[name][key] * 100 for key in ("accuracy", "macro_f1")]
        bars = ax.bar(x + offset, values, width=0.34, label=name, color=COLORS[name],
                      hatch="" if name == "TextCNN" else "//", edgecolor="white")
        ax.bar_label(bars, labels=[f"{value:.3f}%" for value in values], padding=5, fontsize=11)
    ax.set_xticks(x, ["准确率", "Macro-F1"])
    ax.set_ylim(0, 110)
    ax.yaxis.set_major_formatter(PercentFormatter(100))
    ax.set_title("整体分类表现（越高越好）", loc="left", fontsize=15, pad=38)
    ax.legend(frameon=False, ncols=2, loc="lower center", bbox_to_anchor=(0.5, 1.0))
    style_axis(ax)

    ax = axes[0, 1]
    values = [metrics[name]["loss"] for name in names]
    bars = ax.bar(names, values, width=0.48, color=[COLORS[name] for name in names], edgecolor="white")
    bars[1].set_hatch("//")
    ax.bar_label(bars, labels=[f"{value:.4f}" for value in values], padding=6, fontsize=12)
    ax.set_ylim(0, max(values) * 1.32)
    ax.set_ylabel("交叉熵损失")
    ax.set_title("测试损失（越低越好）", loc="left", fontsize=15, pad=16)
    style_axis(ax)

    ax = axes[1, 0]
    x = np.arange(4)
    for offset, name in zip((-0.18, 0.18), names):
        values = [row["f1"] * 100 for row in metrics[name]["per_class"]]
        bars = ax.bar(x + offset, values, width=0.34, color=COLORS[name],
                      hatch="" if name == "TextCNN" else "//", edgecolor="white")
        ax.bar_label(bars, labels=[f"{value:.2f}" for value in values], padding=4, fontsize=10)
    ax.set_xticks(x, LABEL_NAMES)
    ax.set_ylim(0, 108)
    ax.yaxis.set_major_formatter(PercentFormatter(100))
    ax.set_title("各类别 F1（每类 1900 条测试样本）", loc="left", fontsize=15, pad=16)
    style_axis(ax)

    ax = axes[1, 1]
    values = [metrics[name]["errors"] for name in names]
    bars = ax.bar(names, values, width=0.48, color=[COLORS[name] for name in names], edgecolor="white")
    bars[1].set_hatch("//")
    ax.bar_label(bars, labels=[f"{value} 条" for value in values], padding=6, fontsize=12)
    ax.set_ylim(0, max(values) * 1.32)
    ax.set_ylabel("误分类样本数")
    ax.set_title("测试错误总数（越低越好）", loc="left", fontsize=15, pad=16)
    style_axis(ax)
    delta = (metrics["BiLSTM"]["accuracy"] - metrics["TextCNN"]["accuracy"]) * 100
    fig.supxlabel(f"同一官方测试集 n=7600 · 权重均按验证集准确率选择 · BiLSTM 准确率变化 {delta:+.3f} 个百分点",
                  fontsize=11, color="#475569")
    save_figure(fig, assets, "textcnn_vs_bilstm_overview")


def plot_history(histories, metrics, assets):
    fig, axes = plt.subplots(1, 2, figsize=(16, 6), layout="constrained")
    fig.suptitle("TextCNN 与 BiLSTM：20 轮训练过程", fontsize=21, weight="bold")
    for ax, suffix, title in zip(axes, ("accuracy", "loss"), ("训练／验证准确率", "训练／验证损失")):
        for name, rows in histories.items():
            epochs = [row["epoch"] for row in rows]
            for split, style, label in (("train", "--", "训练"), ("val", "-", "验证")):
                values = [row[f"{split}_{suffix}"] for row in rows]
                ax.plot(epochs, values, color=COLORS[name], linestyle=style, linewidth=2,
                        label=f"{name} {label}")
            selected = metrics[name]["epoch"]
            row = rows[selected - 1]
            ax.scatter([selected], [row[f"val_{suffix}"]], color=COLORS[name],
                       s=85, edgecolor="white", marker="o", zorder=4)
        ax.set_xlim(1, 20)
        ax.set_xticks([1, 5, 10, 15, 20])
        ax.set_xlabel("训练轮次")
        ax.set_title(title, loc="left", fontsize=15)
        style_axis(ax)
        if suffix == "accuracy":
            ax.yaxis.set_major_formatter(PercentFormatter(1))
            ax.set_ylim(min(row["train_accuracy"] for rows in histories.values() for row in rows) - 0.025, 1.01)
        else:
            ax.set_ylim(bottom=0)
        ax.legend(frameon=False, fontsize=10, ncols=2)
    fig.supxlabel("实线：验证集；虚线：训练集；圆点：按验证准确率选出的测试权重轮次。", fontsize=11, color="#475569")
    save_figure(fig, assets, "textcnn_vs_bilstm_training")


def plot_confusion(metrics, assets):
    fig, axes = plt.subplots(1, 2, figsize=(14.5, 6.8), layout="constrained")
    fig.suptitle("TextCNN 与 BiLSTM：测试集混淆矩阵", fontsize=21, weight="bold")
    for ax, (name, values) in zip(axes, metrics.items()):
        matrix = np.asarray(values["confusion_matrix"])
        image = ax.imshow(matrix, cmap="Blues", vmin=0, vmax=1900)
        for (row, column), count in np.ndenumerate(matrix):
            ax.text(column, row, str(count), ha="center", va="center", fontsize=13,
                    color="white" if count > 950 else "#172B4D")
        ax.set_xticks(range(4), LABEL_NAMES)
        ax.set_yticks(range(4), LABEL_NAMES)
        ax.set_xlabel("预测类别")
        ax.set_ylabel("真实类别")
        ax.set_title(f"{name} · 第 {values['epoch']} 轮 · 准确率 {values['accuracy']:.3%}", fontsize=14, pad=14)
        ax.tick_params(length=0, pad=8)
        for spine in ax.spines.values():
            spine.set_visible(False)
    fig.colorbar(image, ax=axes, shrink=0.72, label="样本数（两图共用 0—1900 色标）", pad=0.035)
    fig.supxlabel("每行 1900 条，合计 7600 条；对角线表示分类正确的样本。", fontsize=11, color="#475569")
    save_figure(fig, assets, "textcnn_vs_bilstm_confusion")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    torch.set_num_threads(4)
    execution = read_json(RUN / "training_execution.json")
    textcnn_execution = read_json(TEXTCNN_RUN / "training_execution.json")
    if execution["status"] != "completed" or execution["completed_epochs"] != 20:
        raise RuntimeError("请先完成全部 20 轮正式训练和测试评估")
    assets = EXPERIMENT / "assets"
    data_dir = EXPERIMENT / "data"
    assets.mkdir(exist_ok=True)
    data_dir.mkdir(exist_ok=True)
    baseline = read_json(TEXTCNN_DATA / "metrics.json")
    baseline_path = TEXTCNN_RUN / "best_accuracy.pt"
    assert hashlib.sha256(baseline_path.read_bytes()).hexdigest() == baseline["checkpoint_sha256"]
    textcnn = torch.load(baseline_path, map_location="cpu", weights_only=True)
    bilstm_path = RUN / "best_accuracy.pt"
    bilstm = torch.load(bilstm_path, map_location="cpu", weights_only=True)
    assert textcnn["vocab"] == bilstm["vocab"]
    for field in ("seed", "data", "training"):
        assert textcnn["config"][field] == bilstm["config"][field], field
    export_dir = RUN / "comparison_evaluation"
    if not (export_dir / "metrics.json").exists():
        infer_checkpoint(bilstm_path, export_dir)
    candidate = read_json(export_dir / "metrics.json")
    assert hashlib.sha256(bilstm_path.read_bytes()).hexdigest() == candidate["checkpoint_sha256"]
    labels, before = validate_predictions(TEXTCNN_DATA, baseline)
    after_labels, after = validate_predictions(export_dir, candidate)
    assert np.array_equal(labels, after_labels)
    assert prediction_identity(TEXTCNN_DATA) == prediction_identity(export_dir)
    assert abs(candidate["accuracy"] - execution["test_metrics"]["accuracy"]) < 1e-12
    groups = error_groups(labels, before, after)
    assert baseline["errors"] - candidate["errors"] == len(groups["fixed"]) - len(groups["new_errors"])
    metrics = {"TextCNN": baseline, "BiLSTM": candidate}
    histories = {"TextCNN": read_history(TEXTCNN_RUN / "metrics.csv"), "BiLSTM": read_history(RUN / "metrics.csv")}
    for rows in histories.values():
        assert [int(row["epoch"]) for row in rows] == list(range(1, 21))
        assert all(np.isfinite(value) for row in rows for value in row.values())
    font = Path("C:/Windows/Fonts/msyh.ttc")
    if font.exists():
        font_manager.fontManager.addfont(str(font))
        plt.rcParams["font.family"] = font_manager.FontProperties(fname=str(font)).get_name()
    plt.rcParams.update({"font.size": 11, "axes.unicode_minus": False, "svg.fonttype": "none"})
    plot_overview(metrics, assets)
    plot_history(histories, metrics, assets)
    plot_confusion(metrics, assets)
    summary = dict(models=metrics, accuracy_delta_percentage_points=(candidate["accuracy"] - baseline["accuracy"]) * 100,
                   macro_f1_delta_percentage_points=(candidate["macro_f1"] - baseline["macro_f1"]) * 100,
                   error_reduction=baseline["errors"] - candidate["errors"],
                   paired_error_groups={key: len(value) for key, value in groups.items()},
                   recorded_training_seconds={"TextCNN": textcnn_execution["elapsed_seconds"], "BiLSTM": execution["training_seconds"]},
                   provenance=dict(textcnn_predictions=str(TEXTCNN_DATA / "predictions.npz"),
                                   bilstm_predictions=str(export_dir / "predictions.npz"),
                                   same_seed_data_training_and_vocabulary=True, training_seconds=execution["training_seconds"]))
    write_json(data_dir / "comparison_summary.json", summary)
    with (data_dir / "comparison_metrics.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=["model", "selected_epoch", "test_accuracy", "macro_f1", "test_loss", "errors", "parameters"])
        writer.writeheader()
        for name, values in metrics.items():
            writer.writerow(dict(model=name, selected_epoch=values["epoch"], test_accuracy=values["accuracy"],
                                 macro_f1=values["macro_f1"], test_loss=values["loss"], errors=values["errors"], parameters=values["parameters"]))
    with (data_dir / "paired_predictions.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(["sample_id", "label", "textcnn_prediction", "bilstm_prediction"])
        writer.writerows((f"test:{i}", LABEL_NAMES[y], LABEL_NAMES[b], LABEL_NAMES[a]) for i, (y, b, a) in enumerate(zip(labels, before, after)))
    rows = ["# TextCNN 与 BiLSTM 正式实验对比", "", "两者使用相同的 AG-news 数据划分、词表、随机种子和训练超参数；均训练 20 轮，按验证准确率选权重后报告测试集结果。", "",
            "| 指标 | 原最佳 TextCNN | 本次 BiLSTM |", "| --- | ---: | ---: |"]
    for label, key, fmt in [("选中轮次", "epoch", "d"), ("测试准确率", "accuracy", ".4%"),
                            ("Macro-F1", "macro_f1", ".4%"), ("测试损失", "loss", ".6f"),
                            ("错误数 / 7600", "errors", "d"), ("参数量", "parameters", ",d")]:
        rows.append(f"| {label} | {format(baseline[key], fmt)} | {format(candidate[key], fmt)} |")
    rows.append(f"| 记录中的 20 轮训练用时 | {textcnn_execution['elapsed_seconds']/60:.2f} 分钟 | {execution['training_seconds']/60:.2f} 分钟 |")
    rows += ["", f"本次 BiLSTM 的测试准确率变化为 **{summary['accuracy_delta_percentage_points']:+.4f} 个百分点**，"
             f"Macro-F1 变化为 {summary['macro_f1_delta_percentage_points']:+.4f} 个百分点。"
             f"它修正了 TextCNN 的 {len(groups['fixed'])} 条错误，同时新增 {len(groups['new_errors'])} 条错误，"
             f"错误总数由 {baseline['errors']} 条变为 {candidate['errors']} 条。", "",
             "BiLSTM 的 World、Business 类 F1 高于 TextCNN，Sports、Sci/Tech 类 F1 略低；"
             "Business 与 Sci/Tech 的双向混淆从 259 条变为 255 条，仍是两者主要的错误来源。", "",
             "两者选中的权重都来自第 8 轮。BiLSTM 后续训练准确率继续升高，但验证损失从第 8 轮的 "
             f"{histories['BiLSTM'][7]['val_loss']:.4f} 升至第 20 轮的 {histories['BiLSTM'][-1]['val_loss']:.4f}，"
             "呈现过拟合。更晚的轮次没有带来更好的验证表现。", "",
             "## 对比图", "", "![整体指标与各类别 F1](assets/textcnn_vs_bilstm_overview.png)", "",
             "![20 轮训练曲线](assets/textcnn_vs_bilstm_training.png)", "",
             "![混淆矩阵](assets/textcnn_vs_bilstm_confusion.png)", "",
             "图表提供 PNG 和 SVG；原始汇总和对齐后的逐样本预测在 `data/`。",
             "", "## 结果范围", "",
             "这是单个随机种子的两次运行对比，尚不能据此推断 BiLSTM 在所有训练条件下都更好或更差。"
             "原 TextCNN 已经做过多组调参，本次 BiLSTM 是首个基线；历史调参期间查看过测试结果，"
             "这里保留这一限制，不把差异解释为严格的模型架构因果结论。", "",
             f"BiLSTM 正式训练耗时 {execution['training_seconds'] / 60:.2f} 分钟。"
             "训练全过程未用测试集选择轮次。模型权重和执行记录保存在 `.build/task2/runs/bilstm_baseline_20261103/`。", ""]
    (EXPERIMENT / "2026-11-03_textcnn_vs_bilstm.md").write_text("\n".join(rows), encoding="utf-8")
    HANDOFF.mkdir(parents=True, exist_ok=True)
    for path in assets.iterdir():
        if path.suffix in (".png", ".svg"):
            shutil.copy2(path, HANDOFF / path.name)
    for name in ("comparison_summary.json", "comparison_metrics.csv"):
        shutil.copy2(data_dir / name, HANDOFF / name)
    print(json.dumps(summary, ensure_ascii=False, indent=2), flush=True)
    print(f"图表交付目录：{HANDOFF}", flush=True)


if __name__ == "__main__":
    main()
