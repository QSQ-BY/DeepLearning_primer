"""独立从逐样本 CSV 重算指标、错误集合与跨种子统计，并核验报告资产。"""

import collections
import csv
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import re
import statistics
import xml.etree.ElementTree as ET

from PIL import Image

PROJECT = Path(__file__).resolve().parents[2]
OUT = PROJECT / "experiments/random_seeds"
NAMES = ["World", "Sports", "Business", "Sci/Tech"]


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def read_rows(path):
    with path.open(encoding="utf-8", newline="") as source:
        return list(csv.DictReader(source))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def close(a, b):
    assert math.isclose(a, b, abs_tol=1e-12), (a, b)


def main():
    summary = read_json(OUT / "data/summary.json")
    assert summary["new_seeds"] == [17, 2024, 3407]
    reconstructed = {name: collections.defaultdict(list) for name in ("textcnn", "bilstm")}
    errors_by_model = {name: [] for name in reconstructed}
    deltas, rows_checked = [], 0
    for run in summary["runs"]:
        folder = OUT / f"seed_{run['seed']}"
        paired = read_rows(folder / "data/paired_predictions.csv")
        assert [r["sample_id"] for r in paired] == [f"test:{i}" for i in range(7600)]
        groups = collections.Counter()
        for row in paired:
            a = row["textcnn_prediction"] == row["true_label"]
            b = row["bilstm_prediction"] == row["true_label"]
            group = ("both_correct" if a else "fixed") if b else ("new_errors" if a else "both_wrong")
            assert group == row["group"]
            groups[group] += 1
        assert dict(groups) == run["groups"]
        for group in ("fixed", "new_errors", "both_wrong"):
            assert read_rows(folder / f"data/{group}.csv") == [r for r in paired if r["group"] == group]
        for name in reconstructed:
            rows = read_rows(folder / f"data/{name}/all_predictions.csv")
            assert len(rows) == 7600
            rows_checked += len(rows)
            matrix = [[0] * 4 for _ in range(4)]
            for r, p in zip(rows, paired):
                assert r["sample_id"] == p["sample_id"] and r["text"] == p["text"]
                assert r["true_label"] == p["true_label"]
                assert r["predicted_label"] == p[f"{name}_prediction"]
                matrix[NAMES.index(r["true_label"])][NAMES.index(r["predicted_label"]) ] += 1
            errors = {r["sample_id"] for r in rows if r["predicted_label"] != r["true_label"]}
            errors_by_model[name].append(errors)
            metric = run["metrics"][name]
            assert matrix == metric["confusion_matrix"]
            assert len(errors) == metric["errors"]
            assert all(sum(r) == 1900 for r in matrix)
            accuracy = 1 - len(errors) / 7600
            f1 = statistics.mean(2 * matrix[i][i] / (sum(matrix[i]) + sum(r[i] for r in matrix)) for i in range(4))
            close(accuracy, metric["accuracy"])
            close(f1, metric["macro_f1"])
            for key, value in (("accuracy", accuracy), ("macro_f1", f1), ("errors", len(errors))):
                reconstructed[name][key].append(value)
            checkpoint = Path(metric["checkpoint"])
            assert sha(checkpoint) == metric["checkpoint_sha256"]
        delta = (run["metrics"]["bilstm"]["accuracy"] - run["metrics"]["textcnn"]["accuracy"]) * 100
        close(delta, run["accuracy_delta_pp"])
        deltas.append(delta)
        fixed, added = groups["fixed"], groups["new_errors"]
        p = 2 * sum(math.comb(fixed + added, i) for i in range(min(fixed, added) + 1)) / 2 ** (fixed + added)
        close(min(p, 1), run["mcnemar_exact_p"])
    for name, metrics in reconstructed.items():
        for key, values in metrics.items():
            stored = summary["primary"][name][key]
            close(statistics.mean(values), stored["mean"])
            close(statistics.stdev(values), stored["sample_std"])
        combined = metrics["accuracy"] + [summary["historical_seed42"][name]["accuracy"]]
        close(statistics.mean(combined), summary["including_historical_seed42_accuracy"][name]["mean"])
        close(statistics.stdev(combined), summary["including_historical_seed42_accuracy"][name]["sample_std"])
        frequencies = collections.Counter(sum(f"test:{i}" in e for e in errors_by_model[name]) for i in range(7600))
        assert {str(k): frequencies[k] for k in range(4)} == summary["error_frequency_new_seeds"][name]
    close(statistics.mean(deltas), summary["accuracy_delta_pp"]["mean"])
    close(statistics.stdev(deltas), summary["accuracy_delta_pp"]["sample_std"])
    assert sum(d > 0 for d in deltas) == summary["bilstm_wins"]
    recurring = set.intersection(*(errors_by_model["textcnn"] + errors_by_model["bilstm"]))
    assert len(recurring) == summary["both_models_wrong_all_three"]

    report_hashes, links, text_count = {}, 0, 0
    for path in OUT.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix in (".md", ".json", ".csv", ".svg"):
            raw = path.read_bytes()
            assert not raw.startswith(b"\xef\xbb\xbf"), path
            assert "\ufffd" not in raw.decode("utf-8"), path
            text_count += 1
        if path.suffix == ".md":
            text = path.read_text(encoding="utf-8")
            assert "训练进行中" not in text
            report_hashes[str(path.relative_to(OUT))] = sha(path)
            for target in re.findall(r'!?\[[^\]]*\]\(([^\s)]+)\)', text):
                if target.startswith(("http://", "https://", "#")):
                    continue
                resolved = (path.parent / target.split("#", 1)[0]).resolve()
                assert resolved.exists() or resolved == OUT / "verification.json", (path, target)
                links += 1
    images = {}
    for path in OUT.rglob("*.png"):
        with Image.open(path) as img:
            img.verify()
        with Image.open(path) as img:
            assert min(img.size) >= 750
            images[str(path.relative_to(OUT))] = list(img.size)
        assert ET.parse(path.with_suffix(".svg")).getroot().tag.endswith("svg")
    assert len(images) == 10
    assert len(list(OUT.rglob("2026-11-03*.md"))) == 4
    assert not list(OUT.rglob("*.pdf"))
    for script in ("run_random_seeds.py", "analyze_random_seeds.py", "report_random_seeds.py", "verify_random_seeds.py"):
        path = PROJECT / "experiments/scripts" / script
        compile(path.read_text(encoding="utf-8"), str(path), "exec")
    record = dict(status="passed", verified_at_utc=datetime.now(timezone.utc).isoformat(),
                  source_prediction_rows=rows_checked, paired_rows=22800,
                  report_files=4, image_pairs=10, checked_local_links=links, checked_text_files=text_count,
                  checks=["CSV confusion matrices, error groups, accuracy and macro-F1 independently reconstructed",
                          "statistics.mean and statistics.stdev agree with aggregate", "math.comb exact paired tests",
                          "cross-seed error frequencies", "checkpoint SHA256", "Markdown local links",
                          "UTF8 without BOM", "PNG integrity and SVG XML", "script syntax", "no PDF"],
                  report_sha256=report_hashes, images=images,
                  visual_review="All ten PNGs inspected: labels, legends, scales, annotations and footnotes readable.")
    (OUT / "verification.json").write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in record.items() if k not in ("images", "report_sha256")}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
