#softmax模型的简洁实现
import torch
from torch import nn
from torch.nn import init
import torchvision
import numpy as np
from pathlib import Path
import sys

common_dir = Path(__file__).resolve().parent.parent.parent / "通用模板库"
sys.path.insert(0, str(common_dir))

import d2lzh_pytorch as d2l
from d2lzh_pytorch import FlattenLayer
from d2lzh_pytorch import train_ch3
#获取和读取数据
batch_size = 256
train_iter,test_iter = d2l.load_data_fashion_mnist(batch_size)

#定义和初始化模型
num_inputs = 784
num_outputs = 10
class LinearNet(nn.Module):
    def __init__(self,num_inputs,num_outputs):
        super().__init__()
        self.linear = nn.Linear(num_inputs,num_outputs)
    def forward(self,x):#x shape:（batch_size,1,28,28)
        y = self.linear(x.view(x.shape[0],-1))
        return y

net = LinearNet(num_inputs,num_outputs)
#初始化模型的权重参数
init.normal_(net.linear.weight,mean = 0,std = 0.01)
init.zeros_(net.linear.bias)

#损失函数
loss = nn.CrossEntropyLoss()

#定义优化算法
optimizer = torch.optim.SGD(net.parameters(),lr = 0.1)

#训练模型
num_epochs = 10
d2l.train_ch3(net,train_iter,test_iter,loss,num_epochs,batch_size,None,None,optimizer)