import torch as tc
import numpy as np
import random

#绘图工具
from IPython import display
from matplotlib import pyplot as plt

from pathlib import Path
import sys

common_dir = Path(__file__).resolve().parent.parent.parent / "通用模板库"
sys.path.insert(0, str(common_dir))

import d2lzh_pytorch as d2l

import torch.utils.data as Data#导入数据模块
from torch import nn#导入神经网络模块,nn是神经网络的缩写
#线性回归第一种实现
def test01():
    tc.manual_seed(42)#自己设置随机种子

    num_examples = 1000#训练集总数
    num_inputs = 2#训练集变量数
    #整个训练集是一个1000行2列的矩阵
    #1000份数据，每一份的x\y随机生成
    features= tc.randn(num_examples,num_inputs,dtype = tc.float32)
    true_w = [2,-3.4]
    true_b = 4.2
    #y（标签）
    labels = true_w[0]*features[:,0] + true_w[1]*features[:,1] + true_b
    #为数据集添加随机噪声误差
    labels += tc.normal(0,0.01,size = labels.size(),dtype = tc.float32)

    #数据集展示
    # 数据集展示
    plt.figure(figsize=(3.5, 2.5))
    plt.scatter(
        features[:, 1].numpy(),#第二个变量
        labels.numpy(),
        s=1
    )
    plt.xlabel("feature 2")
    plt.ylabel("label")
    plt.show()

    """
    cnt = 5
    for X, y in d2l.data_iter(batch_size, features, labels):
        print(X, y)
        cnt -=1
        if(cnt == 0):break """

    #参数初始化
    w = tc.normal(0,0.01,(num_inputs,1),dtype = tc.float,requires_grad = True)#初始化w,为两行一列的矩阵
    b = tc.zeros(1,dtype = tc.float,requires_grad = True)

    """ 在训练中，我们将多次迭代模型参数。在每次迭代中，
    我们根据当前读取的小批量数据样本（特征X和标签y），
    通过调用反向函数backward计算小批量随机梯度，
    并调用优化算法sgd迭代模型参数。由于我们之前设批量大小batch_size为10，
    每个小批量的损失l的形状为(10, 1)。回忆一下自动求梯度一节。
    由于变量l并不是一个标量，所以我们可以调用.sum()将其求和得到一个标量，
    再运行l.backward()得到该变量有关模型参数的梯度。注意在每次更新完参数后不要忘了将参数的梯度清零。

    在一个迭代周期（epoch）中，我们将完整遍历一遍data_iter函数，
    并对训练数据集中所有样本都使用一次（假设样本数能够被批量大小整除）。
    这里的迭代周期个数num_epochs和学习率lr都是超参数，分别设3和0.03。
    在实践中，大多超参数都需要通过反复试错来不断调节。虽然迭代周期数设得越大模型可能越有效，
    但是训练时间可能过长。而有关学习率对模型的影响，我们会在后面“优化算法”一章中详细介绍。 """

    #模型训练
    #定义线性回归模型模板
    def linreg(X,w,b):
        return tc.mm(X,w)+b#mm为矩阵乘法
    lr = 0.01
    num_epochs = 10
    batch_size = 10
    for epoch in range(num_epochs):
        for X,y in d2l.data_iter(batch_size,features,labels):
            #1.向前传播
            y_hat = linreg(X,w,b)
            #2.计算损失函数
            loss = d2l.squared_loss(y_hat,y).sum()#使用sum函数计算总损失
            #3.反向传播计算梯度
            loss.backward()
            #使用sgd更新参数
            d2l.sgd([w,b],lr,batch_size)

        with tc.no_grad():
            train_loss = d2l.squared_loss(linreg(features,w,b),labels).mean()
        print(
            f"epoch {epoch + 1}, "
            f"loss {train_loss.item():.6f}"
        )

    #查看训练的结果
    print(f"w:{true_w}——{w}\n")
    print(f"b:{true_b}——{b}\n")

#线性回归模型的简洁实现
def test02():
    #数据集的生成与之前的一样
    tc.manual_seed(42)#自己设置随机种子
    num_examples = 1000#训练集总数
    num_inputs = 2#训练集变量数
    #整个训练集是一个1000行2列的矩阵
    #1000份数据，每一份的x\y随机生成
    features= tc.randn(num_examples,num_inputs,dtype = tc.float32)
    true_w = [2,-3.4]
    true_b = 4.2
    #y（标签）
    labels = true_w[0]*features[:,0] + true_w[1]*features[:,1] + true_b
    #为数据集添加随机噪声误差
    labels += tc.normal(0,0.01,size = labels.size(),dtype = tc.float32)

    #读取数据
    #使用pytorch提供的数据包Data来读取数据
    batch_size = 10
    #把训练数据的特征和标签进行组合
    dataset = Data.TensorDataset(features,labels)
    #随机读取小批量的数据
    data_iter = Data.DataLoader(dataset,batch_size,shuffle = True)
    #这里的dataiter的使用与上一个相同
    #for X,y in data_iter:

    #定义模型，继承nn的Module类
    class LinearNet(nn.Module):
        def __init__(self,n_feature):#传入特征的个数

            #这行代码调用父类 nn.Module 的构造函数。
            #它会初始化 PyTorch 管理模型所需的内部结构，包括：
            #- 子网络层
            #- 可训练参数
            #- 缓冲区
            #- 前向传播钩子
            #- 模型状态
            super().__init__()
            #输入特征数量：n_feature
            #输出特征数量：1
            #默认包含偏置参数 b
            self.linear = nn.Linear(n_feature,1)#创造线性层

        def forward(self,x):
            y_hat = self.linear(x)
            return y_hat
    #创建模型实体
    net = LinearNet(num_inputs)
    print(net)#使用print可以输出网络的结构
    print(net.linear.weight)#(输出特征数, 输入特征数)(y,x)->(1,2)
    print(net.linear.bias)#偏置值数，就相当于b
    #可以通过net.parameters()来查看模型所有的可学习参数，此函数将返回一个生成器。
    for param in net.parameters():
        print(param)

    #初始化参数
    from torch.nn import init
    #随机初始化系数
    init.normal_(net.linear.weight,mean = 0,std = 0.01)
    #直接给偏置赋初始值0
    init.constant_(net.linear.bias,val = 0)
    #init.zeros_(net.linear.bias)与上一句话等价

    #定义损失函数
    #PyTorch在nn模块中提供了各种损失函数，
    #这些损失函数可看作是一种特殊的层，
    #PyTorch也将这些损失函数实现为nn.Module的子类。
    #我们现在使用它提供的均方误差损失作为模型的损失函数
    loss = nn.MSELoss()

    #定义优化算法
    import torch.optim as optim
    optimizer = optim.SGD(net.parameters(),lr = 0.03)

    #训练模型
    num_epochs = 3
    for epoch in range(1,num_epochs+1):
        for X,y in data_iter:
            output = net(X)#向前传播
            l = loss(output,y.view(output.size()))
            optimizer.zero_grad()
            l.backward()
            optimizer.step()
        print(f"epoch:{epoch},loss:{l.item()}\n")

    print(f"w:{true_w}——{net.linear.weight}")
    print(f"b:{true_b}——{net.linear.bias}")

#test01()
test02()



