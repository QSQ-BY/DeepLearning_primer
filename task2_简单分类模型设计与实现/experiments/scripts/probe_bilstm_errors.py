"""对预先选定的三条案例做 UNK 遮挡；原始输入先与全量预测核对。"""

import csv
import json
from pathlib import Path
import sys

import numpy as np
import torch

PROJECT = Path(__file__).resolve().parents[2]
ROOT = PROJECT.parent
sys.path.insert(0, str(PROJECT))
from news_classifier.models import build_model
from news_classifier.config import min_sequence_length
from news_classifier.data import LABEL_NAMES, tokenize, collate_batch


def main():
    output = PROJECT / "experiments/bilstm/error_analysis/data"
    with (output / "paired_predictions.csv").open(encoding="utf-8", newline="") as stream:
        rows = {row["sample_id"]: row for row in csv.DictReader(stream)}
    specs = {
        "test:139": [("mask_bank", {"bank"}), ("mask_west", {"west"}), ("mask_political_cues", {"sharon", "israel", "settlements"})],
        "test:4825": [("mask_tech", {"tech"}), ("mask_sports_cues", {"turnovers", "plays", "randall", "hokies"})],
        "test:172": [("mask_computer", {"computer"}), ("mask_financial_cues", {"profit", "retailer", "quarter", "demand"})],
    }
    torch.set_num_threads(4)
    results = []
    for name, path in [("TextCNN", ROOT / ".build/task2/runs/textcnn_k237_plateau20/best_accuracy.pt"),
                       ("BiLSTM", ROOT / ".build/task2/runs/bilstm_es_dropout02_20261103/best_accuracy.pt")]:
        saved = torch.load(path, map_location="cpu", weights_only=True)
        model = build_model(len(saved["vocab"]), saved["config"]["model"]).eval()
        model.load_state_dict(saved["model_state_dict"])
        source = (PROJECT / "experiments/textcnn/error_analysis/data/kernel_comparison/k237") if name == "TextCNN" else path.parent / "final_evaluation"
        with np.load(source / "predictions.npz") as values:
            reference = values["probabilities"].copy()
        for sample_id, probes in specs.items():
            tokens = tokenize(rows[sample_id]["text"])[:saved["config"]["data"]["max_length"]]
            ids = [saved["vocab"].get(token, 1) for token in tokens]
            variants = [("original", ids, [])]
            for label, words in probes:
                masked = ids.copy()
                changed = []
                for i, token in enumerate(tokens):
                    if token in words:
                        changed.append(dict(position=i, token=token))
                        masked[i] = 1
                assert changed
                variants.append((label, masked, changed))
            batch, lengths, _ = collate_batch([(values, 0) for _, values, _ in variants], min_length=min_sequence_length(saved["config"]["model"]))
            with torch.inference_mode():
                probabilities = model(batch, lengths).softmax(1).numpy()
            index = int(sample_id.split(":")[1])
            np.testing.assert_allclose(probabilities[0], reference[index], atol=5e-4, rtol=1e-3)
            expected = rows[sample_id]["textcnn_prediction" if name == "TextCNN" else "bilstm_prediction"]
            assert LABEL_NAMES[int(probabilities[0].argmax())] == expected
            for (label, _, changed), probability in zip(variants, probabilities):
                results.append(dict(model=name, sample_id=sample_id, variant=label, masked_positions=changed,
                                    prediction=LABEL_NAMES[int(probability.argmax())],
                                    probabilities={label: float(value) for label, value in zip(LABEL_NAMES, probability)}))
    (output / "masking_probes.json").write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Verified original predictions; saved {len(results)} original/masked results.")


if __name__ == "__main__":
    main()
