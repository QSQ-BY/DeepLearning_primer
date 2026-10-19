import torch
from torch import nn
from torch.nn import functional as F

torch.manual_seed(42)
text = "hello pytorch\n"*(100)

chars = sorted(set(text))
char_to_id = {ch:i for i,ch in enumerate(chars)}
data = torch.tensor([char_to_id[ch] for ch in text],dtype = torch.long)

vocab_size = len(chars)
batch_size,num_steps,hidden_size = 16,16,32

def get_batch():
    #随机选取16段序列，每段包含16个时间步
    starts = torch.randint(len(data)-num_steps,(batch_size,))
    positions = starts[:,None] + torch.arange(num_steps)

    X = data[positions]
    Y = data[positions+1]
    return X,Y

class CharRNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.rnn = nn.RNN(
            input_size = vocab_size,
            hidden_size = hidden_size,
            batch_first = True,
        )
        self.output = nn.Linear(hidden_size,vocab_size)

    def forward(self,X):
        X = F.one_hot(X,num_classes = vocab_size).float()
        #rnn返回的是，所有时间步的隐藏状态H，以及最后一个时间步的隐藏状态
        H,h_last = self.rnn(X)
        logits = self.output(H)
        return logits,h_last

model = CharRNN()
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(),lr = 0.01)
for step in range(1,101):
    X,Y = get_batch()
    optimizer.zero_grad()
    logits,h_last = model(X)
    #把batch和时间维度展开：每个时间步都是一次字符分类
    loss = criterion(logits.reshape(-1,vocab_size),Y.reshape(-1))
    #BPTT:沿展开的时间链路反向传播
    loss.backward()

    grad_norm = nn.utils.clip_grad_norm_(
        model.parameters(),
        max_norm = 1.0,
    )

    optimizer.step()

    if(step == 1 or step%20 == 0):
        print(
            f"step={step:3d} "
            f"loss={loss.item():.4f} "
            f"grad_norm_before_clip={grad_norm.item():.4f}"
        )

X,Y = get_batch()
model.eval()
with torch.no_grad():
    logits,_ = model(X)
    prediction = logits.argmax(dim = -1)
def decode(ids):
    return repr("".join(chars[i] for i in ids.tolist()))

print("输入：", decode(X[0]))
print("目标：", decode(Y[0]))
print("预测：", decode(prediction[0]))

#参数	                    在这个任务中的含义
#input_size=vocab_size	    每个字符转为 one-hot 后，向量长度等于词表大小
#hidden_size=hidden_size	每个时间步的隐藏状态有 32 个特征
#num_layers=1	            使用一层 LSTM，循环处理所有时间步
#batch_first=True	        输入和序列输出按「批量、时间步、特征」排列
class CharLSTM(nn.Module):
    def __init__(self):
        super().__init__()
        #lstm层
        self.lstm = nn.LSTM(
            input_size = vocab_size,
            hidden_size = hidden_size,
            num_layers = 1,
            batch_first = True,
        )
        #最后的线性输出层
        self.output = nn.Linear(hidden_size,vocab_size)

    def forward(self,X):
        #字符编号->one_hot 浮点向量
        X = F.one_hot(X,num_classes = vocab_size).float()
        H,(h_last,c_last) = self.lstm(X)
        logits = self.output(H)
        return logits,(h_last,c_last)

model = CharLSTM()
X, Y = get_batch()

logits, (h_last, c_last) = model(X)

print("X:", X.shape)
print("Y:", Y.shape)
print("logits:", logits.shape)
print("h_last:", h_last.shape)
print("c_last:", c_last.shape)
model = CharLSTM()
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(),lr = 0.01)
model.train()

for step in range(1,101):
    X,Y = get_batch()
    optimizer.zero_grad()
    logits,_ = model(X)
    loss = criterion(
        logits.reshape(-1,vocab_size),
        Y.reshape(-1),
    )
    loss.backward()
    nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
    optimizer.step()

    if step == 1 or step % 20 == 0:
        print(f"step={step:3d} loss={loss.item():.4f}")
model.eval()

with torch.no_grad():
    X, Y = get_batch()
    logits, _ = model(X)
    #在最后一维的 11 个字符分数中，选出最高分对应的字符编号
    prediction = logits.argmax(dim=-1)

print("LSTM 输入：", decode(X[0]))
print("LSTM 目标：", decode(Y[0]))
print("LSTM 预测：", decode(prediction[0]))