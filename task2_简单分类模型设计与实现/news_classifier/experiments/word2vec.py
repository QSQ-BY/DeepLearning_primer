"""仅用固定训练集预训练 Word2Vec；不读取验证、测试文本或类别标签。"""
import argparse
import hashlib
import json
from pathlib import Path
import platform
import sys
import time

import numpy as np
import torch

from ..config import project_path
from ..data import NewsSample, build_vocab, tokenize
from ..data.embeddings import load_pretrained_vectors, stable_hash
from ..evaluation.analysis import ROOT, cached_split, write_json


class EpochProgress:
    def __init__(self):
        self.epoch = 0
        self.started = time.perf_counter()

    def on_train_begin(self, model):
        pass

    def on_train_end(self, model):
        pass

    def on_epoch_begin(self, model):
        pass

    def on_epoch_end(self, model):
        self.epoch += 1
        print(f'Word2Vec epoch {self.epoch}/{model.epochs} | '
              f'{time.perf_counter() - self.started:.1f}s', flush=True)


def train_word_vectors(texts, output_dir, *, dimension=128, epochs=10,
                       min_count=2, train_indices_sha256=None):
    """先分词再训练单线程 Skip-gram，保存模型、向量及可核对的语料摘要。"""
    import gensim
    from gensim.models import Word2Vec

    output_dir = Path(output_dir)
    if output_dir.exists() and any(output_dir.iterdir()):
        raise FileExistsError(f'保留已有预训练结果，请使用新目录：{output_dir}')
    output_dir.mkdir(parents=True, exist_ok=True)
    sentences = [tokenize(text) for text in texts]
    digest = hashlib.sha256()
    for sentence in sentences:
        digest.update((' '.join(sentence) + '\n').encode('utf-8'))
    parameters = dict(vector_size=dimension, window=5, min_count=min_count,
                      sg=1, hs=0, negative=5, ns_exponent=0.75, sample=0.001,
                      alpha=0.025, min_alpha=0.0001, epochs=epochs,
                      workers=1, seed=42, sorted_vocab=1, shrink_windows=True)
    started = time.perf_counter()
    model = Word2Vec(**parameters, hashfxn=stable_hash)
    model.build_vocab(sentences)
    print(f'Word2Vec: {len(sentences)}条训练文本，{model.corpus_total_words}词，'
          f'{len(model.wv)}词表项，{dimension}维 Skip-gram', flush=True)
    model.train(sentences, total_examples=model.corpus_count, epochs=epochs,
                callbacks=[EpochProgress()])
    model.save(str(output_dir / 'word2vec.model'), separately=[])
    vector_path = output_dir / 'vectors.txt'
    # 无数字头行，直接复用按词对齐的预训练向量加载器。
    with vector_path.open('w', encoding='utf-8', newline='\n') as stream:
        for word in model.wv.index_to_key:
            values = ' '.join(format(float(value), '.9g') for value in model.wv[word])
            stream.write(f'{word} {values}\n')
    metadata = dict(method='word2vec_skipgram_negative_sampling', parameters=parameters,
                    tokenizer='lowercase_regex_[a-z0-9]+', corpus_split='training_only',
                    labels_used=False, external_corpus_used=False,
                    corpus_rows=len(sentences), corpus_tokens=sum(map(len, sentences)),
                    corpus_sha256=digest.hexdigest(),
                    train_indices_sha256=train_indices_sha256,
                    vector_vocab_size=len(model.wv),
                    vectors_sha256=hashlib.sha256(vector_path.read_bytes()).hexdigest(),
                    model_sha256=hashlib.sha256((output_dir / 'word2vec.model').read_bytes()).hexdigest(),
                    gensim=gensim.__version__, numpy=np.__version__, python=platform.python_version(),
                    hash_function='sha256_first_4_bytes_little_endian',
                    elapsed_seconds=time.perf_counter() - started)
    write_json(output_dir / 'source_manifest.json', metadata)
    return metadata


def load_word2vec_initialization(path, vocab, initial, train_indices_sha256):
    """拒绝不同训练划分或已被修改的向量，再按原有词编号导入。"""
    path = Path(path)
    source = json.loads((path.parent / 'source_manifest.json').read_text(encoding='utf-8'))
    if source['train_indices_sha256'] != train_indices_sha256:
        raise ValueError('Word2Vec 语料与分类器训练划分不一致')
    if source['vectors_sha256'] != hashlib.sha256(path.read_bytes()).hexdigest():
        raise ValueError('Word2Vec 向量 SHA-256 不一致')
    if source['parameters']['vector_size'] != initial.shape[1]:
        raise ValueError('Word2Vec 维度与分类器词向量维度不一致')
    if source['corpus_split'] != 'training_only' or source['labels_used']:
        raise ValueError('Word2Vec 必须仅使用无标签训练文本')
    weights, metadata = load_pretrained_vectors(path, vocab, initial)
    metadata['source'] = source
    metadata['vector_path'] = str(path.resolve())
    return weights, metadata


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', default='../.build/task2/pretrained/word2vec_ag_news128_20261103')
    parser.add_argument('--epochs', type=int, default=10)
    args = parser.parse_args()
    source = ROOT / '.build/task2/runs/textcnn_k237_plateau20/best_accuracy.pt'
    checkpoint = torch.load(source, map_location='cpu', weights_only=True)
    config = checkpoint['config']
    raw = cached_split('train', config['data']['cache_dir'])
    raw = raw.add_column('source_row', list(range(len(raw))))
    split = raw.train_test_split(test_size=config['data']['val_ratio'], seed=config['seed'],
                                stratify_by_column='label')
    train_ids = np.asarray(split['train']['source_row'], dtype=np.int64)
    validation_ids = np.asarray(split['test']['source_row'], dtype=np.int64)
    assert len(train_ids) == 108000 and len(validation_ids) == 12000
    assert not set(train_ids) & set(validation_ids)
    samples = [NewsSample(row['text'], row['label']) for row in split['train']]
    assert build_vocab(samples, config) == checkpoint['vocab']
    output_dir = project_path(args.output_dir)
    metadata = train_word_vectors(
        [sample.text for sample in samples], output_dir,
        dimension=config['model']['embed_dim'], epochs=args.epochs,
        min_count=config['data']['min_freq'],
        train_indices_sha256=hashlib.sha256(train_ids.tobytes()).hexdigest(),
    )
    np.savez_compressed(output_dir / 'split_indices.npz', train=train_ids, validation=validation_ids)
    metadata.update(source_checkpoint=str(source),
                    source_checkpoint_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                    validation_indices_sha256=hashlib.sha256(validation_ids.tobytes()).hexdigest())
    write_json(output_dir / 'source_manifest.json', metadata)
    print(f'预训练完成：{output_dir}', flush=True)


if __name__ == '__main__':
    main()
