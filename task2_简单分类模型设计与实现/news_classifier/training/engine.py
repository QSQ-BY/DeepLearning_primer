"""单轮训练和评估接口；命令行、文件保存与调度器放在训练入口。"""

from dataclasses import dataclass

import torch
from torch import nn
from torch.utils.data import DataLoader


@dataclass(frozen=True)
class EpochMetrics:
    loss: float
    accuracy: float
    num_samples: int

def train_one_epoch(
    model: nn.Module,
    loader: DataLoader,
    optimizer: torch.optim.Optimizer,
    device: torch.device,
) -> EpochMetrics:
    #进行一轮的训练，返回统计的损失和准确率
    model.train()
    criterion = nn.CrossEntropyLoss()
    total_loss = 0.0
    total_correct = 0
    num_samples = 0

    for input_ids,lengths,labels in loader:
        input_ids = input_ids.to(device)
        lengths = lengths.to(device)
        labels = labels.to(device)

        optimizer.zero_grad(set_to_none = True)

        #进行前向传播，计算预测分数和损失
        logits = model.forward(input_ids,lengths)
        loss = criterion(logits,labels)

        loss.backward()
        optimizer.step()

        batch_size = labels.size(0)
        total_loss += loss.item()*batch_size
        total_correct += (
            logits.argmax(dim = 1) == labels
        ).sum().item()
        num_samples += batch_size

    if num_samples == 0:
        raise ValueError("训练 DataLoader 中没有样本")

    return EpochMetrics(
        loss=total_loss / num_samples,
        accuracy=total_correct / num_samples,
        num_samples=num_samples,
    )

@torch.no_grad()
def evaluate(
    model: nn.Module, loader: DataLoader, device: torch.device
) -> EpochMetrics:
    """评估模型，返回按样本平均的损失和准确率。"""
    model.eval()
    criterion = nn.CrossEntropyLoss()

    total_loss = 0.0
    total_correct = 0
    num_samples = 0

    for input_ids, lengths, labels in loader:
        input_ids = input_ids.to(device)
        lengths = lengths.to(device)
        labels = labels.to(device)

        logits = model(input_ids, lengths)
        loss = criterion(logits, labels)

        batch_size = labels.size(0)
        total_loss += loss.item() * batch_size
        total_correct += (
            logits.argmax(dim=1) == labels
        ).sum().item()
        num_samples += batch_size

    if num_samples == 0:
        raise ValueError("评估 DataLoader 中没有样本")

    return EpochMetrics(
        loss=total_loss / num_samples,
        accuracy=total_correct / num_samples,
        num_samples=num_samples,
    )
