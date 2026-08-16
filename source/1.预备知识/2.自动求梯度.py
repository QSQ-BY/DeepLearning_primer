import torch as tc
x = tc.ones(2,2,requires_grad=True)
print(x)
print(x.grad_fn)#None
#grad_fn创建该Tensor的Function, 就是说该Tensor是不是通过某些运算得到的
y = x+2
print(y)
print(y.grad_fn)#y是通过加法创建的所以拥有<AddBackward>的grad_fn
print(x.is_leaf,y.is_leaf)
#像x这种直接创建的称为叶子节点，叶子节点对应的grad_fn是None。

z = y*y*3#grad_fn=<MulBackward>
out = z.mean() #grad_fn=<MeanBackward1>
print(z,out)

out.backward()#对out进行反向传播
print(x.grad)#计算d(out)/dxi

out2 = x.sum()
out2.backward()
print(x.grad)#要与之前的梯度累加

out3 = x.sum()
x.grad.data.zero_()
print(x.grad)#结果为1

x.grad.data.zero_()
x = tc.tensor([1.0,2.0,3.0,4.0],requires_grad = True)
y = 2*x#grad_fn = <MulBackward>
z = y.view(2,2) #grad_fn=<ViewBackward>
print(y)
print(z)
""" 不允许张量对张量求导，只允许标量对张量求导，
求导结果是和自变量同形的张量。
所以必要时我们要把张量通过将所有张量的元素加权求和的方式转换为标量 """
#现在 z 不是一个标量，所以在调用backward时需要传入一个和z同形的权重向量进行加权求和得到一个标量。
v = tc.tensor([[1,2],[3,4]])
z.backward(v)
print(x.grad)#求导后为2

#中断梯度追踪，使用with代码块
x = tc.tensor([[1,2],[3,4]],dtype = tc.float,requires_grad = True)
y1 = x**2
with tc.no_grad():
    y2 = x**3#在 with 代码块中，PyTorch 暂时关闭自动梯度追踪
y3 = y1+y2
v = tc.tensor([[1,2],[3,4]])
y3.backward(v)
print(x.grad)#y3 = 2*x，y2的梯度没有被计入
""" tensor([[ 2.,  8.],
        [18., 32.]])
"""
print(x.requires_grad)
print(y1.requires_grad)
print(y2.requires_grad)#False
print(y3.requires_grad)
#此时对y2进行反向传播就会报错（y2.backward(v)）
""" 
如果我们想要修改tensor的数值，
但是又不希望被autograd记录（即不会影响反向传播），
那么我么可以对tensor.data进行操作。 """

x = tc.ones(2,2,dtype = tc.float,requires_grad = True)
print(x)
print(x.data)#二者打印结果一样
print(x.data.requires_grad)#显示False
y = x^2
#PyTorch 需要保护这个叶子张量及其计算图状态，因此禁止直接原地修改它。
#x*=100会直接禁用

#可以用以下两种方式更改tensor的值但是不计入梯度
with tc.no_grad():
    x *=2
x.data*=50
v = tc.tensor([[1,1],[1,1]])
y.backward(v)
print(x)#更改data的值会影响tensor的值
print(x.grad)