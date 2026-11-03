"""验证学习率调度和两种检查点选择规则，不下载数据。"""

import csv
import importlib
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import torch

from news_classifier.config import load_config
from news_classifier.data import DataBundle
from news_classifier.engine import EpochMetrics

entry = importlib.import_module("news_classifier.training.train")


class TrainExperimentTests(unittest.TestCase):
    def test_learning_rate_timing_and_independent_checkpoint_selection(self):
        for scheduler_name in ("none", "reduce_on_plateau"):
            with self.subTest(scheduler=scheduler_name), tempfile.TemporaryDirectory() as directory:
                config = load_config()
                config["model"].update(embed_dim=8, num_filters=4, kernel_sizes=[2, 3])
                config["training"].update(
                    epochs=5, device="cpu", learning_rate=0.001,
                    scheduler={"name": scheduler_name, "factor": 0.5, "patience": 1, "min_lr": 1e-5},
                )
                config["output"].update(
                    run_dir=directory, checkpoint_name="best_loss.pt",
                    accuracy_checkpoint_name="best_accuracy.pt",
                )
                vocab = {"<PAD>": 0, "<UNK>": 1, "word": 2}

                class Loader:
                    dataset = [0, 1]

                data = DataBundle(Loader(), Loader(), Loader(), vocab)
                used_rates = []

                def train_epoch(model, loader, optimizer, device):
                    used_rates.append(optimizer.param_groups[0]["lr"])
                    # 保存不同轮次的真实参数，检查文件是否保留了选中轮次的快照。
                    with torch.no_grad():
                        model.classifier.bias.fill_(len(used_rates))
                    return EpochMetrics(loss=0.4, accuracy=0.9, num_samples=2)

                validation = [
                    EpochMetrics(loss=0.60, accuracy=0.70, num_samples=2),
                    EpochMetrics(loss=0.50, accuracy=0.80, num_samples=2),
                    EpochMetrics(loss=0.55, accuracy=0.81, num_samples=2),
                    EpochMetrics(loss=0.56, accuracy=0.81, num_samples=2),
                    EpochMetrics(loss=0.52, accuracy=0.81, num_samples=2),
                ]
                with patch.object(entry, "prepare_data", return_value=data), patch.object(
                    entry, "train_one_epoch", side_effect=train_epoch
                ), patch.object(entry, "evaluate", side_effect=validation), patch.object(
                    torch.cuda, "is_available", return_value=False
                ):
                    entry.train(config)

                loss_checkpoint = torch.load(Path(directory) / "best_loss.pt", weights_only=True)
                self.assertEqual(loss_checkpoint["epoch"], 2)
                self.assertTrue(torch.all(loss_checkpoint["model_state_dict"]["classifier.bias"] == 2))
                accuracy_path = Path(directory) / "best_accuracy.pt"
                self.assertTrue(accuracy_path.exists(), "必须单独保存最高准确率模型")
                accuracy_checkpoint = torch.load(accuracy_path, weights_only=True)
                self.assertEqual(accuracy_checkpoint["epoch"], 5)
                self.assertEqual(accuracy_checkpoint["val_accuracy"], 0.81)
                self.assertEqual(accuracy_checkpoint["val_loss"], 0.52)
                self.assertTrue(torch.all(accuracy_checkpoint["model_state_dict"]["classifier.bias"] == 5))
                self.assertEqual(loss_checkpoint["selection_metric"], "val_loss")
                self.assertEqual(accuracy_checkpoint["selection_metric"], "val_accuracy")
                expected_rates = [0.001] * 5 if scheduler_name == "none" else [0.001] * 4 + [0.0005]
                self.assertEqual(used_rates, expected_rates)
                with (Path(directory) / "metrics.csv").open(encoding="utf-8", newline="") as file:
                    rows = list(csv.DictReader(file))
                self.assertEqual([float(row["learning_rate"]) for row in rows], expected_rates)

    def test_unknown_scheduler_fails_before_loading_data(self):
        config = load_config()
        config["training"]["scheduler"] = {"name": "unknown_scheduler"}
        with patch.object(entry, "prepare_data", side_effect=AssertionError("不应加载数据")):
            with self.assertRaisesRegex(ValueError, "scheduler"):
                entry.train(config)


if __name__ == "__main__":
    unittest.main()
