"""AG-news数据读取、分词和批次处理。"""
from .dataset import LABEL_NAMES,NewsSample,DataBundle,tokenize,build_vocab,encode,collate_batch,prepare_data
