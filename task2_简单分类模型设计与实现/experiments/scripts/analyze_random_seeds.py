"""核验六次训练、统一评估固定权重，并导出配对与跨种子统计；不挑选种子。"""

import argparse
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
OUT = PROJECT / "experiments/random_seeds"
RUNS = ROOT / ".build/task2/runs/random_seeds_20261103"
SEEDS = (17, 2024, 3407)
sys.path.insert(0, str(PROJECT))
from news_classifier.evaluation.analysis import classification_metrics, error_groups, infer_checkpoint, write_csv, write_json


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_metrics(path):
    with path.open(encoding="utf-8", newline="") as source:
        return [{key: float(value) for key, value in row.items()} for row in csv.DictReader(source)]


def audit_training():
    protocol = read_json(OUT / "protocol.json")
    assert protocol["training_seeds"] == list(SEEDS) and protocol["split_seed"] == 42
    audits, initial_hashes = [], {name: [] for name in ("textcnn", "bilstm")}
    records = {}
    for seed in SEEDS:
        records[seed] = {}
        for name in ("textcnn", "bilstm"):
            folder = RUNS / f"seed_{seed}" / name
            status = read_json(folder / "execution.json")
            assert status["status"] == "completed", (seed, name, status["status"])
            assert status["seed"] == seed and status["model"] == name
            for path, expected in status["source_sha256"].items():
                assert sha(ROOT / path) == expected, path
            checkpoint = torch.load(folder / "best_accuracy.pt", map_location="cpu", weights_only=True)
            history = read_metrics(folder / "metrics.csv")
            assert len(history) == status["summary"]["completed_epochs"]
            selected = min(history, key=lambda row: (-row["val_accuracy"], row["val_loss"]))
            assert checkpoint["epoch"] == int(selected["epoch"]) == status["selected_epoch"]
            assert checkpoint["val_accuracy"] == selected["val_accuracy"]
            assert checkpoint["val_loss"] == selected["val_loss"]
            assert checkpoint["config"]["seed"] == seed
            assert checkpoint["config"]["data"]["split_seed"] == 42
            assert sha(folder / "best_accuracy.pt") == status["checkpoint_sha256"]
            if name == "textcnn":
                assert len(history) == 20 and status["summary"]["early_stopping"] is None
            else:
                assert checkpoint["config"]["model"]["embedding_dropout"] == 0.2
                # 从逐轮验证损失独立回放早停规则。
                best, bad, stop = float("inf"), 0, None
                for row in history:
                    if row["val_loss"] < best - 0.001:
                        best, bad = row["val_loss"], 0
                    else:
                        bad += 1
                    if bad >= 3:
                        stop = int(row["epoch"])
                        break
                assert len(history) == (stop if stop is not None else 20)
            base_path = Path(protocol["sources"][name]["config"])
            assert sha(base_path) == protocol["sources"][name]["sha256"]
            base = read_json(base_path)
            actual = checkpoint["config"]
            assert actual["model"] == base["model"] and actual["training"] == base["training"]
            for key, value in base["data"].items():
                assert actual["data"][key] == (str((PROJECT / value).resolve()) if key == "cache_dir" else value)
            audit = status["data_audit"]
            for split in ("train", "val", "test"):
                assert audit[f"{split}_sampler_seed"] == seed
            audits.append({key: value for key, value in audit.items() if not key.endswith("sampler_seed")})
            initial_hashes[name].append(status["summary"]["initial_parameter_sha256"])
            records[seed][name] = dict(status=status, history=history)
    assert all(audit == audits[0] for audit in audits)
    assert all(len(set(values)) == 3 for values in initial_hashes.values())
    write_json(OUT / "training_verification.json", dict(status="passed", runs=6, fixed_data_audit=audits[0], initial_hashes=initial_hashes))
    return records


def load_evaluation(path, expected_checkpoint):
    metrics = read_json(path / "metrics.json")
    assert Path(metrics["checkpoint"]).resolve() == expected_checkpoint.resolve()
    assert sha(expected_checkpoint) == metrics["checkpoint_sha256"]
    with np.load(path / "predictions.npz") as source:
        labels, predictions = source["labels"].copy(), source["predictions"].copy()
        probabilities, logits = source["probabilities"].copy(), source["logits"].copy()
    assert labels.shape == predictions.shape == (7600,)
    assert probabilities.shape == logits.shape == (7600, 4)
    assert np.isfinite(probabilities).all() and np.isfinite(logits).all()
    np.testing.assert_allclose(probabilities.sum(1), 1, atol=1e-6)
    assert np.array_equal(logits.argmax(1), predictions)
    calculated = classification_metrics(labels, predictions)
    for key, value in calculated.items():
        assert value == metrics[key], key
    with (path / "all_predictions.csv").open(encoding="utf-8", newline="") as source:
        rows = list(csv.DictReader(source))
    assert len(rows) == 7600
    for i, row in enumerate(rows):
        assert row["sample_id"] == f"test:{i}"
        assert row["predicted_label"] == metrics["per_class"][int(predictions[i])]["label"]
        assert abs(float(row["confidence"]) - float(probabilities[i].max())) < 1e-6
    return metrics, labels, predictions, rows


def summarize_pair(seed, data, training):
    cnn, lstm = data["textcnn"], data["bilstm"]
    assert np.array_equal(cnn[1], lstm[1])
    groups = error_groups(cnn[1], cnn[2], lstm[2])
    pair_rows = []
    membership = {i: group for group, indexes in groups.items() for i in indexes}
    for i, (a, b) in enumerate(zip(cnn[3], lstm[3])):
        assert a["sample_id"] == b["sample_id"]
        assert a["text"] == b["text"] and a["true_label"] == b["true_label"]
        pair_rows.append(dict(sample_id=a["sample_id"], true_label=a["true_label"],
                              textcnn_prediction=a["predicted_label"], bilstm_prediction=b["predicted_label"],
                              textcnn_confidence=float(a["confidence"]), bilstm_confidence=float(b["confidence"]),
                              group=membership[i], text=a["text"]))
    target = OUT / f"seed_{seed}/data"
    target.mkdir(parents=True, exist_ok=True)
    write_csv(target / "paired_predictions.csv", pair_rows)
    for group in ("fixed", "new_errors", "both_wrong"):
        write_csv(target / f"{group}.csv", [pair_rows[i] for i in groups[group]])
    fixed, added = len(groups["fixed"]), len(groups["new_errors"])
    assert fixed - added == lstm[0]["correct"] - cnn[0]["correct"]
    summary = dict(seed=seed, metrics={name: values[0] for name, values in data.items()},
                   training={name: {key: record["status"][key] for key in
                                    ("selected_epoch", "elapsed_seconds", "val_accuracy", "val_loss", "summary", "data_audit")}
                             for name, record in training.items()},
                   groups={key: len(value) for key, value in groups.items()},
                   accuracy_delta_pp=(lstm[0]["accuracy"] - cnn[0]["accuracy"]) * 100,
                   macro_f1_delta_pp=(lstm[0]["macro_f1"] - cnn[0]["macro_f1"]) * 100,
                   mcnemar_exact_p=float(binomtest(fixed, fixed + added, 0.5).pvalue) if fixed + added else 1.0)
    write_json(target / "summary.json", summary)
    return summary


def stats(values):
    a = np.array(values, dtype=float)
    return dict(n=len(a), mean=float(a.mean()), sample_std=float(a.std(ddof=1)),
                min=float(a.min()), max=float(a.max()), values=a.tolist())


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evaluate", action="store_true", help="仅在尚无评估目录时执行测试推理；已存在则核验并复用")
    args = parser.parse_args()
    torch.set_num_threads(4)
    records = audit_training()  # 六次训练均完成且一致性通过后，才允许读取测试预测。
    summaries, predictions, labels_reference, text_reference = [], {name: [] for name in ("textcnn", "bilstm")}, None, None
    for seed in SEEDS:
        data = {}
        for name in ("textcnn", "bilstm"):
            target = OUT / f"seed_{seed}/data/{name}"
            checkpoint = RUNS / f"seed_{seed}" / name / "best_accuracy.pt"
            if not target.exists():
                if not args.evaluate:
                    raise FileNotFoundError(f"尚未评估：{target}，请显式提供 --evaluate")
                infer_checkpoint(checkpoint, target)
            data[name] = load_evaluation(target, checkpoint)
            if labels_reference is None:
                labels_reference, text_reference = data[name][1], [r["text"] for r in data[name][3]]
            else:
                assert np.array_equal(data[name][1], labels_reference)
                assert [r["text"] for r in data[name][3]] == text_reference
            predictions[name].append(data[name][2])
        summaries.append(summarize_pair(seed, data, records[seed]))
    historical_path = PROJECT / "experiments/bilstm/error_analysis/data/summary.json"
    historical = read_json(historical_path)
    for name in ("textcnn", "bilstm"):
        assert sha(Path(historical[name]["checkpoint"])) == historical[name]["checkpoint_sha256"]
    aggregates = {}
    for name in ("textcnn", "bilstm"):
        aggregates[name] = {key: stats([row["metrics"][name][key] for row in summaries])
                            for key in ("accuracy", "macro_f1", "loss", "errors")}
    delta = stats([row["accuracy_delta_pp"] for row in summaries])
    aggregate4 = {name: stats([row["metrics"][name]["accuracy"] for row in summaries] + [historical[name]["accuracy"]]) for name in ("textcnn", "bilstm")}
    frequency_rows = []
    wrong = {name: np.sum(np.stack(values) != labels_reference, axis=0) for name, values in predictions.items()}
    frequency = {name: {str(k): int(np.sum(values == k)) for k in range(4)} for name, values in wrong.items()}
    for i, label in enumerate(labels_reference):
        frequency_rows.append(dict(sample_id=f"test:{i}", true_label=summaries[0]["metrics"]["textcnn"]["per_class"][int(label)]["label"],
                                   textcnn_error_seeds=int(wrong["textcnn"][i]), bilstm_error_seeds=int(wrong["bilstm"][i]), text=text_reference[i]))
    (OUT / "data").mkdir(exist_ok=True)
    write_csv(OUT / "data/error_frequency.csv", frequency_rows)
    table = []
    for summary in summaries:
        for name, metric in summary["metrics"].items():
            run = summary["training"][name]
            table.append(dict(seed=summary["seed"], model=name, epochs=run["summary"]["completed_epochs"],
                              selected_epoch=run["selected_epoch"], val_accuracy=metric["val_accuracy"],
                              test_accuracy=metric["accuracy"], macro_f1=metric["macro_f1"],
                              errors=metric["errors"], test_loss=metric["loss"], elapsed_seconds=run["elapsed_seconds"]))
    write_csv(OUT / "data/results.csv", table)
    combined = dict(new_seeds=list(SEEDS), primary=aggregates, accuracy_delta_pp=delta,
                    bilstm_wins=sum(row["accuracy_delta_pp"] > 0 for row in summaries),
                    ties=sum(row["accuracy_delta_pp"] == 0 for row in summaries),
                    historical_seed42={name: historical[name] for name in ("textcnn", "bilstm")},
                    including_historical_seed42_accuracy=aggregate4,
                    error_frequency_new_seeds=frequency,
                    both_models_wrong_all_three=int(np.sum((wrong["textcnn"] == 3) & (wrong["bilstm"] == 3))),
                    runs=summaries)
    write_json(OUT / "data/summary.json", combined)
    print(json.dumps({k: v for k, v in combined.items() if k not in ("runs", "historical_seed42")}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
