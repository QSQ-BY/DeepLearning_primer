#LeNet模型
import time
import torch
from torch import nn,optim
from pathlib import Path
import sys
common_dir = Path(__file__).resolve().parent.parent.parent / "通用模板库"
sys.path.insert(0, str(common_dir))

import d2lzh_pytorch as d2l
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

#模型实现
class LeNet(nn.Module):
    def __init__ (self):
        super().__init__()
        self.conv = nn.Sequential(
            #in_channels,out_channels,kernal_size
            nn.Conv2d(1,6,5),
            nn.Sigmoid(),
            #kernal_size,stride
            nn.MaxPool2d(2,2),
            nn.Conv2d(6,16,5),
            nn.Sigmoid(),
            nn.MaxPool2d(2,2),
        )

        #全连接层
        self.fc = nn.Sequential(
            nn.Linear(16*4*4,120),
            nn.Sigmoid(),
            nn.Linear(120,84),
            nn.Sigmoid(),
            nn.Linear(84,10)
        )
    def forward(self,img):
        feature = self.conv(img)
        output = self.fc(feature.view(img.shape[0],-1))
        return output
net = LeNet()
print(net)

#获取训练数据
batch_size = 256
train_iter,test_iter = d2l.load_data_fashion_mnist(batch_size)
lr,num_epochs = 0.001,10
#使用Adam优化算法
optimizer = torch.optim.Adam(net.parameters(),lr)
d2l.train_ch5(net,train_iter,test_iter,batch_size,optimizer,device,num_epochs)
