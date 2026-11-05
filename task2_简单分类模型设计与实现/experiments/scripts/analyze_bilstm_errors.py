"""对齐最新最佳 BiLSTM 和历史最佳 TextCNN 的逐样本预测，导出错误证据。"""

import csv
import hashlib
import json
from pathlib import Path
import sys

import numpy as np
from scipy.stats import binomtest
import torch

PROJECT = Path(__file__).resolve().parents[2]
ROOT = PROJECT.parent
sys.path.insert(0, str(PROJECT))
from news_classifier.data import LABEL_NAMES, tokenize
from news_classifier.evaluation.analysis import cached_split, classification_metrics, error_groups, write_csv, write_json

OUTPUT = PROJECT / "experiments/bilstm/error_analysis"
TEXTCNN = PROJECT / "experiments/textcnn/error_analysis/data/kernel_comparison/k237"
BILSTM = ROOT / ".build/task2/runs/bilstm_es_dropout02_20261103/final_evaluation"


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_predictions(folder):
    metrics = read_json(folder / "metrics.json")
    checkpoint_path = Path(metrics["checkpoint"])
    assert hashlib.sha256(checkpoint_path.read_bytes()).hexdigest() == metrics["checkpoint_sha256"]
    checkpoint = torch.load(checkpoint_path, map_location="cpu", weights_only=True)
    with (folder / "all_predictions.csv").open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    with np.load(folder / "predictions.npz") as arrays:
        labels, predictions = arrays["labels"].copy(), arrays["predictions"].copy()
        probabilities, logits = arrays["probabilities"].copy(), arrays["logits"].copy()
    assert len(rows) == 7600
    assert labels.shape == predictions.shape == (7600,)
    assert probabilities.shape == logits.shape == (7600, 4)
    assert np.array_equal(logits.argmax(1), predictions)
    assert np.isfinite(logits).all() and np.isfinite(probabilities).all()
    np.testing.assert_allclose(probabilities.sum(1), 1, atol=1e-6)
    exponentials = np.exp(logits - logits.max(1, keepdims=True))
    np.testing.assert_allclose(probabilities, exponentials / exponentials.sum(1, keepdims=True), atol=1e-6)
    recalculated = classification_metrics(labels, predictions)
    for key in ("correct", "errors", "accuracy", "macro_f1", "confusion_matrix"):
        assert recalculated[key] == metrics[key], key
    for index, row in enumerate(rows):
        assert row["sample_id"] == f"test:{index}" and int(row["test_index"]) == index
        assert row["true_label"] == LABEL_NAMES[labels[index]]
        assert row["predicted_label"] == LABEL_NAMES[predictions[index]]
        assert abs(float(row["confidence"]) - float(probabilities[index].max())) < 1e-6
    return metrics, checkpoint, rows, labels, predictions, probabilities


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    OUTPUT.mkdir(parents=True, exist_ok=True)
    data_dir = OUTPUT / "data"
    data_dir.mkdir(exist_ok=True)
    before, old, old_rows, labels, cnn, cnn_p = load_predictions(TEXTCNN)
    after, new, new_rows, new_labels, lstm, lstm_p = load_predictions(BILSTM)
    selection = read_json(PROJECT / "experiments/bilstm/regularization/data/selection.json")
    assert Path(selection["selected_checkpoint"]).resolve() == Path(after["checkpoint"]).resolve()
    assert not selection["test_used_for_selection"]
    assert new["config"]["model"]["name"] == "bilstm" and new["config"]["model"]["embedding_dropout"] == 0.2
    assert new["epoch"] == 8 and old["vocab"] == new["vocab"]
    assert old["config"]["seed"] == new["config"]["seed"] == 42
    assert old["config"]["data"] == new["config"]["data"]
    assert np.array_equal(labels, new_labels)
    raw = cached_split("test", new["config"]["data"]["cache_dir"])
    assert len(raw) == len(old_rows) == len(new_rows) == 7600
    groups = error_groups(labels, cnn, lstm)
    membership = {index: group for group, indexes in groups.items() for index in indexes}
    records = []
    for i, (a, b, source) in enumerate(zip(old_rows, new_rows, raw)):
        assert a["text"] == b["text"] == source["text"]
        assert a["processed_text"] == b["processed_text"] == source["text"]
        assert source["label"] == int(labels[i])
        tokens = tokenize(source["text"])
        unknown = sum(word not in new["vocab"] for word in tokens)
        records.append(dict(sample_id=f"test:{i}", test_index=i, true_label=LABEL_NAMES[labels[i]],
                            textcnn_prediction=LABEL_NAMES[cnn[i]], bilstm_prediction=LABEL_NAMES[lstm[i]],
                            group=membership[i], textcnn_confidence=float(cnn_p[i].max()),
                            bilstm_confidence=float(lstm_p[i].max()), token_count=len(tokens),
                            oov_count=unknown, oov_ratio=unknown/max(len(tokens), 1),
                            textcnn_margin=float(np.sort(cnn_p[i])[-1]-np.sort(cnn_p[i])[-2]),
                            bilstm_margin=float(np.sort(lstm_p[i])[-1]-np.sort(lstm_p[i])[-2]),
                            text=source["text"]))
    write_csv(data_dir / "paired_predictions.csv", records)
    for group in ("fixed", "new_errors", "both_wrong"):
        write_csv(data_dir / f"{group}.csv", [records[i] for i in groups[group]])
    errors = [row for row in records if row["bilstm_prediction"] != row["true_label"]]
    write_csv(data_dir / "bilstm_all_errors.csv", errors)
    appendix = ["# 最新最佳 BiLSTM：全部 581 条测试错误", "",
                "使用官方测试行号，保留全部原文和原始标签；这里只作模型诊断，不修改标注。", ""]
    for row in errors:
        appendix += [f"## {row['sample_id']}：{row['true_label']} → {row['bilstm_prediction']}", "",
                     f"TextCNN：{row['textcnn_prediction']}（置信度 {row['textcnn_confidence']:.4f}）；"
                     f"BiLSTM：{row['bilstm_prediction']}（置信度 {row['bilstm_confidence']:.4f}）；错误分组：{row['group']}。", "",
                     row["text"], ""]
    (data_dir / "bilstm_all_errors.md").write_text("\n".join(appendix), encoding="utf-8")
    lengths = np.array([row["token_count"] for row in records])
    oov = np.array([row["oov_count"] for row in records])
    class_rows = []
    for c, name in enumerate(LABEL_NAMES):
        indexes = np.flatnonzero(labels == c)
        class_rows.append(dict(label=name, samples=len(indexes), textcnn_errors=int(np.sum(cnn[indexes] != c)),
                               bilstm_errors=int(np.sum(lstm[indexes] != c)),
                               fixed=int(np.sum((cnn[indexes] != c) & (lstm[indexes] == c))),
                               new_errors=int(np.sum((cnn[indexes] == c) & (lstm[indexes] != c))),
                               both_wrong=int(np.sum((cnn[indexes] != c) & (lstm[indexes] != c))),
                               textcnn_precision=before["per_class"][c]["precision"], bilstm_precision=after["per_class"][c]["precision"],
                               textcnn_recall=before["per_class"][c]["recall"], bilstm_recall=after["per_class"][c]["recall"],
                               textcnn_f1=before["per_class"][c]["f1"], bilstm_f1=after["per_class"][c]["f1"]))
    write_csv(data_dir / "per_class.csv", class_rows)
    segments = []
    masks = [("不超过20词", lengths <= 20), ("21至40词", (lengths > 20) & (lengths <= 40)),
             ("超过40词", lengths > 40), ("没有未知词", oov == 0), ("至少一个未知词", oov > 0)]
    for name, mask in masks:
        n = int(mask.sum())
        a = int(np.sum((cnn != labels) & mask)); b = int(np.sum((lstm != labels) & mask))
        segments.append(dict(segment=name, samples=n, textcnn_errors=a, bilstm_errors=b,
                             textcnn_error_rate=a/n if n else None, bilstm_error_rate=b/n if n else None,
                             fixed=int(np.sum((cnn != labels) & (lstm == labels) & mask)),
                             new_errors=int(np.sum((cnn == labels) & (lstm != labels) & mask))))
    write_csv(data_dir / "feature_segments.csv", segments)
    confidence = []
    for name, pred, prob in [("TextCNN", cnn, cnn_p), ("BiLSTM", lstm, lstm_p)]:
        maxima = prob.max(1)
        for title, mask in [("置信度低于0.6", maxima < 0.6), ("置信度至少0.9", maxima >= 0.9)]:
            n, mistakes = int(mask.sum()), int(((pred != labels) & mask).sum())
            confidence.append(dict(model=name, segment=title, samples=n, errors=mistakes, error_rate=mistakes/n if n else None))
    write_csv(data_dir / "confidence_segments.csv", confidence)
    fixed, added = len(groups["fixed"]), len(groups["new_errors"])
    p_value = float(binomtest(fixed, fixed+added, p=0.5, alternative="two-sided").pvalue) if fixed+added else 1.0
    common = np.array(groups["both_wrong"])
    same_wrong = int(np.sum(cnn[common] == lstm[common]))
    summary = dict(textcnn=before, bilstm=after, selection=selection,
                   groups={name: len(values) for name, values in groups.items()},
                   per_class=class_rows, segments=segments, confidence=confidence,
                   common_errors_same_wrong_label=same_wrong, common_errors_different_wrong_label=len(common)-same_wrong,
                   accuracy_delta_percentage_points=(after["accuracy"]-before["accuracy"])*100,
                   relative_error_reduction=(before["errors"]-after["errors"])/before["errors"],
                   mcnemar_exact_two_sided=dict(fixed=fixed, new_errors=added, discordant=fixed+added, p_value=p_value),
                   truncation=dict(max_tokens=int(lengths.max()), over_max_length=int((lengths>256).sum())),
                   no_oov_bilstm_errors=int(np.sum((lstm != labels) & (oov == 0))))
    assert fixed-added == before["errors"]-after["errors"] == 26
    assert len(errors) == after["errors"] == 581
    assert sum(summary["groups"].values()) == 7600
    write_json(data_dir / "summary.json", summary)
    # 候选案例用于人工逐条阅读，候选排序不构成全体错误的原因标注。
    bank = {}
    for group in ("fixed", "new_errors", "both_wrong"):
        bank[group] = sorted([records[i] for i in groups[group]], key=lambda row: -row["bilstm_confidence"])[:18]
    bank["historical_cases"] = [records[i] for i in [139, 4359, 4047]]
    bank["world_business_fixed"] = [row for row in records if row["group"] == "fixed" and row["true_label"] == "World" and row["textcnn_prediction"] == "Business"][:10]
    bank["business_scitech_fixed"] = [row for row in records if row["group"] == "fixed" and {row["true_label"], row["textcnn_prediction"]} == {"Business", "Sci/Tech"}][:12]
    bank["business_scitech_new"] = [row for row in records if row["group"] == "new_errors" and {row["true_label"], row["bilstm_prediction"]} == {"Business", "Sci/Tech"}][:12]
    write_json(data_dir / "case_candidates.json", bank)
    print(json.dumps({key: value for key, value in summary.items() if key not in ("textcnn", "bilstm", "selection")}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
