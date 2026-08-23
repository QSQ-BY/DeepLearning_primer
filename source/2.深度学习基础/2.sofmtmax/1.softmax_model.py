import torch
import torchvision
import numpy as np
from pathlib import Path
import sys

common_dir = Path(__file__).resolve().parent.parent.parent / "通用模板库"
sys.path.insert(0, str(common_dir))

import d2lzh_pytorch as d2l
from d2lzh_pytorch import load_data_fashion_mnist

#获取和读取数据
batch_size = 256
train_iter,test_iter = load_data_fashion_mnist(batch_size)

#初始化模型参数
#每个样本输入都是长和宽均为28个像素的图像
#因此模型的输入向量长度为28*28 = 784
num_inputs = 784
#输出为10种类别的图像分类
num_outputs = 10
W = torch.normal(0,0.01,(num_inputs,num_outputs),dtype = torch.float,requires_grad = True)
b = torch.zeros(num_outputs,dtype  = torch.float,requires_grad = True)

#实现softmax运算
#softmax运算会先通过exp函数对每个元素做指数运算，
#再对exp矩阵同行元素求和，最后令矩阵每行各元素与该行元素之和相除。
#这样一来，最终得到的矩阵每行元素和为1且非负。
#因此，该矩阵每行都是合法的概率分布。
#softmax运算的输出矩阵中的任意一行元素代表了一个样本在各个输出类别上的预测概率。
def softmax(X):
    X_exp = X.exp()#n行m列的张量
    partition = X_exp.sum(dim = 1,keepdim = True)#对同一行的元素求和，dim = 0是对每同一列的元素求和
    #partiotion是一个n行1列的张量
    return X_exp / partition

def test01():
    X = torch.normal(0,0.1,(2,5))
    X_prob = softmax(X)
    print(X,X_prob,X_prob.sum(dim=1,keepdim = True))

#test01()

#模型定义
def net(X):
    return softmax(torch.mm((X.view(-1,num_inputs)),W)+b)

#定义损失函数(交叉熵损失函数)
def cross_entropy(y_hat,y):
    return -torch.log(y_hat.gather(1,y.view(-1,1)))

#模型训练
d2l.train_ch3(net,train_iter,test_iter,cross_entropy,10,batch_size,[W,b],0.1)