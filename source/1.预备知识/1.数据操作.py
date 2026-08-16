""" 在PyTorch中，torch.Tensor是存储和变换数据的主要工具 """


""" tensor的创建 """
import torch

def test01():
    """ 空矩阵 """
    x = torch.empty(5, 3)
    print(x)
    """ 随机矩阵 """
    y = torch.rand(5,3)
    print(y)
    """ 0矩阵，并且矩阵数据类型为long """
    z = torch.zeros(5,3,dtype = torch.long)
    print(z)

    """ 直接创建一个tensor外面需要再次套上一层中括号 """
    x = torch.tensor([[1,1,2],[5,6,7],[8,6,5]])#不能直接创建两个矩阵存在一个tensor里面
    print(x)
    print(x.size())
    print(x.shape)

    """ 函数	                            功能
    Tensor(*sizes)	                    基础构造函数
    tensor(data,)	                    类似np.array的构造函数
    ones(*sizes)	                    全1Tensor
    zeros(*sizes)	                    全0Tensor
    eye(*sizes)	                        对角线为1，其他为0
    arange(s,e,step)	                从s到e，步长为step
    linspace(s,e,steps)	                从s到e，均匀切分成steps份
    rand/randn(*sizes)	                均匀/标准分布
    normal(mean,std)/uniform(from,to)	正态分布/均匀分布
    randperm(m)	                           随机排列 """

    """ 在原有的tensor上新创建出来一个tensor new_ones new_zeros new_eye new_“tensor的类型” """
    x = x.new_ones(4,3,dtype = torch.float64)# 返回的tensor默认具有相同的torch.dtype和torch.device
    print(x)

    #_like创建一个与x一样的tensor，其会继承x的数据类型和大小，可以指定新的数据类型但是不能指定新的大小
    y = torch.randn_like(x,dtype = torch.float)#指定新的数据类型
    print(x)
    print(y)
    #y是一个与x大小一样的矩阵但是数据类型为浮点且数据性质为randn的标准正态分布

#tensor的操作
#加法操作
def test02():
    x = torch.eye(4,3)
    y = torch.ones(4,3,dtype = torch.float)
    print(x+y)
    print(torch.add(x,y))
    result = torch.zeros(4,3)
    torch.add(x,y,out = result)
    print(result)
    y.add_(x)#把x加到y上面去
    print(y)
    print(x)

#索引
def test03():
    x = torch.tensor([
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [0,0,0],
    ])
    #获取元素，与C++的二维数组类似
    #索引出来的结果与原数据共享内存，也即修改一个，另一个会跟着修改
    print(x[0])
    print(x[1])
    print(x[1][2])
    print(x[:,0])#获取某一列的元素,获取第0列的元素
    print(x[0,:])#获取某一行的元素 与x[0]等价
    y = x[:,0]
    print(y)
    y +=1
    print(y)
    print(x)#也会跟着被修改
"""     除了常用的索引选择数据之外，PyTorch还提供了一些高级的选择函数:

函数	                                            功能
index_select(input, dim, index)	        在指定维度dim上选取，比如选取某些行、某些列
masked_select(input, mask)	            例子如上，a[a>0]，使用ByteTensor进行选取
nonzero(input)	                        非0元素的下标
gather(input, dim, index)	            根据index，在dim维度上选取数据，输出的size与index一样 """



#改变形状
def test04():
    #用view()来改变Tensor的形状：
    x = torch.tensor([
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [0,0,0],
    ])
    y = torch.eye(3,3)
    y = x.view(12)
    z = x.view(3,4)
    a = x.view(-1,6)#-1虽然是无效维度，但是其可以通过其他维度退出来，所以是合法的
    print(x)
    print(y)
    print(z)
    print(a)
    print(x.size(),y.size(),z.size(),a.size())
    #注意view()返回的新Tensor与源Tensor虽然可能有不同的size，
    # 但是是共享data的，也即更改其中的一个，
    # 另外一个也会跟着改变。(顾名思义，view仅仅是改变了对这个张量的观察角度，内部数据并未改变)
    x+=1
    print(x)
    print(y)
    print(z)

#克隆
def test05():
    #先用clone创造一个副本然后再使用view。
    x = torch.tensor([
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [0,0,0],
    ])
    y = x.clone()
    z = x.clone().view(12)
    print(x)
    print(y)
    print(z)
    x-=1
    print(x)
    print(y)
    print(z)
    #另外一个常用的函数就是item(), 它可以将一个标量Tensor转换成一个Python number
    x = torch.randn(1, dtype=torch.float)
    y = x.item()
    print(x)
    print(y)

#另外，PyTorch还支持一些线性函数，这里提一下，免得用起来的时候自己造轮子，具体用法参考官方文档。如下表所示：

""" 函数	                                    功能
trace	                                对角线元素之和(矩阵的迹)
diag	                                对角线元素
triu/tril	                            矩阵的上三角/下三角，可指定偏移量
mm/bmm	                                矩阵乘法，batch的矩阵乘法
addmm/addbmm/addmv/addr/baddbmm..	    矩阵运算
t	                                    转置
dot/cross	                            内积/外积
inverse	                                求逆矩阵
svd	                                    奇异值分解
PyTorch中的Tensor支持超过一百种操作，包括转置、索引、切片、数学运算、线性代数、随机数等等，可参考官方文档。 """

#广播机制
def test06():
    x = torch.arange(1,3)
    y = torch.arange(1,4).view(3,1)
    print(x)
    print(y)
    print(x +y)
    #由于x和y分别是1行2列和3行1列的矩阵，如果要计算x + y，
    # 那么x中第一行的2个元素被广播（复制）到了第二行和第三行，
    # 而y中第一列的3个元素被广播（复制）到了第二列。
    # 如此，就可以对2个3行2列的矩阵按元素相加。

#内存的开销
def test07():
    x = torch.arange(1,4)
    y = torch.arange(2,5)
    id_before = id(y)#id函数用于查询变量の具体内存地址
    print(x)
    print(y)
    y = y+x
    print(y)
    print(id_before)
    print(id(y))
    if(id(y) == id_before):
        print("yes")
    elif(id(y) != id_before):
        print("no")
#索引操作是不会开辟新内存的，而像y = x + y这样的运算是会新开内存的，然后将y指向新内存
    x = torch.arange(3,9).view(2,3)
    y = torch.arange(2,8).view(2,3)
    id_before = id(y)
    print(x)
    print(y)
    y[:,:] = y+x#使用索引可以避免拷贝直接对原本的量进行操作，可以理解为C++的引用操作，提升效率
    print(y)
    print(id_before)
    print(id(y))
    if(id(y) == id_before):
        print("yes")
    elif(id(y) != id_before):
        print("no")
#使用add函数把out写入y中也可以达到同样的效果,不用重新拷贝数据
    x = torch.arange(4,10).view(2,3)
    y = torch.arange(1,7).view(2,3)
    id_before = id(y)
    print(x)
    print(y)
    torch.add(x,y,out = y)
    print(y)
    print(id_before)
    print(id(y))
    if(id(y) == id_before):
        print("yes")
    elif(id(y) != id_before):
        print("no")

#numpy与tensor的互相转换
def test08():
    #tensor转换为numpy
    x = torch.ones(5,3)
    y = x.numpy()
    print(x,y)
    x += 1
    print(x,y)
    y+=1
    print(x,y)
    
    #numpy转换为tensor
    import numpy as np
    a = np.ones(5)
    b = torch.from_numpy(a)
    print(a,b)
    a+=1
    print(a,b)
    b+=1
    print(a,b)
    #使用tensor函数把numpy转换为tensor，但是这种方法是拷贝数据，操作的不是同一份数据
    c = torch.tensor(a)
    a += 1
    print(a,c)
    c += 1
    print(a,c)

#tensor数据在gpu和cpu之间转换
def test09():
    x = torch.ones(5)
    if(torch.cuda.is_available()):
        device = torch.device("cuda")#gpu
        y = torch.randn_like(x,device = device)#直接创建一个在GPU上的tensor
        #用方法to()可以将Tensor在CPU和GPU（需要硬件支持）之间相互移动。
        x = x.to(device) #等价于 x= x.to("cuda")
        z = x+y
        print(z.to("cpu",torch.double))#to还可以同时更改数据类型

#test01()
#test02()
#test03()
#test04()
#test05()
#test06()
#test07()
#test08()
test09()