"""从已核验的随机种子统计生成各组 Markdown 报告、汇总报告和 PNG/SVG。"""

import csv
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.ticker import PercentFormatter
import numpy as np

PROJECT = Path(__file__).resolve().parents[2]
OUT = PROJECT / "experiments/random_seeds"
COLORS = {"textcnn": "#2563A6", "bilstm": "#D77A22"}
DISPLAY = {"textcnn": "TextCNN", "bilstm": "BiLSTM"}
CLASSES = ["World", "Sports", "Business", "Sci/Tech"]
REPORT_NAME = "2026-11-03_textcnn_vs_bilstm.md"


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def history(seed, model):
    path = PROJECT.parent / f".build/task2/runs/random_seeds_20261103/seed_{seed}/{model}/metrics.csv"
    with path.open(encoding="utf-8", newline="") as source:
        return [{k: float(v) for k, v in row.items()} for row in csv.DictReader(source)]


def save(fig, folder, name):
    folder.mkdir(exist_ok=True, parents=True)
    for extension in ("png", "svg"):
        fig.savefig(folder / f"{name}.{extension}", dpi=170, facecolor="white")
    plt.close(fig)


def style(ax):
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", color="#E2E8F0", linewidth=0.8)
    ax.set_axisbelow(True)


def pair_plots(row):
    seed = row["seed"]
    target = OUT / f"seed_{seed}/assets"
    fig, axes = plt.subplots(1, 2, figsize=(13.5, 5.3), layout="constrained")
    fig.suptitle(f"训练种子 {seed} · 训练与验证曲线（划分种子固定 42）", fontsize=19)
    for name in COLORS:
        values = history(seed, name)
        epochs = [r["epoch"] for r in values]
        for ax, key in zip(axes, ("accuracy", "loss")):
            for split, line in (("train", "--"), ("val", "-")):
                ax.plot(epochs, [r[f"{split}_{key}"] for r in values], linestyle=line,
                        color=COLORS[name], linewidth=1.8,
                        label=f"{DISPLAY[name]} {'训练' if split == 'train' else '验证'}")
            ax.set_xlabel("训练轮次")
            ax.set_ylabel("准确率" if key == "accuracy" else "交叉熵")
            ax.set_xticks(range(1, 21, 2))
            style(ax)
        selected = row["training"][name]["selected_epoch"]
        axes[0].scatter([selected], [values[selected - 1]["val_accuracy"]],
                        color=COLORS[name], marker="D", s=50, zorder=4)
    axes[0].yaxis.set_major_formatter(PercentFormatter(1))
    axes[0].legend(frameon=False, fontsize=9, loc="lower right")
    fig.supxlabel("实线为验证，虚线为训练；菱形为最高验证准确率权重。测试集未用于选择轮次。", fontsize=10, color="#475569")
    save(fig, target, "training_curves")
    fig, axes = plt.subplots(1, 2, figsize=(13, 6), layout="constrained")
    fig.suptitle(f"训练种子 {seed} · 官方测试集混淆矩阵", fontsize=19)
    for ax, name in zip(axes, COLORS):
        metric = row["metrics"][name]
        matrix = np.array(metric["confusion_matrix"])
        im = ax.imshow(matrix, cmap="Blues", vmin=0, vmax=1900)
        for (i, j), value in np.ndenumerate(matrix):
            ax.text(j, i, str(value), ha="center", va="center", color="white" if value > 950 else "#172B4D", fontsize=12)
        ax.set_xticks(range(4), CLASSES)
        ax.set_yticks(range(4), CLASSES)
        ax.set_xlabel("预测类别")
        ax.set_ylabel("真实类别")
        ax.set_title(f"{DISPLAY[name]} · {metric['accuracy']:.4%}", pad=12)
        ax.tick_params(length=0)
    fig.colorbar(im, ax=axes, shrink=0.7, label="样本数（共用色标）", pad=0.02)
    fig.supxlabel("每类 1900 条，总计 7600 条；行是真实类别，列是预测类别。", fontsize=10, color="#475569")
    save(fig, target, "confusion")


def aggregate_plots(summary):
    rows = summary["runs"]
    target = OUT / "assets"
    fig, ax = plt.subplots(figsize=(11.5, 5.6), layout="constrained")
    fig.suptitle("固定配置在不同训练种子上的测试准确率", fontsize=19)
    x = np.arange(4)
    all_values = []
    for offset, name in ((-0.11, "textcnn"), (0.11, "bilstm")):
        values = [r["metrics"][name]["accuracy"] for r in rows] + [summary["historical_seed42"][name]["accuracy"]]
        all_values += values
        ax.scatter(x + offset, values, color=COLORS[name], marker="o" if name == "textcnn" else "D", s=75, label=DISPLAY[name], zorder=4)
        for i, value in enumerate(values):
            ax.annotate(f"{value:.4%}", (x[i] + offset, value), xytext=(-8 if offset < 0 else 8, -19 if offset < 0 else 8),
                        textcoords="offset points", ha="right" if offset < 0 else "left", fontsize=10, color=COLORS[name])
    ax.axvline(2.5, color="#94A3B8", linestyle="--", linewidth=1)
    ax.set_xticks(x, [str(r["seed"]) for r in rows] + ["42\n历史参考"])
    ax.set_xlim(-0.6, 3.65)
    ax.set_ylim(min(all_values) - 0.004, max(all_values) + 0.004)
    ax.yaxis.set_major_formatter(PercentFormatter(1))
    ax.set_xlabel("训练种子（训练/验证划分种子均固定 42）")
    ax.set_ylabel("测试准确率（局部刻度）")
    ax.legend(frameon=False, loc="upper left", ncol=2)
    style(ax)
    fig.supxlabel("每个点对应一次训练、同一批 7600 条测试样本；新增三个种子为主分析，42 为此前实验。", fontsize=10, color="#475569")
    save(fig, target, "accuracy_by_seed")
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.8), layout="constrained")
    fig.suptitle("三个新增种子的均值与波动", fontsize=19)
    for ax, key, title in zip(axes, ("accuracy", "macro_f1"), ("测试准确率", "Macro-F1")):
        for i, name in enumerate(COLORS):
            result = summary["primary"][name][key]
            ax.errorbar(result["mean"], i, xerr=result["sample_std"], fmt="o" if name == "textcnn" else "D", color=COLORS[name], capsize=6, markersize=9)
            ax.annotate(f"{result['mean']:.4%} ± {result['sample_std'] * 100:.4f} pp", (result["mean"], i),
                        xytext=(0, 16), textcoords="offset points", ha="center", fontsize=10)
        ax.set_yticks([0, 1], ["TextCNN", "BiLSTM"])
        ax.set_ylim(-0.6, 1.6)
        ax.xaxis.set_major_formatter(PercentFormatter(1))
        ax.set_title(title)
        ax.set_xlabel("均值 ± 样本标准差（局部刻度）")
        ax.grid(axis="x", color="#E2E8F0")
        ax.spines[["top", "right"]].set_visible(False)
    fig.supxlabel("n=3，种子 17/2024/3407；误差线为 ddof=1 的样本标准差，不是置信区间。", fontsize=10, color="#475569")
    save(fig, target, "mean_std")
    fig, ax = plt.subplots(figsize=(11.5, 5), layout="constrained")
    fig.suptitle("每个新增种子的配对错误变化", fontsize=19)
    x = np.arange(3)
    for offset, key, label, color in ((-0.25, "fixed", "BiLSTM 修正", COLORS["textcnn"]),
                                      (0, "both_wrong", "两者共同错误", "#64748B"),
                                      (0.25, "new_errors", "BiLSTM 新增", COLORS["bilstm"])):
        bars = ax.bar(x + offset, [r["groups"][key] for r in rows], width=0.23, label=label, color=color)
        ax.bar_label(bars, padding=3)
    ax.set_xticks(x, [f"种子 {r['seed']}" for r in rows])
    ax.set_ylim(0, max(r["groups"]["both_wrong"] for r in rows) * 1.22)
    ax.set_ylabel("样本数")
    ax.legend(frameon=False, ncol=3, loc="upper center")
    style(ax)
    fig.supxlabel("以同种子的 TextCNN 为参照：净减少错误 = 修正数 − 新增数；每组测试样本均为 7600。", fontsize=10, color="#475569")
    save(fig, target, "paired_errors")
    fig, ax = plt.subplots(figsize=(10.5, 5), layout="constrained")
    fig.suptitle("同一测试样本在三个新增种子中被分错的次数", fontsize=18)
    for offset, name in ((-0.18, "textcnn"), (0.18, "bilstm")):
        values = [summary["error_frequency_new_seeds"][name][str(k)] for k in (1, 2, 3)]
        bars = ax.bar(np.arange(3) + offset, values, width=0.34, color=COLORS[name], label=DISPLAY[name],
                      hatch="//" if name == "bilstm" else "", edgecolor="white")
        ax.bar_label(bars, padding=3)
    ax.set_xticks(range(3), ["只错 1 个种子", "错 2 个种子", "三个种子都错"])
    ax.set_ylabel("不同测试样本数")
    ax.set_ylim(0, max(int(r.get(str(k), 0)) for r in summary["error_frequency_new_seeds"].values() for k in (1, 2, 3)) * 1.2)
    ax.legend(frameon=False)
    style(ax)
    fig.supxlabel("按原始测试 ID 对齐；只展示至少错一次的样本，三个种子都正确的数量见报告。", fontsize=10, color="#475569")
    save(fig, target, "error_frequency")


def write_pair(row):
    seed = row["seed"]
    a, b = row["metrics"]["textcnn"], row["metrics"]["bilstm"]
    groups = row["groups"]
    net = b["correct"] - a["correct"]
    outcome = "更高" if net > 0 else "更低" if net < 0 else "相同"
    net_description = f"净减少 {net} 条" if net >= 0 else f"净增加 {-net} 条"
    contents = [f"# 训练种子 {seed}：TextCNN 与 BiLSTM 重新实验", "", "实验日期：2026-11-03；训练/验证划分种子固定为 42。", "",
                f"本组 BiLSTM 测试准确率为 **{b['accuracy']:.4%}**，TextCNN 为 **{a['accuracy']:.4%}**，BiLSTM {outcome}，差值为 **{row['accuracy_delta_pp']:+.4f} 个百分点**。"
                f"以 TextCNN 为参照，BiLSTM 修正 {groups['fixed']} 条、增加 {groups['new_errors']} 条错误，{net_description}。此处是一个种子的结果，最终判断见[三组汇总报告](../2026-11-03_random_seed_summary.md)。", "",
                "## 训练设置与权重选择", "",
                "本轮沿用之前已确定的两个最终方案。TextCNN 使用卷积核 2/3/7、分类 Dropout=0.5；BiLSTM 使用单层双向 LSTM，每方向隐藏维度 128、词嵌入 Dropout=0.2、分类 Dropout=0.5。两者词嵌入均为随机初始化 128 维，Adam 学习率 0.001、WD=1e-4、batch size=64、验证损失驱动降学习率。", "",
                "训练/验证/测试样本数为 108000/12000/7600，分词、42396 项词表、最大长度 256 与历史实验一致。固定划分种子 42，仅改变模型初始化、训练批次顺序及 Dropout 的随机种子。数据编码和词表哈希已跨六次训练核对，详见[训练核验](../training_verification.json)。", "",
                "| 模型 | 实际轮次 | 选中轮次 | 验证准确率 | 测试准确率 | Macro-F1 | 测试错误 | 测试交叉熵 |", "|---|---:|---:|---:|---:|---:|---:|---:|"]
    for name in COLORS:
        metric, run = row["metrics"][name], row["training"][name]
        contents.append(f"| {DISPLAY[name]} | {run['summary']['completed_epochs']} | {run['selected_epoch']} | {metric['val_accuracy']:.4%} | {metric['accuracy']:.4%} | {metric['macro_f1']:.4%} | {metric['errors']} | {metric['loss']:.6f} |")
    contents += ["", "TextCNN 保留原 20 轮训练流程；BiLSTM 保留验证损失早停（patience=3、min_delta=0.001），最大 20 轮。两者分别保存最高验证准确率权重，同准确率时选验证损失更低者。六次训练全部完成并核验后才统一评估固定权重，测试集不参与选种子或选轮次。", "",
                 "![训练与验证曲线](assets/training_curves.png)", "", "曲线展示拟合过程，两个模型的训练策略不同，本次结果反映最终方案的比较。不能把差值全部归因于模型结构或早停。", "",
                 "## 配对错误与类别表现", "", "| 结果 | 数量 |", "|---|---:|",
                 f"| 两者正确 | {groups['both_correct']} |", f"| BiLSTM 修正 | {groups['fixed']} |",
                 f"| 两者错误 | {groups['both_wrong']} |", f"| BiLSTM 新增 | {groups['new_errors']} |", "",
                 f"精确双侧 McNemar 检验 p={row['mcnemar_exact_p']:.6f}，仅作本组配对诊断；本轮三个逐种子检验未作多重比较校正，单组较小的 p 值不能代表跨种子整体显著。三个种子不是三个独立测试集，不能合并为 22800 条独立样本来夸大证据。", "",
                 "![测试集混淆矩阵](assets/confusion.png)", "", "| 真实类别（每类 1900 条） | TextCNN 错误 | BiLSTM 错误 | TextCNN F1 | BiLSTM F1 |", "|---|---:|---:|---:|---:|"]
    for ca, cb in zip(a["per_class"], b["per_class"]):
        contents.append(f"| {ca['label']} | {ca['errors']} | {cb['errors']} | {ca['f1']:.4%} | {cb['f1']:.4%} |")
    ac, bc = a["confusion_matrix"], b["confusion_matrix"]
    contents += ["", f"商业→科技误分为 {ac[2][3]}→{bc[2][3]} 条，科技→商业为 {ac[3][2]}→{bc[3][2]} 条；"
                 f"科技→体育为 {ac[3][1]}→{bc[3][1]} 条。方向性差异需要结合三组结果判断，不能只挑选改善的一侧。", "",
                 "## 数据与复现", "", "- 配置：[TextCNN](configs/textcnn.json)、[BiLSTM](configs/bilstm.json)。",
                 "- 指标和原始概率：[TextCNN 指标](data/textcnn/metrics.json)、[BiLSTM 指标](data/bilstm/metrics.json)，同目录保留 `predictions.npz` 与全量预测 CSV。",
                 "- 配对清单：[全部样本](data/paired_predictions.csv)、[修正](data/fixed.csv)、[新增](data/new_errors.csv)、[共同错误](data/both_wrong.csv)。",
                 "- [本组汇总 JSON](data/summary.json)、[预先固定的实验方案](../protocol.json)。", "",
                 f"权重及逐轮日志位于仓库根目录 `.build/task2/runs/random_seeds_20261103/seed_{seed}/textcnn/` 和 `.../bilstm/`；`execution.json` 记录源码、数据编码、初始化与最终权重哈希。图表均有同名 SVG。", "",
                 "```powershell", f"# 在仓库根目录、尚无同名训练目录时运行；已有结果不会覆盖", f"python task2_简单分类模型设计与实现/experiments/scripts/run_random_seeds.py --seed {seed} --model textcnn",
                 f"python task2_简单分类模型设计与实现/experiments/scripts/run_random_seeds.py --seed {seed} --model bilstm", "```", ""]
    target = OUT / f"seed_{seed}"
    (target / REPORT_NAME).write_text("\n".join(contents), encoding="utf-8")
    (target / "README.md").write_text(f"# 随机种子 {seed}\n\n[本组结果分析报告]({REPORT_NAME})\n\n[返回三组汇总](../2026-11-03_random_seed_summary.md)\n", encoding="utf-8")


def write_aggregate(s):
    a, b = s["primary"]["textcnn"], s["primary"]["bilstm"]
    delta, wins = s["accuracy_delta_pp"], s["bilstm_wins"]
    verdict = "三个新增种子中均取得更高准确率" if wins == 3 else f"三个新增种子中有 {wins} 组准确率更高"
    contents = ["# 三组新增随机种子：TextCNN 与 BiLSTM 复现实验分析", "", "实验日期：2026-11-03。新增训练种子 17、2024、3407；数据划分种子固定 42。", "",
                f"固定此前选定的两个方案后，BiLSTM 在{verdict}。其平均准确率为 **{b['accuracy']['mean']:.4%} ± {b['accuracy']['sample_std'] * 100:.4f} 个百分点**，"
                f"TextCNN 为 **{a['accuracy']['mean']:.4%} ± {a['accuracy']['sample_std'] * 100:.4f} 个百分点**，配对平均差为 **{delta['mean']:+.4f} 个百分点**。± 表示三个种子间的样本标准差。", "",
                "本轮完成六次重新训练和六次固定权重测试评估，未按测试成绩删除种子或另选配置。三个种子共享同一测试集，主要用于观察训练随机性；不能把它们当作三个独立数据集，也不能凭三个点宣称已经证明架构具有普遍优势。", "",
                "## 1. 每个种子的实际结果", "", "| 训练种子 | TextCNN 准确率 | BiLSTM 准确率 | 差值（百分点） | TextCNN 错误 | BiLSTM 错误 | BiLSTM 修正 / 新增 |", "|---|---:|---:|---:|---:|---:|---:|"]
    for row in s["runs"]:
        ca, cb, g = row["metrics"]["textcnn"], row["metrics"]["bilstm"], row["groups"]
        contents.append(f"| [{row['seed']}](seed_{row['seed']}/{REPORT_NAME}) | {ca['accuracy']:.4%} | {cb['accuracy']:.4%} | {row['accuracy_delta_pp']:+.4f} | {ca['errors']} | {cb['errors']} | {g['fixed']} / {g['new_errors']} |")
    ha, hb = s["historical_seed42"]["textcnn"], s["historical_seed42"]["bilstm"]
    contents += [f"| 42（历史参考） | {ha['accuracy']:.4%} | {hb['accuracy']:.4%} | {(hb['accuracy'] - ha['accuracy']) * 100:+.4f} | {ha['errors']} | {hb['errors']} | 192 / 166 |", "",
                 "![各种子准确率](assets/accuracy_by_seed.png)", "",
                 f"新增三组的准确率差值范围为 **{delta['min']:+.4f} 至 {delta['max']:+.4f} 个百分点**，配对差值的样本标准差为 **{delta['sample_std']:.4f} 个百分点**。平均值与每组差值一起解释，避免单个最高结果代表整个方案。", "",
                 "## 2. 跨种子的均值与波动", "", "| 指标（仅新增三种子） | TextCNN 均值 ± 样本标准差 | BiLSTM 均值 ± 样本标准差 |", "|---|---:|---:|"]
    for key, label in (("accuracy", "准确率"), ("macro_f1", "Macro-F1")):
        contents.append(f"| {label} | {a[key]['mean']:.4%} ± {a[key]['sample_std'] * 100:.4f} pp | {b[key]['mean']:.4%} ± {b[key]['sample_std'] * 100:.4f} pp |")
    for key, label in (("loss", "测试交叉熵"), ("errors", "每次测试错误数")):
        contents.append(f"| {label} | {a[key]['mean']:.4f} ± {a[key]['sample_std']:.4f} | {b[key]['mean']:.4f} ± {b[key]['sample_std']:.4f} |")
    contents += ["", "![均值和标准差](assets/mean_std.png)", "",
                 "标准差采用 `ddof=1`，描述训练种子之间的波动，**不是置信区间**。本次仅三个新增种子，不给出精确的总体稳定性保证，也不将逐样本配对检验当作跨种子重复实验的替代。", "",
                 "补充加入历史种子 42 后，四种子的描述统计为：", "", "| 模型 | 四种子准确率均值 | 样本标准差（百分点） |", "|---|---:|---:|"]
    for name in COLORS:
        r = s["including_historical_seed42_accuracy"][name]
        contents.append(f"| {DISPLAY[name]} | {r['mean']:.4%} | {r['sample_std'] * 100:.4f} |")
    contents += ["", "种子 42 是此前调参与方案选择所在的历史实验，本轮没有重跑；其结果作为次要参考。主结果始终是三个预先指定的新种子，避免把历史选型结果和新增复现结果混为同一批确认性证据。", "",
                 "## 3. 净改善之外，错误是否持续出现", "", "![每种子的错误交换](assets/paired_errors.png)", "",
                 "修正数大于新增数表示本组净改善；两者共同错误则反映当前两个方案都未解决的样本。详细清单与混淆矩阵分别放在各随机种子文件夹。", "",
                 "按测试 ID 对齐三个新增种子后，同一条新闻的错误重复情况如下。每一列均按不同新闻计数，四行合计 7600；不是将三个种子的错误条数直接累加。", "",
                 "| 同一模型在三个新增种子中的错误次数 | TextCNN 样本数 | BiLSTM 样本数 |", "|---|---:|---:|"]
    for k in range(4):
        contents.append(f"| {k} | {s['error_frequency_new_seeds']['textcnn'][str(k)]} | {s['error_frequency_new_seeds']['bilstm'][str(k)]} |")
    contents += ["", "![错误在三个种子间的重复情况](assets/error_frequency.png)", "",
                 f"两个模型均在三个新增种子上持续分错的新闻有 **{s['both_models_wrong_all_three']} 条**。这些样本可作为后续主题边界与标注一致性复核的候选，"
                 "但不能据此直接删除样本或修改官方测试标签。重复错误也不自动等于标注有误。", "",
                 "## 4. 各类别与主要混淆方向", "", "下表为三个新增种子的每次测试平均错误数，每类每次均有 1900 条；平均错误数可能为小数。", "",
                 "| 真实类别 | TextCNN 平均错误 | BiLSTM 平均错误 | BiLSTM − TextCNN |", "|---|---:|---:|---:|"]
    for i, label in enumerate(CLASSES):
        ca = np.mean([r["metrics"]["textcnn"]["per_class"][i]["errors"] for r in s["runs"]])
        cb = np.mean([r["metrics"]["bilstm"]["per_class"][i]["errors"] for r in s["runs"]])
        contents.append(f"| {label} | {ca:.2f} | {cb:.2f} | {cb - ca:+.2f} |")
    contents += ["", "| 误分方向 | TextCNN 三种子平均次数 | BiLSTM 三种子平均次数 |", "|---|---:|---:|"]
    for i, j in ((2, 3), (3, 2), (3, 1), (0, 2)):
        ca = np.mean([r["metrics"]["textcnn"]["confusion_matrix"][i][j] for r in s["runs"]])
        cb = np.mean([r["metrics"]["bilstm"]["confusion_matrix"][i][j] for r in s["runs"]])
        contents.append(f"| {CLASSES[i]} → {CLASSES[j]} | {ca:.2f} | {cb:.2f} |")
    business_changes = [r["metrics"]["bilstm"]["per_class"][2]["errors"] - r["metrics"]["textcnn"]["per_class"][2]["errors"] for r in s["runs"]]
    business_description = "、".join(f"种子 {r['seed']}：{change:+d} 条" for r, change in zip(s["runs"], business_changes))
    contents += ["", "这里保留相反方向的商业/科技误分，以及此前发现可能恶化的科技/体育方向；结论应结合方向变化，而非仅看总准确率。每组报告还保留精确率、召回率对应的原始指标文件。", "",
                 f"商业类错误的逐种子变化为：**{business_description}**。本轮均值恶化主要受种子 17 影响，不能解读为每个种子都发生相同程度的商业类退化。种子 3407 的科技类错误也由 200 增至 205，即使整体准确率上升，个别类别仍可能受损。", "",
                 "## 5. 本轮结果的含义", "",
                 f"三个新增种子的整体准确率均高于各自 TextCNN，净增加正确数分别为 {', '.join(str(r['metrics']['bilstm']['correct'] - r['metrics']['textcnn']['correct']) for r in s['runs'])} 条。"
                 f"其平均优势 {delta['mean']:.4f} 个百分点与历史种子 42 的 {(hb['accuracy'] - ha['accuracy']) * 100:.4f} 个百分点接近，说明本轮观察到的提升方向在新增种子中得到重复。Macro-F1 平均也提高 {(b['macro_f1']['mean'] - a['macro_f1']['mean']) * 100:.4f} 个百分点，且三组交叉熵均更低。", "",
                 f"BiLSTM 的准确率标准差为 {b['accuracy']['sample_std'] * 100:.4f} 个百分点，高于 TextCNN 的 {a['accuracy']['sample_std'] * 100:.4f} 个百分点，因此本轮较高的平均准确率没有伴随更小的种子间波动。"
                 f"三个新增种子始终分错的样本数为 TextCNN {s['error_frequency_new_seeds']['textcnn']['3']} 条、BiLSTM {s['error_frequency_new_seeds']['bilstm']['3']} 条，数量仍然接近；主题边界和持续错误没有随着均值提升而消失。", "",
                 "逐种子的 McNemar 检验未做多重比较校正，且都是同一测试集上的探索性诊断；不能挑出种子 2024 的 p<0.05，就宣称跨种子的整体优势已经具有统计显著性。结合重复方向与小样本限制，本轮支持保留当前 BiLSTM 方案继续使用，但仍应把优势描述为本数据划分上的小幅提升。", "",
                 "后续若继续改进，应优先在训练/验证数据上检查商业新闻中的科技背景词，以及两个模型持续分错的主题边界案例；保留整体和逐类指标，避免用单个平均准确率掩盖类别退化。本轮不根据测试成绩替换当前权重，也不据此修改官方测试标签。", "",
                 "## 6. 训练条件、限制与复现", "",
                 "- 固定官方数据、训练/验证划分种子 42、42396 项训练词表、最大长度 256；仅改变初始化、批次采样与 Dropout 使用的训练种子。新配置增加 `data.split_seed=42`；旧配置不带该字段时仍按原 `seed` 划分，兼容性已测试。",
                 "- 两个方案的其余参数完全沿用之前选定的配置：TextCNN 卷积核 2/3/7、20 轮；BiLSTM 词嵌入 Dropout=0.2、验证损失早停，最大 20 轮。两者均按验证准确率选择权重，同准确率比较验证损失。",
                 "- 这是最终方案的复现比较，结构与正则化、停止策略的作用混合存在，不能把差距全部解释为架构收益。训练时最多两个进程共享一张 GPU，因此执行时长受并发负载影响，不用于证明模型推理速度优劣。",
                 "- 沿用现有 PyTorch/CUDA 默认执行设置，没有额外启用严格确定性算法。固定种子控制了主要随机源，但不承诺不同设备或软件版本下逐位一致。",
                 "- 六次训练完成后才开始本轮测试评估；保留全部种子。当前测试集此前已用于错误分析，新增种子没有消除测试集反复使用与选型带来的偏差，新的泛化结论仍需独立保留数据。", "",
                 "原始配置、各组完整训练日志、最佳轮次、源码/数据/权重哈希均有记录。跨六次训练的编码序列与词表哈希一致，同一模型的三个初始参数哈希互不相同。", "",
                 "| 证据 | 位置 |", "|---|---|", "| 预先固定的种子、方案与原配置哈希 | [protocol.json](protocol.json) |",
                 "| 训练完成、数据一致性与初始化差异检查 | [training_verification.json](training_verification.json) |",
                 "| 六次训练/测试的指标表 | [results.csv](data/results.csv) |", "| 完整统计与各组配对结果 | [summary.json](data/summary.json) |",
                 "| 7600 条新闻的跨种子错误频率 | [error_frequency.csv](data/error_frequency.csv) |",
                 "| 最终独立核验记录 | [verification.json](verification.json) |", "",
                 "在仓库根目录、激活 `d2l-pytorch` 环境后，结果汇总与报告可复现：", "", "```powershell",
                 "python task2_简单分类模型设计与实现/experiments/scripts/analyze_random_seeds.py --evaluate",
                 "python task2_简单分类模型设计与实现/experiments/scripts/report_random_seeds.py",
                 "python task2_简单分类模型设计与实现/experiments/scripts/verify_random_seeds.py", "```", "",
                 "分析脚本在评估前检查全部六次训练；已有完整测试评估会被核验并复用。图表 PNG 与同名 SVG 保存在汇总或各组 `assets/` 中。训练目录不允许覆盖，重新训练应另设新的输出目录。", ""]
    (OUT / "2026-11-03_random_seed_summary.md").write_text("\n".join(contents), encoding="utf-8")
    index = ["# TextCNN 与 BiLSTM 随机种子复现实验", "", "[三组新增随机种子结果分析报告](2026-11-03_random_seed_summary.md)", "",
             f"已完成种子 17、2024、3407 的六次训练。BiLSTM 平均准确率 {b['accuracy']['mean']:.4%}，TextCNN 为 {a['accuracy']['mean']:.4%}；平均差值 {delta['mean']:+.4f} 个百分点。", ""]
    for row in s["runs"]:
        index.append(f"- [种子 {row['seed']} 的独立报告](seed_{row['seed']}/{REPORT_NAME})。")
    index += ["", "配置、原始评估数据和图表分别位于各组目录；跨种子统计在本目录 `data/`，权重与完整训练日志在仓库根目录 `.build/task2/runs/random_seeds_20261103/`。主统计只包含新增三组，历史种子 42 单列参考，不选择测试成绩最高的种子。", ""]
    (OUT / "README.md").write_text("\n".join(index), encoding="utf-8")


def main():
    font = Path("C:/Windows/Fonts/msyh.ttc")
    font_manager.fontManager.addfont(str(font))
    plt.rcParams.update({"font.family": font_manager.FontProperties(fname=str(font)).get_name(),
                         "font.size": 11, "axes.unicode_minus": False, "svg.fonttype": "none"})
    summary = read_json(OUT / "data/summary.json")
    for row in summary["runs"]:
        pair_plots(row)
        write_pair(row)
    aggregate_plots(summary)
    write_aggregate(summary)
    print("Saved four Markdown reports, indexes and ten PNG/SVG figures.")


if __name__ == "__main__":
    main()
