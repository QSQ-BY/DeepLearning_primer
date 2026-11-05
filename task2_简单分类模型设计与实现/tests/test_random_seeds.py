"""固定数据划分时，训练随机种子只改变采样随机性；不访问网络。"""

import copy
import unittest
from unittest.mock import patch

from datasets import ClassLabel, Dataset, DatasetDict

from news_classifier.data import prepare_data


class RandomSeedDataTests(unittest.TestCase):
    def test_fixed_split_with_distinct_training_seeds_and_legacy_fallback(self):
        train = Dataset.from_dict({
            "text": [f"news sample {i} category {i % 4}" for i in range(80)],
            "label": [i % 4 for i in range(80)],
        }).cast_column("label", ClassLabel(num_classes=4))
        dataset = DatasetDict(train=train, test=train.select(range(8)))
        config = dict(seed=17,
                      data=dict(dataset_name="unused", cache_dir="unused", split_seed=42,
                                val_ratio=0.2, min_freq=1, max_vocab_size=200, max_length=32),
                      model=dict(name="bilstm"), training=dict(batch_size=8, num_workers=0))
        other = copy.deepcopy(config)
        other["seed"] = 2024
        legacy = copy.deepcopy(config)
        del legacy["data"]["split_seed"]
        explicit_legacy = copy.deepcopy(legacy)
        explicit_legacy["data"]["split_seed"] = 17
        with patch("datasets.load_dataset", return_value=dataset):
            a, b, old, explicit = [prepare_data(c) for c in (config, other, legacy, explicit_legacy)]
        self.assertEqual(a.vocab, b.vocab)
        self.assertEqual(a.train_loader.dataset, b.train_loader.dataset)
        self.assertEqual(a.val_loader.dataset, b.val_loader.dataset)
        self.assertNotEqual(list(a.train_loader.sampler), list(b.train_loader.sampler))
        self.assertEqual(old.vocab, explicit.vocab)
        self.assertEqual(old.train_loader.dataset, explicit.train_loader.dataset)
        self.assertEqual(old.val_loader.dataset, explicit.val_loader.dataset)
        self.assertNotEqual(a.val_loader.dataset, old.val_loader.dataset)


if __name__ == "__main__":
    unittest.main()
