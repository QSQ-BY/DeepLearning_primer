"""Word2Vec 预训练与训练词表对齐的离线检查。"""
import hashlib
from pathlib import Path
import tempfile
import unittest
import runpy
import warnings

import numpy as np
import torch

from news_classifier.experiments.word2vec import (
    load_word2vec_initialization,
    train_word_vectors,
)


class Word2VecTests(unittest.TestCase):
    def test_saved_model_loads_when_pretraining_module_runs_as_an_entrypoint(self):
        from gensim.models import Word2Vec

        with warnings.catch_warnings():
            warnings.filterwarnings('ignore', message=".*found in sys.modules.*", category=RuntimeWarning)
            entrypoint = runpy.run_module('news_classifier.experiments.word2vec', run_name='word2vec_cli')
        with tempfile.TemporaryDirectory() as tmp:
            entrypoint['train_word_vectors'](['bank news'] * 5, tmp, dimension=4,
                                              epochs=1, min_count=1)
            loaded = Word2Vec.load(str(Path(tmp) / 'word2vec.model'))
            self.assertIn('bank', loaded.wv)

    def test_pretraining_uses_only_supplied_texts_and_is_reproducible(self):
        from gensim.models import Word2Vec

        texts = ['West Bank peace news', 'Bank profit business news'] * 12
        vocab = {'<PAD>': 0, '<UNK>': 1, 'bank': 2, 'news': 3, 'heldout': 4}
        with tempfile.TemporaryDirectory() as tmp:
            metadata = train_word_vectors(
                texts, Path(tmp) / 'first', dimension=4, epochs=2,
                min_count=1, train_indices_sha256='training-only',
            )
            train_word_vectors(
                texts, Path(tmp) / 'second', dimension=4, epochs=2,
                min_count=1, train_indices_sha256='training-only',
            )
            first = Word2Vec.load(str(Path(tmp) / 'first' / 'word2vec.model'))
            second = Word2Vec.load(str(Path(tmp) / 'second' / 'word2vec.model'))
            self.assertNotIn('heldout', first.wv)
            self.assertIn('bank', first.wv)
            self.assertTrue(np.array_equal(first.wv.vectors, second.wv.vectors))
            self.assertEqual(metadata['corpus_rows'], len(texts))
            self.assertEqual(metadata['corpus_tokens'], 96)
            expected = ('west bank peace news\nbank profit business news\n' * 12)
            self.assertEqual(metadata['corpus_sha256'], hashlib.sha256(expected.encode()).hexdigest())
            initial = torch.arange(20, dtype=torch.float32).reshape(5, 4)
            weights, coverage = load_word2vec_initialization(
                Path(tmp) / 'first' / 'vectors.txt', vocab, initial, 'training-only',
            )
            self.assertTrue(np.allclose(weights[2].numpy(), first.wv['bank']))
            self.assertTrue(torch.equal(weights[4], initial[4]))
            self.assertTrue(torch.equal(weights[1], initial[1]))
            self.assertTrue(torch.equal(weights[0], torch.zeros(4)))
            self.assertEqual(coverage['matched_words'], 2)
            with self.assertRaises(FileExistsError):
                train_word_vectors(texts, Path(tmp) / 'first', dimension=4)

    def test_loading_rejects_different_training_split_or_modified_vectors(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp) / 'vectors'
            train_word_vectors(['bank news'] * 5, folder, dimension=4, epochs=1,
                               min_count=1, train_indices_sha256='expected-split')
            vocab = {'<PAD>': 0, '<UNK>': 1, 'bank': 2}
            initial = torch.zeros(3, 4)
            with self.assertRaisesRegex(ValueError, '训练划分'):
                load_word2vec_initialization(folder / 'vectors.txt', vocab, initial, 'other-split')
            with (folder / 'vectors.txt').open('a', encoding='utf-8') as stream:
                stream.write('tampered 1 2 3 4\n')
            with self.assertRaisesRegex(ValueError, 'SHA-256'):
                load_word2vec_initialization(folder / 'vectors.txt', vocab, initial, 'expected-split')


if __name__ == '__main__':
    unittest.main()
