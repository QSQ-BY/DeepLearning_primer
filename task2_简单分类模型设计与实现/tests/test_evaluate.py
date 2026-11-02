"""使用本地权重和微型测试集检查独立评估，不访问网络。"""

import hashlib
import importlib
import json
import tempfile
import unittest
from functools import partial
from pathlib import Path
from unittest.mock import patch

import torch
from torch.utils.data import DataLoader

from news_classifier.config import load_config
from news_classifier.data import LABEL_NAMES, collate_batch
from news_classifier.engine import evaluate
from news_classifier.model import TextCNN


entry = importlib.import_module("news_classifier.evaluate")


class EvaluateCheckpointTests(unittest.TestCase):
    def test_restores_saved_vocabulary_and_writes_metrics_beside_checkpoint(self):
        torch.manual_seed(42)
        with tempfile.TemporaryDirectory() as directory:
            checkpoint_path = Path(directory) / "moved" / "best.pt"
            checkpoint_path.parent.mkdir()
            config = load_config()
            config["training"].update(device="cuda", batch_size=2)
            config["model"].update(
                embed_dim=8, num_filters=4, kernel_sizes=[2, 3], dropout=0.5
            )
            config["output"]["run_dir"] = str(Path(directory) / "old-location")

            # 编号特意与字母顺序、频率顺序不同，检查是否复用保存的词表。
            vocab = {
                "<PAD>": 0, "<UNK>": 1, "world": 2,
                "science": 3, "business": 4, "sports": 5,
            }
            model = TextCNN(len(vocab), config["model"])
            torch.save({
                "model_state_dict": model.state_dict(),
                "config": config,
                "vocab": vocab,
                "label_names": LABEL_NAMES,
                "epoch": 1,
            }, checkpoint_path)
            original_hash = hashlib.sha256(checkpoint_path.read_bytes()).hexdigest()

            rows = [
                {"text": "SPORTS world!", "label": 1},
                {"text": "Science", "label": 3},
                {"text": "business unknown", "label": 2},
                {"text": "!!!", "label": 0},
                {"text": "world sports business science", "label": 0},
            ]
            expected_samples = [
                ([5, 2], 1), ([3], 3), ([4, 1], 2), ([1], 0), ([2, 5, 4, 3], 0)
            ]
            expected_loader = DataLoader(
                expected_samples, batch_size=2,
                collate_fn=partial(collate_batch, min_length=3),
            )
            expected = evaluate(model, expected_loader, torch.device("cpu"))

            def load_test_only(name, *, cache_dir, split):
                self.assertEqual(name, config["data"]["dataset_name"])
                self.assertEqual(cache_dir, config["data"]["cache_dir"])
                self.assertEqual(split, "test")
                return rows

            # 仅替换外部数据读取和硬件检测，模型、编码和损失计算均使用真实实现。
            with patch.object(entry, "load_dataset", side_effect=load_test_only), patch(
                "news_classifier.data.build_vocab",
                side_effect=AssertionError("Evaluation must not rebuild vocabulary"),
            ), patch.object(torch.cuda, "is_available", return_value=False):
                result = entry.evaluate_checkpoint(checkpoint_path)

            self.assertAlmostEqual(result["loss"], expected.loss, places=6)
            self.assertEqual(result["accuracy"], expected.accuracy)
            self.assertEqual(result["num_samples"], 5)
            metrics_path = checkpoint_path.parent / "test_metrics.json"
            self.assertEqual(json.loads(metrics_path.read_text(encoding="utf-8")), result)
            self.assertFalse(Path(config["output"]["run_dir"]).exists())
            self.assertEqual(
                hashlib.sha256(checkpoint_path.read_bytes()).hexdigest(), original_hash
            )


if __name__ == "__main__":
    unittest.main()
