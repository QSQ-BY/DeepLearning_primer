"""验证早停阈值、耐心重置、最佳权重保存及旧配置兼容。"""

import importlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import torch

from news_classifier.config import load_config
from news_classifier.data import DataBundle
from news_classifier.engine import EpochMetrics

entry = importlib.import_module("news_classifier.training.train")


class EarlyStoppingTests(unittest.TestCase):
    def test_small_changes_count_as_no_improvement_and_real_improvement_resets(self):
        self.assertTrue(hasattr(entry, "EarlyStopping"), "缺少早停状态对象")
        stop = entry.EarlyStopping(patience=3, min_delta=0.001)
        decisions = [stop.step(value) for value in (0.5, 0.4, 0.3995, 0.41, 0.38, 0.3795, 0.39, 0.40)]
        self.assertEqual(decisions, [False] * 7 + [True])
        self.assertEqual(stop.best, 0.38)
        self.assertEqual(stop.bad_epochs, 3)

    def test_invalid_parameters_and_nonfinite_losses_are_rejected(self):
        self.assertTrue(hasattr(entry, "EarlyStopping"), "缺少早停状态对象")
        for settings in ({"patience": 0}, {"patience": True}, {"min_delta": -0.01},
                         {"min_delta": float("nan")}, {"min_delta": float("inf")}):
            with self.subTest(settings=settings), self.assertRaises(ValueError):
                entry.EarlyStopping(**settings)
        for value in (float("nan"), float("inf")):
            with self.subTest(loss=value), self.assertRaises(ValueError):
                entry.EarlyStopping().step(value)

    def test_training_stops_after_patience_and_keeps_independent_best_checkpoints(self):
        with tempfile.TemporaryDirectory() as directory:
            config = load_config()
            config["model"].update(embed_dim=4, num_filters=2, kernel_sizes=[2])
            config["training"].update(epochs=10, device="cpu", early_stopping={
                "enabled": True, "monitor": "val_loss", "patience": 3, "min_delta": 0.001,
            })
            config["output"].update(run_dir=directory, checkpoint_name="best_loss.pt")
            class Loader:
                dataset = [0, 1]
            data = DataBundle(Loader(), Loader(), Loader(), {"<PAD>": 0, "<UNK>": 1, "word": 2})
            validation = [EpochMetrics(loss, acc, 2) for loss, acc in
                          [(0.5, 0.70), (0.4, 0.75), (0.3995, 0.80), (0.41, 0.77), (0.42, 0.76)]]
            with patch.object(entry, "prepare_data", return_value=data), patch.object(
                entry, "train_one_epoch", return_value=EpochMetrics(0.3, 0.85, 2)
            ) as training, patch.object(entry, "evaluate", side_effect=validation + [validation[-1]] * 5):
                result = entry.train(config)
            self.assertEqual(training.call_count, 5)
            self.assertEqual(result["completed_epochs"], 5)
            self.assertTrue(result["stopped_early"])
            self.assertEqual(torch.load(Path(directory) / "best_loss.pt", weights_only=True)["epoch"], 3)
            self.assertEqual(torch.load(Path(directory) / "best_accuracy.pt", weights_only=True)["epoch"], 3)
            saved = json.loads((Path(directory) / "training_summary.json").read_text(encoding="utf-8"))
            self.assertEqual(saved, result)
            self.assertEqual(saved["early_stopping"]["reference_loss"], 0.4)

    def test_invalid_early_stopping_fails_before_loading_data(self):
        for settings in ({"enabled": True, "patience": 0}, {"enabled": "yes"},
                         {"enabled": True, "monitor": "accuracy"}):
            config = load_config()
            config["training"]["early_stopping"] = settings
            with self.subTest(settings=settings), tempfile.TemporaryDirectory() as directory, patch.object(entry, "prepare_data", side_effect=AssertionError("不应加载数据")):
                config["output"]["run_dir"] = directory
                with self.assertRaises(ValueError):
                    entry.train(config)


if __name__ == "__main__":
    unittest.main()
