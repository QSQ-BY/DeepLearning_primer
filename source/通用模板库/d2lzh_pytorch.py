#绘图工具
from IPython import display
from matplotlib import pyplot as plt
from matplotlib_inline import backend_inline
import random
import torch
import numpy as np
def use_svg_display():
    # 用矢量图显示
    backend_inline.set_matplotlib_formats('svg')

def set_figsize(figsize=(3.5, 2.5)):
    use_svg_display()
    # 设置图的尺寸
    plt.rcParams['figure.figsize'] = figsize

#数据读取
def data_iter(batch_size,features,labels):
    num_examples = len(features)
    index = [i for i in range(num_examples)]#创建样本编号[0, 1, 2, 3, ..., 999]
    random.shuffle(index)#随机打乱编号
    for i in range(0,num_examples,batch_size):
        j = torch.tensor(index[i: min(i + batch_size, num_examples)],dtype = torch.long) # 最后一次可能不足一个batch
        yield  features.index_select(0, j), labels.index_select(0, j)
        #第一个参数0表示按照第0维进行选择，也就是选择行

#平方型损失函数
#y_hat模型计算出来的预测值，y数据集中的真实标签值
def squared_loss (y_hat,y):
    loss = (1/2) * ((y_hat - y.view(y_hat.size())))**2
    return loss

#随机梯度下降法迭代
#自动求梯度模块计算得来的梯度是一个批量样本的梯度和。我们将它除以批量大小来得到平均值。
#params为需要训练的参数，lr为学习率控制每次参数更新的步长，batch_size为样本数据量
def sgd(params,lr,batch_size):
    with torch.no_grad():
        for param in params:
            if(param.grad is None):
                continue
            #梯度下降，每次都往梯度的反方向更新训练参数
            param -= lr*param.grad/batch_size
            param.grad.zero_()#每都要把梯度重置

#获取数据集
import torchvision
import torchvision.transforms as transforms
import time
import sys
from pathlib import Path
def load_data_fashion_mnist(batch_size:int,resize = None):
    """下载 Fashion-MNIST，并返回训练集与测试集的数据迭代器。"""
    transform_list = []
    if(resize is not None):
        transform_list.append(transforms.Resize(resize))
    transform_list.append(transforms.ToTensor)
    transform = transforms.Compose(transform_list)

    data_root = (
        Path(__file__).resolve.parents[2]/".build"/"datasets"
    )

    train_dataset = torchvision.datasets.FashionMNIST(
        root = data_root,
        train = True,
        transform = transform,
        download = True,
    )

    test_dataset = torchvision.datasets.FashionMNIST(
        root = data_root,
        train = False,
        transform = transform,
        download = True,
    )

    #设置进程数
    num_workers = 0 if sys.platform.startswith("win") else 4
    #训练集生成器
    train_iter=torch.utils.data.Dataloader(
        train_dataset,
        batch_size = batch_size,
        shuffle = True,
        num_workers = num_workers,
    )
    #数据集生成器
    test_iter=torch.utils.data.Dataloader(
        test_dataset,
        batch_size = batch_size,
        shuffle = False,
        num_workers = num_workers,
    )

    return train_iter,test_iter


