"""使用双向 LSTM 编码变长新闻，输出四分类 logits。"""

import torch
from torch import nn
from torch.nn.utils.rnn import pack_padded_sequence


class BiLSTM(nn.Module):
    def __init__(self, vocab_size: int, model_config: dict, pad_id: int = 0):
        super().__init__()
        embed_dim = model_config["embed_dim"]
        hidden_size = model_config["hidden_size"]
        num_layers = model_config["num_layers"]
        dropout = model_config["dropout"]
        self.embedding = nn.Embedding(vocab_size, embed_dim, padding_idx=pad_id)
        self.embedding_dropout = nn.Dropout(model_config.get("embedding_dropout", 0.0))
        self.lstm = nn.LSTM(
            input_size=embed_dim,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True,
            bidirectional=True,
            # LSTM 内部的 dropout 只作用于相邻循环层之间。
            dropout=dropout if num_layers > 1 else 0.0,
        )
        self.dropout = nn.Dropout(dropout)
        self.classifier = nn.Linear(2 * hidden_size, model_config["num_classes"])

    def forward(self, input_ids: torch.Tensor, lengths: torch.Tensor) -> torch.Tensor:
        """[B, L] → [B, L, D] → [B, 2H] → [B, C]。"""
        if input_ids.ndim != 2 or lengths.ndim != 1 or lengths.numel() != input_ids.size(0):
            raise ValueError("input_ids 必须为 [B, L]，lengths 必须为 [B]")
        if lengths.dtype not in (torch.int32, torch.int64):
            raise ValueError("lengths 必须是整数张量")
        if lengths.numel() == 0 or (lengths < 1).any() or (lengths > input_ids.size(1)).any():
            raise ValueError("lengths 必须介于 1 和输入序列宽度之间")

        embedded = self.embedding_dropout(self.embedding(input_ids))
        # 打包后只计算真实词元；批次不必预先按长度排序。
        packed = pack_padded_sequence(
            embedded, lengths.detach().cpu(), batch_first=True, enforce_sorted=False,
        )
        _, (hidden, _) = self.lstm(packed)
        # 最后一层的两个方向各提供一个末状态，不取补齐序列的最后一列。
        features = torch.cat((hidden[-2], hidden[-1]), dim=1)
        return self.classifier(self.dropout(features))
