"""BiLSTM 的变长序列、梯度和训练后恢复测试；不访问网络。"""

import importlib
import json
from functools import partial
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import torch
from torch.utils.data import DataLoader

from news_classifier import models
from news_classifier.config import load_config
from news_classifier.data import DataBundle, LABEL_NAMES, collate_batch


class BiLSTMTests(unittest.TestCase):
    def setUp(self):
        torch.manual_seed(42)
        torch.set_num_threads(1)
        self.model_config = dict(name="bilstm", embed_dim=8, hidden_size=6,
                                 num_layers=2, dropout=0.0, num_classes=4)

    def test_unsorted_batch_matches_individual_sequences_and_ignores_padding(self):
        self.assertTrue(hasattr(models, "build_model"), "缺少统一模型构建入口")
        model = models.build_model(12, self.model_config).eval()
        lengths = torch.tensor([2, 4, 1])
        ids = torch.tensor([[2, 3, 9, 8], [4, 5, 6, 7], [8, 9, 9, 9]])
        actual = model(ids, lengths)
        expected = torch.cat([model(row[:n].unsqueeze(0), n.reshape(1))
                              for row, n in zip(ids, lengths)])
        torch.testing.assert_close(actual, expected, atol=1e-6, rtol=1e-5)
        extra_padding = torch.cat([ids, torch.zeros(3, 5, dtype=torch.long)], dim=1)
        torch.testing.assert_close(model(extra_padding, lengths), actual)
        self.assertEqual(tuple(actual.shape), (3, 4))

    def test_backward_reaches_both_directions_and_preserves_pad_embedding(self):
        self.assertTrue(hasattr(models, "build_model"), "缺少统一模型构建入口")
        model = models.build_model(12, self.model_config)
        ids = torch.tensor([[2, 3, 0], [4, 5, 6]])
        loss = torch.nn.functional.cross_entropy(model(ids, torch.tensor([2, 3])), torch.tensor([0, 1]))
        loss.backward()
        for name in ("weight_ih_l0", "weight_ih_l0_reverse"):
            gradient = getattr(model.lstm, name).grad
            self.assertTrue(torch.isfinite(gradient).all())
            self.assertGreater(gradient.abs().sum().item(), 0)
        self.assertEqual(model.embedding.weight.grad[0].abs().sum().item(), 0)

    def test_invalid_lengths_are_rejected(self):
        self.assertTrue(hasattr(models, "build_model"), "缺少统一模型构建入口")
        model = models.build_model(12, self.model_config)
        for lengths in (torch.tensor([0, 1]), torch.tensor([4, 1]), torch.tensor([1])):
            with self.subTest(lengths=lengths), self.assertRaises(ValueError):
                model(torch.ones(2, 3, dtype=torch.long), lengths)

    def test_embedding_dropout_changes_training_only_and_preserves_old_weights(self):
        base_config = dict(self.model_config, num_layers=1)
        torch.manual_seed(42)
        baseline = models.build_model(12, base_config)
        torch.manual_seed(42)
        model = models.build_model(12, dict(base_config, embedding_dropout=0.5))
        self.assertTrue(hasattr(model, "embedding_dropout"), "缺少词嵌入 Dropout")
        model.load_state_dict(baseline.state_dict(), strict=True)
        ids = torch.tensor([[2, 3, 4, 5], [6, 7, 8, 9]])
        lengths = torch.tensor([4, 4])
        baseline.eval()
        model.eval()
        expected = baseline(ids, lengths)
        torch.testing.assert_close(model(ids, lengths), expected)
        model.train()
        self.assertFalse(torch.allclose(model(ids, lengths), expected))
        model.eval()
        torch.testing.assert_close(model(ids, lengths), expected)

    def test_old_textcnn_configs_still_build_and_unknown_model_is_rejected(self):
        self.assertTrue(hasattr(models, "build_model"), "缺少统一模型构建入口")
        config = load_config()["model"]
        config.pop("name")
        self.assertIsInstance(models.build_model(12, config), models.TextCNN)
        with self.assertRaisesRegex(ValueError, "model.name"):
            models.build_model(12, dict(self.model_config, name="unknown"))

    def test_bilstm_configuration_does_not_require_convolution_settings(self):
        with tempfile.TemporaryDirectory() as directory:
            config = load_config()
            config["model"] = self.model_config
            path = Path(directory) / "config.json"
            path.write_text(json.dumps(config), encoding="utf-8")
            self.assertEqual(load_config(path)["model"]["name"], "bilstm")
            for key, value in (("hidden_size", 0), ("num_layers", 0), ("name", "unknown")):
                with self.subTest(key=key), self.assertRaises(ValueError):
                    config["model"] = dict(self.model_config, **{key: value})
                    path.write_text(json.dumps(config), encoding="utf-8")
                    load_config(path)

    def test_training_checkpoint_can_be_predicted_evaluated_and_exported(self):
        self.assertTrue(hasattr(models, "build_model"), "缺少统一模型构建入口")
        entry = importlib.import_module("news_classifier.training.train")
        evaluation = importlib.import_module("news_classifier.evaluation.evaluate")
        analysis = importlib.import_module("news_classifier.evaluation.analysis")
        from news_classifier.evaluation.predict import predict
        vocab = {"<PAD>": 0, "<UNK>": 1, "world": 2, "sports": 3, "business": 4, "science": 5}
        rows = [([2 + label] * (label + 1), label) for label in range(4)] * 2
        loader = DataLoader(rows, batch_size=4, collate_fn=partial(collate_batch, min_length=1))
        class UnusedTestLoader:
            dataset = rows
            def __iter__(self):
                raise AssertionError("训练不应评估测试集")
        data = DataBundle(loader, loader, UnusedTestLoader(), vocab)
        test_rows = [{"text": "world", "label": 0}, {"text": "!!!", "label": 3}]
        with tempfile.TemporaryDirectory() as directory:
            config = load_config()
            config["model"] = self.model_config
            config["training"].update(epochs=2, device="cpu")
            config["output"].update(run_dir=directory, checkpoint_name="best_loss.pt")
            with patch.object(entry, "prepare_data", return_value=data):
                entry.train(config)
            path = Path(directory) / "best_loss.pt"
            checkpoint = torch.load(path, map_location="cpu", weights_only=True)
            self.assertEqual(checkpoint["config"]["model"]["name"], "bilstm")
            with patch.object(torch.cuda, "is_available", return_value=False):
                label, probabilities = predict(path, "!!!")
                self.assertIn(label, LABEL_NAMES)
                self.assertAlmostEqual(sum(probabilities), 1, places=6)
                with patch.object(evaluation, "load_dataset", return_value=test_rows):
                    metrics = evaluation.evaluate_checkpoint(path)
                self.assertEqual(metrics["num_samples"], 2)
                from datasets import Dataset
                with patch.object(analysis, "cached_split", return_value=Dataset.from_list(test_rows)):
                    exported, _, _ = analysis.infer_checkpoint(path, Path(directory) / "export")
                self.assertEqual(exported["num_samples"], 2)
            before = path.read_bytes()
            with patch.object(entry, "prepare_data", side_effect=AssertionError("不应重载数据")):
                with self.assertRaises(FileExistsError):
                    entry.train(config)
            self.assertEqual(path.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
