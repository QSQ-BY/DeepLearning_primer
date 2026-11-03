"""按训练词表导入预训练向量，未覆盖词保留原始随机初始化。"""
from pathlib import Path
import hashlib
import numpy as np
import torch


def stable_hash(word):
    """为 Word2Vec 提供跨进程稳定、可由模型文件重新导入的词哈希。"""
    return int.from_bytes(hashlib.sha256(word.encode('utf-8')).digest()[:4], 'little')


def load_pretrained_vectors(path,vocab,initial):
    weights=initial.clone()
    dimension=weights.shape[1]
    matched=set()
    with Path(path).open(encoding='utf-8') as stream:
        for line in stream:
            word,_,values=line.rstrip().partition(' ')
            if word not in vocab or vocab[word]<2: continue
            vector=np.fromstring(values,sep=' ',dtype=np.float32)
            if len(vector)!=dimension:
                raise ValueError(f'{word} 的词向量维度为 {len(vector)}，应为 {dimension}')
            if not np.isfinite(vector).all(): raise ValueError('词向量包含非有限数')
            weights[vocab[word]]=torch.from_numpy(vector)
            matched.add(word)
    weights[vocab['<PAD>']].zero_()
    return weights,dict(matched_words=len(matched),ordinary_vocab_size=len(vocab)-2,
                        type_coverage=len(matched)/max(1,len(vocab)-2),embedding_dim=dimension)

