import torch
import torch.nn as nn
import torch.nn.functional as F

def test01():
    #词嵌入曾的实现
    #维度1:词表数量V:vocabulary size
    #维度2：词表中的每一个词用多少个向量来表示D:embedding_dimension
    #整个词嵌入曾的权重矩阵形状就是V*D
    embedding = nn.Embedding(
        num_embeddings=1000,
        embedding_dim=128,
        padding_idx = 0,#表示句子长度不一样的时候会优先填充0
    )

    #输入张量
    #维度1：批量大小B:batch size表示一共要处理多少句话
    #维度2：序列长度L:Sequence Length表示每一句的token数
    #输入张量大小就是B*L
    x = torch.randint(
        low = 0,high = 1000,
        size = (32,50)
    )
    #输出张量表示的是每一句的每一个单词对应的词向量
    #输出y的形状应该是B*L*D
    y = embedding(x)
    print(x.shape)
    print(y.shape)
    print(embedding.weight.shape)
    #输出：
    #torch.Size([32, 50])
    #torch.Size([32, 50, 128])
    #torch.Size([1000, 128])
    #这说明：
    #- 一个 Batch 有 32 句话。
    #- 每句话包含 50 个 Token。
    #- 每个 Token 对应一个 128 维向量。
    #- 词表大小为 1000，因此 Embedding 权重矩阵拥有 1000*128 个可训练参数。


    #卷积层的实现
    H = torch.tensor([
        [0.2,  0.5, -0.1],
        [0.6, -0.3,  0.8],
        [0.1,  0.7,  0.4],
        [0.9,  0.2,  0.6]
    ], dtype=torch.float32)

    # 添加 Batch 维度
    x = H.unsqueeze(0)
    print(x.shape)
    #输出为(1,4,3)表示输出了1个batch
    #每个batch里面由4个词，每个词对应3个向量
    #然后交换维度，原来是B*L*D
    #交换之后要变成B*D*L
    x = x.transpose(1,2)#交换原来的维度1和维度2
    print(x.shape)
    #输出：
    #torch.Size([1, 3, 4])
    #现在：
    #- 1：Batch Size
    #- 3：输入通道数，即 Embedding Dimension
    #- 4：句子长度

    #创建卷积层
    conv = nn.Conv1d(
        in_channels = 3,#输入通道数
        out_channels = 1,#输出通道数，这里规定为1
        kernel_size = 2,
        bias = True,
    )
    #人为给定的卷积核为
    #[
    #    [1,0,-1],
    #    [0,1,1]
    #]
    with torch.no_grad():
        conv.weight.copy_(
            torch.tensor([
                [
                    [ 1.0, 0.0],
                    [ 0.0, 1.0],
                    [-1.0, 1.0]
                ]
            ])
        )
        conv.bias.fill_(-0.7)
    #这里要按照pytorch的规定形状(输出通道数，输入通道数，卷积核长度)

    z = conv(x)
    a = torch.relu(z)
    print("卷积前：", tuple(x.shape))
    print("卷积后：", tuple(z.shape))
    print(
        "卷积结果：",
        [round(v, 2) for v in z.detach().flatten().tolist()]
    )
    print(
        "ReLU结果：",
        [round(v, 2) for v in a.detach().flatten().tolist()]
    )

    #使用conv2d实现，因为每一个展开的词向量矩阵都可以看成一个二维图像
    # Conv2d 实现
    x = H.unsqueeze(0).unsqueeze(0)
    # x.shape = (1, 1, 4, 3)
    conv2d = nn.Conv2d(
        in_channels=1,
        out_channels=1,
        kernel_size=(2, 3)
    )
    z = conv2d(x)
    print(z.shape)
    #               Conv1d 实现	    Conv2d 实现
    #输入形状	    (B,D,L)	         (B,1,L,D)
    #卷积核尺寸	        k	            (k,D)
    #输出通道数	        F	            F
    #输出形状	    (B,F,L-k+1)	    (B,F,L-k+1,1)


    #实现最大池化层
    A = torch.tensor(
        [
            [
                [0.1, 0.2, 0.0],
                [0.6, 0.6, 1.5],
                [0.4, 0.0, 0.8]
            ]
        ]
    )
    #三个维度分别表示(B,F,Lout)
    #B一个批量，也就是一句话
    #F卷积核数目，也就是输入的每个词向量维数embedding_dim
    #每个卷积核生成的激活值
    print(A.shape)

    #实现最大池化
    #方法一：直接使用max函数取最大值
    P = torch.max(A,dim = 2).values
    #这里使用dim = 2是直接字文本序列上求解最大值
    #使用dim = 1就是在不同的卷积核上求最大值
    print(P)
    print(P.shape)

    #方法二：使用torch自己提供的最大池化层
    pool = nn.AdaptiveMaxPool1d(output_size=1)
    p = pool(A)
    #经过池化层之后形状由原来的B*F*L
    #变成了现在的B*F*1#最后一个维度只保留最大值
    print(p)
    print(p.shape)
    #最后再进行压缩，把最后一个维度消除
    #最后就变成了B*F
    P = P.squeeze(-1)
    print(P.shape)
    #从词嵌入到句子特征向量的完整维度变化
    #Token ID 输入
    #(32,50)
    #    |Embedding
    #(32,50,128)
    #    |transpose(1,2)
    #Conv1d 输入
    #(32,128,50)
    #    |Conv1d(128,100,3) + ReLU
    #卷积特征图
    #(32,100,48)
    #    |AdaptiveMaxPool1d(1)
    #最大池化输出
    #(32,100,1)
    #    |squeeze(-1)
    #句子特征向量
    #组后每个句子对应100个维度的向量
    #每一个维度代表的都是这一个卷积核在当前这个句子检测到达最强反应
    #(32,100)


    #实现全连接和softmax以及交叉熵损失
    P = torch.tensor([
        [0.2,1.5,0.8]
    ],dtype = torch.float32)
    print(P.shape)
    #实现全连接层
    fc = nn.Linear(
        in_features = 3,
        out_features = 2,
    )
    with torch.no_grad():
        fc.weight.copy_(
            torch.tensor([
                [0.0, 1.0, 0.0],  # 消极类别
                [1.0, 0.0, 1.0]   # 积极类别
            ])
        )

        fc.bias.copy_(
            torch.tensor([-0.5, 1.0])
        )
    print(fc.weight.shape)
    print(fc.bias.shape)
    logits = fc(P)
    print(logits)
    print(logits.shape)
    probabilities = F.softmax(
        logits,
        dim=1
    )
    print(probabilities)
    pred = torch.argmax(logits, dim=1)
    print(pred)
    target = torch.tensor([1])
    loss = F.cross_entropy(logits, target)
    print(loss.item())

#实现完整的pytorh textcnn模型
import torch
import torch.nn as nn
import torch.nn.functional as F

#进行一个单次的小验证
def test02():
    

    class TextCNN(nn.Module):
        def __init__(
            self,
            vocab_size=1000,
            embed_dim=128,
            num_filters=100,#卷积核的数目，也是卷积层输出通道数
            #多个卷积核，每个卷积核的大小不同
            #但是最后经过最大池化都会变为一所以可以直接拼接
            #最后的结果几乎不受影响同样可以直接压缩最后一维
            kernel_sizes=(2, 3, 4),
            num_classes=2
        ):
            super().__init__()

            # 1. Embedding 层
            self.embedding = nn.Embedding(
                vocab_size,
                embed_dim
            )

            # 2. 多尺度卷积层
            self.convs = nn.ModuleList([
                nn.Conv1d(
                    in_channels=embed_dim,
                    out_channels=num_filters,
                    kernel_size=k
                )
                for k in kernel_sizes#实现不同大小的卷积核
            ])

            # 3. 全连接分类层
            self.fc = nn.Linear(
                num_filters * len(kernel_sizes),
                num_classes
            )

        def forward(self, x):

            # x: (B, L)

            # Embedding
            x = self.embedding(x)
            # x: (B, L, D)

            # 调整维度
            x = x.transpose(1, 2)
            # x: (B, D, L)

            pooled_outputs = []

            # 多尺度卷积
            for conv in self.convs:

                feature = F.relu(conv(x))
                # feature: (B, F, L-k+1)

                pooled = F.adaptive_max_pool1d(
                    feature,
                    output_size=1
                )
                # pooled: (B, F, 1)

                pooled = pooled.squeeze(-1)
                # pooled: (B, F)

                pooled_outputs.append(pooled)

            # 特征拼接,把每一个卷积核的output沿着最后一维进行拼接
            features = torch.cat(
                pooled_outputs,
                dim=1
            )
            # features: (B, F * len(kernel_sizes))

            # 全连接分类
            logits = self.fc(features)
            # logits: (B, num_classes)

            return logits
    #验证模型输出
    torch.manual_seed(42)
    model = TextCNN()
    # 模拟输入数据
    x = torch.randint(
        0, 1000, (32, 50)
    )
    logits = model(x)
    print("输入形状：", x.shape)
    print("输出形状：", logits.shape)
    # 预测类别
    pred = logits.argmax(dim=1)
    print("预测结果形状：", pred.shape)

    #加上损失函数和反向传播
    #进行单次测试
    target = torch.randint(
        0, 2, (32,)
    )
    # 计算损失
    loss = F.cross_entropy(logits, target)
    print("Loss:", loss.item())
    # 反向传播
    loss.backward()

import random
from collections import Counter
from torch.utils.data import Dataset,DataLoader

#进行一次完整的textcnn训练
def test03():
    # ======================================
    # 1. 超参数
    # ======================================

    SEED = 42
    BATCH_SIZE = 16
    EMBED_DIM = 32
    NUM_FILTERS = 32
    KERNEL_SIZES = (2, 3, 4)
    EPOCHS = 12
    LEARNING_RATE = 0.003

    PAD_ID = 0
    UNK_ID = 1

    random.seed(SEED)
    torch.manual_seed(SEED)

    device = torch.device(
        "cuda" if torch.cuda.is_available() else "cpu"
    )

    print("运行设备：", device)


    # ======================================
    # 2. 创建教学数据集
    # ======================================

    subjects = [
        ("这部", "电影"),
        ("这部", "电视剧"),
        ("这本", "小说"),
        ("这个", "游戏"),
        ("这个", "节目"),
        ("这个", "故事"),
        ("这部", "动画"),
        ("这个", "作品"),
    ]

    positive_patterns = [
        "真的 很 好看",
        "特别 精彩",
        "非常 有趣",
        "令人 感动",
        "十分 优秀",
        "特别 棒",
        "值得 推荐",
        "体验 很好",
        "表现 出色",
        "我 很 喜欢",
    ]

    negative_patterns = [
        "真的 很 难看",
        "特别 无聊",
        "非常 乏味",
        "令人 失望",
        "十分 糟糕",
        "特别 差",
        "不 值得 推荐",
        "体验 很差",
        "表现 失败",
        "我 很 讨厌",
    ]

    positive_samples = []
    negative_samples = []

    for prefix, subject in subjects:
        for pattern in positive_patterns:
            text = f"{prefix} {subject} {pattern}"
            positive_samples.append((text, 1))

        for pattern in negative_patterns:
            text = f"{prefix} {subject} {pattern}"
            negative_samples.append((text, 0))

    # 固定随机种子，按类别划分数据
    rng = random.Random(SEED)
    rng.shuffle(positive_samples)
    rng.shuffle(negative_samples)

    pos_split = int(len(positive_samples) * 0.8)
    neg_split = int(len(negative_samples) * 0.8)

    train_data = (
        positive_samples[:pos_split]
        + negative_samples[:neg_split]
    )

    val_data = (
        positive_samples[pos_split:]
        + negative_samples[neg_split:]
    )

    print("训练样本：", len(train_data))
    print("验证样本：", len(val_data))


    # ======================================
    # 3. 构建词表
    # ======================================

    # 只使用训练集构建词表
    counter = Counter()

    for text, label in train_data:
        counter.update(text.split())

    vocab = {
        "<PAD>": PAD_ID,
        "<UNK>": UNK_ID,
    }

    for token, count in counter.most_common():
        vocab[token] = len(vocab)

    print("词表大小：", len(vocab))


    def encode(text, vocab):
        tokens = text.strip().split()

        if not tokens:
            raise ValueError("输入文本不能为空")

        return [
            vocab.get(token, UNK_ID)
            for token in tokens
        ]


    # ======================================
    # 4. Dataset
    # ======================================

    class ReviewDataset(Dataset):
        def __init__(self, samples, vocab):
            self.samples = [
                (encode(text, vocab), label)
                for text, label in samples
            ]

        def __len__(self):
            return len(self.samples)

        def __getitem__(self, idx):
            return self.samples[idx]

    train_dataset = ReviewDataset(train_data, vocab)
    val_dataset = ReviewDataset(val_data, vocab)
    # ======================================
    # 5. collate_fn：Batch 填充
    # ======================================

    def collate_fn(batch):

        sequences, labels = zip(*batch)

        lengths = torch.tensor(
            [len(seq) for seq in sequences],
            dtype=torch.long
        )

        # 至少达到最大卷积核长度
        max_len = max(
            max(len(seq) for seq in sequences),
            max(KERNEL_SIZES)
        )

        input_ids = torch.full(
            (len(sequences), max_len),
            PAD_ID,
            dtype=torch.long
        )

        for i, seq in enumerate(sequences):
            input_ids[i, :len(seq)] = torch.tensor(
                seq, dtype=torch.long
            )

        labels = torch.tensor(
            labels, dtype=torch.long
        )

        return input_ids, lengths, labels


    train_loader = DataLoader(
        train_dataset,
        batch_size=BATCH_SIZE,
        shuffle=True,
        collate_fn=collate_fn
    )

    val_loader = DataLoader(
        val_dataset,
        batch_size=BATCH_SIZE,
        shuffle=False,
        collate_fn=collate_fn
    )


    # ======================================
    # 6. TextCNN 模型
    # ======================================

    class TextCNN(nn.Module):

        def __init__(self, vocab_size):
            super().__init__()

            self.embedding = nn.Embedding(
                num_embeddings=vocab_size,#整个词表的单词总数
                embedding_dim=EMBED_DIM,
                padding_idx=PAD_ID
            )

            self.convs = nn.ModuleList([
                nn.Conv1d(
                    in_channels=EMBED_DIM,
                    out_channels=NUM_FILTERS,
                    kernel_size=k
                )
                for k in KERNEL_SIZES
            ])

            self.dropout = nn.Dropout(0.3)

            self.fc = nn.Linear(
                NUM_FILTERS * len(KERNEL_SIZES),
                2
            )

        def forward(self, input_ids, lengths):

            # (B, L) -> (B, L, D)
            x = self.embedding(input_ids)

            # (B, L, D) -> (B, D, L)
            x = x.transpose(1, 2)

            pooled_outputs = []

            for conv in self.convs:

                # (B, D, L) -> (B, F, L-k+1)
                feature = F.relu(conv(x))

                kernel_size = conv.kernel_size[0]

                # 有效卷积窗口数量
                valid_count = (
                    lengths - kernel_size + 1
                ).clamp(min=1)

                positions = torch.arange(
                    feature.size(-1),
                    device=feature.device
                ).unsqueeze(0)

                mask = (
                    positions < valid_count.unsqueeze(1)
                )

                # 忽略无效 Padding 窗口
                feature = feature.masked_fill(
                    ~mask.unsqueeze(1),
                    float("-inf")
                )

                # 全局最大池化：(B, F)
                pooled = feature.amax(dim=-1)

                pooled_outputs.append(pooled)

            # 多尺度特征拼接：(B, 96)
            features = torch.cat(
                pooled_outputs, dim=1
            )

            features = self.dropout(features)

            # 分类 Logits：(B, 2)
            logits = self.fc(features)

            return logits

    model = TextCNN(len(vocab)).to(device)

    optimizer = torch.optim.Adam(
        model.parameters(),
        lr=LEARNING_RATE
    )


    # ======================================
    # 7. 训练一个 Epoch
    # ======================================

    def train_one_epoch(model, loader, optimizer):

        model.train()

        total_loss = 0.0
        correct = 0
        total = 0

        for input_ids, lengths, labels in loader:

            input_ids = input_ids.to(device)
            lengths = lengths.to(device)
            labels = labels.to(device)

            # ① 清空上一轮梯度
            optimizer.zero_grad(set_to_none=True)

            # ② 前向传播
            logits = model(input_ids, lengths)

            # ③ 计算交叉熵损失
            loss = F.cross_entropy(logits, labels)

            # ④ 反向传播
            loss.backward()

            # ⑤ Adam 更新参数
            optimizer.step()

            batch_size = labels.size(0)

            total_loss += loss.item() * batch_size

            predictions = logits.argmax(dim=1)

            correct += (
                predictions == labels
            ).sum().item()

            total += batch_size

        return total_loss / total, correct / total


    # ======================================
    # 8. 验证集评估
    # ======================================

    @torch.no_grad()
    def evaluate(model, loader):

        model.eval()

        total_loss = 0.0
        correct = 0
        total = 0

        for input_ids, lengths, labels in loader:

            input_ids = input_ids.to(device)
            lengths = lengths.to(device)
            labels = labels.to(device)

            logits = model(input_ids, lengths)

            loss = F.cross_entropy(logits, labels)

            batch_size = labels.size(0)

            total_loss += loss.item() * batch_size

            predictions = logits.argmax(dim=1)

            correct += (
                predictions == labels
            ).sum().item()
            total += batch_size

        return total_loss / total, correct / total


    # ======================================
    # 9. 正式开始训练
    # ======================================

    best_val_loss = float("inf")
    best_state = None

    for epoch in range(EPOCHS):

        train_loss, train_acc = train_one_epoch(
            model, train_loader, optimizer
        )

        val_loss, val_acc = evaluate(
            model, val_loader
        )

        print(
            f"Epoch {epoch+1:02d}/{EPOCHS} | "
            f"Train Loss: {train_loss:.4f} | "
            f"Train Acc: {train_acc:.2%} | "
            f"Val Loss: {val_loss:.4f} | "
            f"Val Acc: {val_acc:.2%}"
        )

        # 根据验证集损失保留最佳权重
        if val_loss < best_val_loss:
            best_val_loss = val_loss
            best_state = {
                key: value.detach().cpu().clone()
                for key, value in model.state_dict().items()
            }

    model.load_state_dict(best_state)

    torch.save(
        {
            "model_state_dict": best_state,
            "vocab": vocab,
        },
        "textcnn_demo.pt"
    )

    print("最佳模型已保存：textcnn_demo.pt")


    # ======================================
    # 10. 使用训练好的模型预测
    # ======================================

    @torch.no_grad()
    def predict(text):

        model.eval()

        encoded = encode(text, vocab)

        input_ids, lengths, _ = collate_fn([
            (encoded, 0)
        ])

        input_ids = input_ids.to(device)
        lengths = lengths.to(device)

        logits = model(input_ids, lengths)

        probabilities = F.softmax(
            logits, dim=1
        )[0]

        predicted_class = probabilities.argmax().item()

        return predicted_class, probabilities.cpu().tolist()


    test_texts = [
        "这部 电影 真的 很 好看",
        "这个 游戏 特别 无聊",
        "这本 小说 令人 感动",
        "这个 节目 不 值得 推荐",
    ]

    for text in test_texts:
        label, probabilities = predict(text)
        sentiment = "积极" if label == 1 else "消极"
        print(
            f"文本：{text}\n"
            f"预测：{sentiment}\n"
            f"消极概率：{probabilities[0]:.2%}，"
            f"积极概率：{probabilities[1]:.2%}\n"
        )

#test01()
#test02()
test03()