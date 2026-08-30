import torch
import numpy
import sys
from pathlib import Path
common_dir = Path(__file__).resolve().parent.parent.parent / "通用模板库"
sys.path.insert(0, str(common_dir))

import d2lzh_pytorch as d2l
from d2lzh_pytorch import load_data_fashion_mnist

#获取和读取数据
batch_size = 256
train_iter,test_iter = load_data_fashion_mnist(batch_size)

#定义模型参数
#我们假设隐藏单元个数是256
num_inputs, num_outputs, num_hiddens = 784,10,256
w1 = torch.normal(0,0.01,(num_inputs,num_hiddens),dtype = torch.float,requires_grad = True)
b1 = torch.zeros(num_hiddens,dtype = torch.float,requires_grad = True)
w2 = torch.normal(0,0.01,(num_hiddens,num_outputs),dtype = torch.float,requires_grad = True)
b2 = torch.zeros(num_outputs,dtype = torch.float,requires_grad = True)
parameters = [w1,b1,w2,b2]

#定义激活函数
def relu(X):
    return torch.max(input = X,other = torch.tensor(0.0))

#定义模型
def net(X):
    X = X.view((-1,num_inputs))
    H = relu(torch.matmul(X,w1) + b1)
    return torch.matmul(H,w2) + b2

#定义损失函数
loss = torch.nn.CrossEntropyLoss()

num_epochs,lr = 10,100.0
d2l.train_ch3(net,train_iter,test_iter,loss,num_epochs,batch_size,parameters,lr)
