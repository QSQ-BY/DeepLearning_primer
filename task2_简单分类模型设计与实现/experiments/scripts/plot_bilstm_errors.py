"""为最新 BiLSTM 错误分析 Markdown 报告生成真实数据图表。"""

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.colors import LinearSegmentedColormap, TwoSlopeNorm
from matplotlib.ticker import PercentFormatter
import numpy as np

PROJECT = Path(__file__).resolve().parents[2]
OUT = PROJECT / "experiments/bilstm/error_analysis"
COLORS = {"TextCNN": "#2563A6", "BiLSTM": "#D77A22"}
NAMES = ["World", "Sports", "Business", "Sci/Tech"]


def save(fig, name):
    for extension in ("png", "svg"):
        fig.savefig(OUT / "assets" / f"{name}.{extension}", dpi=180, facecolor="white")
    plt.close(fig)


def axis_style(ax):
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", color="#E2E8F0", linewidth=0.8)
    ax.set_axisbelow(True)


def main():
    summary = json.loads((OUT / "data/summary.json").read_text(encoding="utf-8"))
    (OUT / "assets").mkdir(exist_ok=True)
    font = Path("C:/Windows/Fonts/msyh.ttc")
    font_manager.fontManager.addfont(str(font))
    plt.rcParams.update({"font.family": font_manager.FontProperties(fname=str(font)).get_name(),
                         "font.size": 11, "axes.unicode_minus": False, "svg.fonttype": "none"})
    metrics = {"TextCNN": summary["textcnn"], "BiLSTM": summary["bilstm"]}
    fig, axes = plt.subplots(1, 2, figsize=(14.5, 6), layout="constrained")
    fig.suptitle("最新最佳 BiLSTM 与 TextCNN：错误数量及去向", fontsize=21, weight="bold")
    ax = axes[0]
    bars = ax.bar(list(metrics), [m["errors"] for m in metrics.values()], width=0.5, color=list(COLORS.values()))
    ax.bar_label(bars, padding=5)
    ax.set_ylim(0, 750)
    ax.set_ylabel("错误数")
    ax.set_title("各模型总错误", loc="left", pad=15)
    axis_style(ax)
    ax = axes[1]
    groups = summary["groups"]
    values = [groups[key] for key in ("fixed", "both_wrong", "new_errors")]
    bars = ax.bar(["BiLSTM 修正", "两者共同错误", "BiLSTM 新增"], values, width=0.55,
                  color=["#2563A6", "#64748B", "#D77A22"])
    ax.bar_label(bars, padding=5)
    ax.set_ylim(0, 500)
    ax.set_ylabel("样本数")
    ax.set_title("至少一个模型分错的 773 条样本", loc="left", pad=15)
    axis_style(ax)
    fig.supxlabel("官方测试集 n=7600；两者共同正确 6827 条；修正 192 条、新增 166 条，净减少 26 条错误。", color="#475569", fontsize=11)
    save(fig, "paired_error_groups")

    fig, axes = plt.subplots(1, 2, figsize=(14.5, 6.8), layout="constrained")
    fig.suptitle("最新最佳 BiLSTM 与 TextCNN：测试集混淆矩阵", fontsize=21, weight="bold")
    for ax, (name, m) in zip(axes, metrics.items()):
        matrix = np.array(m["confusion_matrix"])
        image = ax.imshow(matrix, cmap="Blues", vmin=0, vmax=1900)
        for (i, j), value in np.ndenumerate(matrix):
            ax.text(j, i, str(value), ha="center", va="center", fontsize=13, color="white" if value > 950 else "#172B4D")
        ax.set_xticks(range(4), NAMES)
        ax.set_yticks(range(4), NAMES)
        ax.set_xlabel("预测类别")
        ax.set_ylabel("真实类别")
        ax.set_title(f"{name} · 准确率 {m['accuracy']:.4%}", pad=14)
        ax.tick_params(length=0, pad=7)
    fig.colorbar(image, ax=axes, shrink=0.75, label="样本数（共用色标）", pad=0.03)
    fig.supxlabel("每类 1900 条，总计 7600 条；行表示真实类别，列表示预测类别。", color="#475569", fontsize=11)
    save(fig, "confusion_comparison")

    delta = np.array(summary["bilstm"]["confusion_matrix"]) - np.array(summary["textcnn"]["confusion_matrix"])
    mask = np.eye(4, dtype=bool)
    off_diagonal = np.ma.array(delta, mask=mask)
    cmap = LinearSegmentedColormap.from_list("blue_white_orange", ["#2563A6", "#FFFFFF", "#D77A22"])
    cmap.set_bad("#E2E8F0")
    fig, ax = plt.subplots(figsize=(9.5, 7.6), layout="constrained")
    image = ax.imshow(off_diagonal, cmap=cmap, norm=TwoSlopeNorm(vmin=-12, vcenter=0, vmax=12))
    for (i, j), value in np.ndenumerate(delta):
        ax.text(j, i, "-" if i == j else f"{value:+d}", ha="center", va="center", fontsize=17, color="#172B4D")
    ax.set_xticks(range(4), NAMES)
    ax.set_yticks(range(4), NAMES)
    ax.set_xlabel("预测类别")
    ax.set_ylabel("真实类别")
    ax.set_title("误分类方向变化：BiLSTM 错误数 - TextCNN 错误数", fontsize=16, pad=20)
    fig.colorbar(image, ax=ax, shrink=0.8, label="负数：错误减少；正数：错误增加")
    fig.supxlabel("只比较非对角的错误项；灰色对角不参与误分类方向比较。", fontsize=11, color="#475569")
    save(fig, "confusion_delta")

    fig, axes = plt.subplots(1, 2, figsize=(15.5, 6.4), layout="constrained")
    fig.suptitle("按文本长度与未知词划分的组内错误率", fontsize=21, weight="bold")
    for ax, segments, title in [(axes[0], summary["segments"][:3], "文本长度"), (axes[1], summary["segments"][3:], "是否包含未知词")]:
        x = np.arange(len(segments))
        for offset, name in [(-0.18, "TextCNN"), (0.18, "BiLSTM")]:
            key = "textcnn_error_rate" if name == "TextCNN" else "bilstm_error_rate"
            values = [row[key] for row in segments]
            bars = ax.bar(x+offset, values, width=0.34, label=name, color=COLORS[name],
                          hatch="//" if name == "BiLSTM" else "", edgecolor="white")
            ax.bar_label(bars, labels=[f"{v:.2%}" for v in values], padding=4, fontsize=10)
        ax.set_xticks(x, [f"{row['segment']}\nn={row['samples']}" for row in segments])
        ax.set_ylim(0, 0.205)
        ax.yaxis.set_major_formatter(PercentFormatter(1))
        ax.set_ylabel("组内错误率")
        ax.set_title(title, loc="left", pad=15)
        ax.legend(frameon=False)
        axis_style(ax)
    fig.supxlabel("错误率 = 组内错误数 / 组内样本数。两种分组方式分别统计，不能跨分组相加。", color="#475569", fontsize=11)
    save(fig, "feature_segment_errors")
    print("Saved four error-analysis figures in PNG and SVG.")


if __name__ == "__main__":
    main()
