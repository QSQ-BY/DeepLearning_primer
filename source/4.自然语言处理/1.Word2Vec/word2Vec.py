#word2Vec的实现
sentences = [
    # 动物：让 cat 和 dog 多次出现在相似上下文中
    "the cat likes milk",
    "the dog likes milk",
    "the cat drinks milk",
    "the dog drinks milk",
    "the cat drinks water",
    "the dog drinks water",
    "the cat eats fish",
    "the dog eats meat",
    "the cat eats food",
    "the dog eats food",
    "the cat sleeps on the bed",
    "the dog sleeps on the bed",
    "the cat plays in the garden",
    "the dog plays in the garden",
    "the cat is a small animal",
    "the dog is a small animal",

    # 水果：重复共同的属性和动作
    "the apple is fresh fruit",
    "the orange is fresh fruit",
    "the banana is fresh fruit",
    "the apple is sweet fruit",
    "the orange is sweet fruit",
    "the banana is sweet fruit",
    "the apple tastes sweet",
    "the orange tastes sweet",
    "the banana tastes sweet",
    "the apple grows in the garden",
    "the orange grows in the garden",
    "the banana grows in the garden",
    "the boy eats fruit",
    "the girl eats fruit",
    "the boy likes fruit",
    "the girl likes fruit",

    # 交通：让不同车辆共享动作和场景
    "the car moves through the city",
    "the bus moves through the city",
    "the train moves through the city",
    "the car carries people",
    "the bus carries people",
    "the train carries people",
    "the car moves on the road",
    "the bus moves on the road",
    "the truck moves on the road",
    "the car stops near the school",
    "the bus stops near the school",
    "the truck stops near the school",
    "the car has wheels",
    "the bus has wheels",
    "the truck has wheels",
    "the train stops near the station",

    # 自然：天空、水域、树木和天气
    "the bird flies in the sky",
    "the duck flies in the sky",
    "the duck swims in the river",
    "the fish swims in the river",
    "the bird lives near the river",
    "the duck lives near the river",
    "the bird rests on the tree",
    "the cat rests on the tree",
    "the sun shines in the sky",
    "the moon shines in the sky",
    "the sun rises above the mountain",
    "the moon rises above the mountain",
    "the rain falls on the garden",
    "the snow falls on the garden",
    "the rain falls on the tree",
    "the snow falls on the tree",

    # 学习：人物、书籍和课堂活动
    "the student reads a book",
    "the teacher reads a book",
    "the boy reads a book",
    "the girl reads a book",
    "the student writes words",
    "the teacher writes words",
    "the boy writes words",
    "the girl writes words",
    "the student uses a computer",
    "the teacher uses a computer",
    "the boy uses a computer",
    "the girl uses a computer",
    "the student studies in the classroom",
    "the teacher teaches in the classroom",
    "the boy studies at the school",
    "the girl studies at the school",
]
corpus = [sentence.lower().split() for sentence in sentences]
from collections import Counter
word_counts = Counter(
    word for sentence in corpus for word in sentence
)

#编号到单词的映射
idx_to_word = list(word_counts)
#list(word_count)会取出其中的键，也就是补充重复的单词，按照首次出现的顺序组成词表

#单词到编号的映射
word_to_idx = {
    word:idx for idx,word in enumerate(idx_to_word)
}

#将每一句转换为单词编号序列
encoded_corpus = [[word_to_idx[word] for word in sentence]for sentence in corpus]

vocab_size = len(idx_to_word)
print(word_to_idx)
print(encoded_corpus)
print("词表大小：",vocab_size)

window_size = 1
pairs = []

for sentence in encoded_corpus:
    for center_pos,center_id in enumerate(sentence):
        #上下文窗口的左右边界
        left = max(0,center_pos - window_size)
        right = min(len(sentence),center_pos+window_size+1)

        for context_pos in range(left,right):
            if(center_pos == context_pos):
                continue
            context_id = sentence[context_pos]
            #pairs用于构建上下文和中心词词对
            pairs.append((center_id,context_id))

# 把编号还原为单词，方便检查
#输出中心词->上下文单词
for center_id, context_id in pairs:
    print(f"{idx_to_word[center_id]} -> {idx_to_word[context_id]}")

print("训练样本数量：", len(pairs))

import torch
from torch import nn
#centers是提供的中心词编号
centers = torch.tensor(
    [center for center,context in pairs],
    dtype = torch.long
)
#targets是用中心词所推断的上下文编号
targets = torch.tensor(
    [context for center,context in pairs],
    dtype = torch.long
)

#定义skip_gram模型
class SkipGram(nn.Module):
    #传入词表中的单词的个数以及所选择的词向量的维度
    #告诉模型需要表示都少个单词并告诉模型每个单词用多少个数字表示
    def __init__(self,vocab_size,embedding_dim):
        super().__init__()
        #embedding:词嵌入，负责存储和查找每一个词所对应的词向量
        self.embedding = nn.Embedding(vocab_size,embedding_dim)
        #输入一个八维的词向量，然后输出词表当中每一个单词的分数
        #这个线性层自身也有一个可训练的权重矩阵
        #bias = False表示不给这个线性层加入偏置
        self.output = nn.Linear(
            embedding_dim,vocab_size,bias = False
        )

    def forward(self,center_ids):
        #这次输入的单词所查询出来的向量
        vectors = self.embedding(center_ids)
        logits = self.output(vectors)
        return logits

#固定随机种子，方便观察结果
torch.manual_seed(42)
embedding_dim = 8
model = SkipGram(vocab_size,embedding_dim)

#损失函数:评价上下文预测的误差
criterion = nn.CrossEntropyLoss()
#优化器，负责更新模型中的参数
optimizer = torch.optim.Adam(model.parameters(),lr = 0.05)

epochs = 30
model.train()
for epoch in range(epochs):
    optimizer.zero_grad()

    logits = model(centers)
    loss = criterion(logits,targets)
    loss.backward()
    optimizer.step()
    if epoch == 0 or (epoch + 1) % 50 == 0:
        print(f"Epoch {epoch + 1:3d}, loss = {loss.item():.4f}")

import torch.nn.functional as F
#取出训练后的词向量，后续计算不再进行梯度跟踪
#这里的detatch函数返回的是一个脱离计算图的张量，保留训练后的数据，不需要继续计算梯度
embeddings = model.embedding.weight.detach()
print("词向量的形状：",embeddings.shape)
#查看每个单词的向量
for idx,word in enumerate(idx_to_word):
    print(word,embeddings[idx])

#使用余弦相似度比较两个单词的向量
def similarity(word1,word2):
    vector1 = embeddings[word_to_idx[word1]]
    vector2 = embeddings[word_to_idx[word2]]

    source = F.cosine_similarity(vector1,vector2,dim = 0)
    return source.item()

#测试训练后的成果
def test01():
    # 同类词、不同类别词和单词自身的对照，用于观察学习结果
    comparison_pairs = [
        ("Animals", "cat", "dog"),
        ("Animals", "cat", "bird"),
        ("Animals", "bird", "duck"),
        ("Animals", "duck", "fish"),
        ("Fruit", "apple", "orange"),
        ("Fruit", "apple", "banana"),
        ("Fruit", "orange", "banana"),
        ("Vehicles", "car", "bus"),
        ("Vehicles", "car", "truck"),
        ("Vehicles", "bus", "train"),
        ("People", "student", "teacher"),
        ("People", "boy", "girl"),
        ("Nature", "sun", "moon"),
        ("Nature", "rain", "snow"),
        ("Cross", "cat", "milk"),
        ("Cross", "cat", "car"),
        ("Cross", "apple", "bus"),
        ("Cross", "dog", "computer"),
        ("Cross", "fruit", "road"),
        ("Cross", "bird", "book"),
        ("Self", "cat", "cat"),
        ("Self", "apple", "apple"),
        ("Self", "car", "car"),
    ]

    print("\n余弦相似度对照（Cross：不同类别，Self：单词自身）")
    table_border = "+------------+------------+------------+------------+"
    print(table_border)
    print(f"| {'Group':<10} | {'Word 1':<10} | {'Word 2':<10} | {'Cosine':>10} |")
    print(table_border)
    for group, word1, word2 in comparison_pairs:
        score = similarity(word1, word2)
        print(f"| {group:<10} | {word1:<10} | {word2:<10} | {score:>10.4f} |")
    print(table_border)

test01()
