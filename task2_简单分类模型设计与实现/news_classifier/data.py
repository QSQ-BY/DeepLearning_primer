"""数据接口骨架：在这里完成 AG-news 读取和预处理。"""

from dataclasses import dataclass
from typing import Sequence

import torch
from torch.utils.data import DataLoader
import re
from collections import Counter
from functools import partial
LABEL_NAMES = ("World", "Sports", "Business", "Sci/Tech")


@dataclass(frozen=True)
class NewsSample:
    text: str
    label: int


@dataclass
class DataBundle:
    train_loader: DataLoader
    val_loader: DataLoader
    test_loader: DataLoader
    vocab: dict[str, int]
    label_names: tuple[str, ...] = LABEL_NAMES


def tokenize(text: str) -> list[str]:
    text = text.lower()
    tokens = re.findall(r"[a-z0-9]+",text)
    return tokens


#建立一张词->查找编号的词表
#传入samples:训练样本序列，config：完整的项目配置字典
def build_vocab(samples: Sequence[NewsSample], config: dict) -> dict[str, int]:
    data_config = config["data"]
    min_freq = data_config["min_freq"]#至少出现了min_freq的普通词才能进入词表
    max_vocab_size = data_config["max_vocab_size"]#整个词表的最多包含50000项
    counter = Counter()
    #遍历训练样本，统计每一个词出现的频率
    for sample in samples:
        counter.update(tokenize(sample.text))#累加每一个词出现的次数

    #按照词语出现的频率从高到低进行排列
    sorted_words = sorted(
        counter.items(),
        key = lambda item:(-item[1],item[0]),
    )

    vocab = {"<PAD>":0,"<UNK>":1}

    for word,frequency in sorted_words:
        if(frequency < min_freq):
            break
        if(len(vocab) >= max_vocab_size):
            break
        vocab[word] = len(vocab)

    return vocab

#传入整个文本串以及词表
def encode(text: str, vocab: dict[str, int], max_length: int) -> list[int]:
    #将整个文本转换为词编号
    if(max_length < 1):
        raise ValueError("max_length 必须大于等于 1")
    tokens = tokenize(text)
    tokens = tokens[:max_length]

    unk_id = vocab["<UNK>"]
    input_ids = [vocab.get(token,unk_id) for token in tokens]

    if(not input_ids):
        input_ids = [unk_id]
    return input_ids

#把多条不同长度的新闻整理成模型可以统一处理的张量，传入的每一个样本的结构是(词编号列表，新闻类别)
def collate_batch(
    batch: list[tuple[list[int], int]], min_length: int
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    #进行传入参数的检查
    if not batch:
        raise ValueError("batch 不能为空")
    if min_length < 1:
        raise ValueError("min_length 必须大于等于 1")
    #拿到每一批新闻序列和其对应的标签
    sequences,label_values = zip(*batch)

    if any(label < 0 or label >= 4 for label in label_values):
        raise ValueError("AG-news 标签必须在 0 到 3 之间")
    lengths = torch.tensor(
        [len(sequence) for sequence in sequences],
        dtype = torch.long,
    )
    batch_length = max(min_length,lengths.max().item())

    input_ids = torch.zeros(
        (len(batch),batch_length),dtype = torch.long
    )

    for row,sequence in enumerate(sequences):
        input_ids[row,:len(sequence)] = torch.tensor(
            sequence,dtype = torch.long,
        )
    labels = torch.tensor(label_values,dtype = torch.long)
    #返回最后的每一句话转换成的张量，每一句话对应的长度以及标签
    return input_ids,lengths,labels

def prepare_data(config: dict) -> DataBundle:
    """加载 AG-news，划分数据，并创建三个 DataLoader。"""
    from datasets import load_dataset

    data_config = config["data"]
    training_config = config["training"]

    # 1. 加载官方训练集和测试集。
    dataset = load_dataset(
        data_config["dataset_name"],
        cache_dir=data_config["cache_dir"],
    )

    # 2. 只从官方训练集中划分验证集，保持类别比例。
    split = dataset["train"].train_test_split(
        test_size=data_config["val_ratio"],
        seed=config["seed"],
        stratify_by_column="label",
    )

    train_dataset = split["train"]
    val_dataset = split["test"]
    test_dataset = dataset["test"]

    # 3. 只使用划分后的训练部分建立词表。
    train_samples = [
        NewsSample(text=row["text"], label=row["label"])
        for row in train_dataset
    ]
    vocab = build_vocab(train_samples, config)

    # 4. 固定批次填充函数所需的最小长度。
    min_length = max(config["model"]["kernel_sizes"])
    collate_fn = partial(collate_batch, min_length=min_length)

    # 5. 编码指定数据集，并创建 DataLoader。
    def make_loader(rows, shuffle: bool) -> DataLoader:
        encoded_samples = [
            (
                encode(row["text"], vocab, data_config["max_length"]),
                row["label"],
            )
            for row in rows
        ]

        generator = torch.Generator()
        generator.manual_seed(config["seed"])

        return DataLoader(
            encoded_samples,
            batch_size=training_config["batch_size"],
            shuffle=shuffle,
            num_workers=training_config["num_workers"],
            collate_fn=collate_fn,
            generator=generator,
        )

    # 6. 将数据加载器、词表和类别名称打包返回。
    return DataBundle(
        train_loader=make_loader(train_dataset, shuffle=True),
        val_loader=make_loader(val_dataset, shuffle=False),
        test_loader=make_loader(test_dataset, shuffle=False),
        vocab=vocab,
        label_names=LABEL_NAMES,
    )