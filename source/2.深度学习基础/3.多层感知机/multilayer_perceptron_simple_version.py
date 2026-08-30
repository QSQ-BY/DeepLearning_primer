import torch
import numpy
import sys
from pathlib import Path
common_dir = Path(__file__).resolve().parent.parent.parent / "通用模板库"
sys.path.insert(0, str(common_dir))
from torch import nn
from torch.nn import init

import d2lzh_pytorch as d2l
from d2lzh_pytorch import load_data_fashion_mnist

num_inputs, num_outputs, num_hiddens = 784, 10, 256

#模型定义
net = nn.Sequential(
    d2l.FlattenLayer(),
    nn.Linear(num_inputs,num_hiddens),
    nn.ReLU(),
    nn.Linear(num_hiddens,num_outputs),
)
for params in net.parameters():
    init.normal_(params,mean = 0,std = 0.01)

#数据读取
batch_size = 256
train_iter, test_iter = d2l.load_data_fashion_mnist(batch_size)
loss = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(net.parameters(),lr = 0.5)
num_epochs = 10

#模型训练
d2l.train_ch3(net, train_iter, test_iter, loss, num_epochs, batch_size, None, None, optimizer)
