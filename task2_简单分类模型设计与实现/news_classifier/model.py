"""TextCNN 接口骨架，参考 source 下已有的 TextCNN 学习代码实现。"""

import torch
from torch import nn

#实现textcnn模型
class TextCNN(nn.Module):
    def __init__(self, vocab_size: int, model_config: dict, pad_id: int = 0):
        super().__init__()
        embed_dim = model_config["embed_dim"]#每一个单词用一个几维向量来表示
        num_filters = model_config["num_filters"]#卷积层的输出通道数，等于卷积核数
        self.kernel_sizes = tuple(model_config["kernel_sizes"])

        #创建词嵌入层，把每一句话转化成一个个可处理张量
        self.embedding = nn.Embedding(
            num_embeddings = vocab_size,#整个词表的大小
            embedding_dim= embed_dim,#每一个词用一个几维向量来表示
            padding_idx= pad_id,
        )

        #创建卷积层
        self.convs = nn.ModuleList([
            nn.Conv1d(
                in_channels = embed_dim,
                out_channels = num_filters,
                kernel_size = kernel_size,
            )
            for kernel_size in self.kernel_sizes
        ])

        self.dropout = nn.Dropout(p = model_config["dropout"])
        #每个卷积层分支池化之后提供num_filters个特征（在前向传播实现手动池化层）
        #最后的输出就是卷积核的种类数量*每一种卷积核对应的数量也就是输出通道数
        #最后的没有个输出通道经过最后的最大池化层之后都会变为一个单独的数
        feature_dim = num_filters * len(self.kernel_sizes)

        self.classifier = nn.Linear(
            in_features = feature_dim,
            out_features = model_config["num_classes"],
            bias = True,
        )


    #传入每一句话对应的词表编号序列以及每一句话对应的实际长度
    def forward(
        self, input_ids: torch.Tensor, lengths: torch.Tensor
    ) -> torch.Tensor:
        """提取多尺度文本特征，屏蔽无效窗口，输出分类 logits。"""
    
        # [B, L] → [B, L, D] → [B, D, L]
        x = self.embedding(input_ids)
        x = x.transpose(1, 2)
        lengths = lengths.to(input_ids.device)
    
        pooled_features = []
    
        for kernel_size, conv in zip(self.kernel_sizes, self.convs):
            # [B, D, L] → [B, F, L-k+1]
            features = torch.relu(conv(x))
    
            # 正常句子保留完全位于真实文本中的窗口。
            # 短于卷积核的句子，保留第一个包含右侧补零的窗口。
            valid_counts = (lengths - kernel_size + 1).clamp(min=1)
    
            positions = torch.arange(
                features.size(2),
                device=features.device,
            ).unsqueeze(0)
    
            valid_mask = positions < valid_counts.unsqueeze(1)
    
            # 无效窗口不参与最大值竞争。
            features = features.masked_fill(
                ~valid_mask.unsqueeze(1),
                float("-inf"),
            )
            # 沿序列方向池化：[B, F, L-k+1] → [B, F]
            pooled = features.max(dim=2).values
            pooled_features.append(pooled)
    
        # 拼接三个分支：[B, 128] × 3 → [B, 384]
        combined = torch.cat(pooled_features, dim=1)
        combined = self.dropout(combined)
    
        # [B, 384] → [B, 4]
        logits = self.classifier(combined)
        return logits
    
