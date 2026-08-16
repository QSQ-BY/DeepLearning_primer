import numpy as np
#创建整数数组
arr1 = np.array([1,2,3])
print(arr1) #输出:[1 2 3],中间没有逗号
#同化定理
arr2 = np.array([1.0,2,3])#内涵浮点则时浮点型数组
arr1[0] = 100.9#插入浮点数会被截断
arr2[1] = 10#插入后会变为浮点数
#改变类型
arr3 = arr1.astype(float)
print(arr3)
arr3 = arr2.astype(int)
print(arr3)
arr1 + 0.0
arr1*1.0
arr1/1
#以上三种方法都会把arr转换成浮点型数组,浮点型数组一般不会降级


#数组维度，维度由中括号数量决定
arr1 = [1,2,3]#一维
arr2 = [[1,2,3]]#二维
arr1 = np.ones(1)
arr2 = np.ones((1,2))
arr3 = np.ones((1,1,3))
print(f"{arr1}{arr2}{arr3}")
#把二维数组降级为一维数组
arr1 = np.arange(10).reshape(2,5)
print(arr1)
arr2 = arr1.reshape(-1)#自动推导
print(arr2)

#由列表转化为数组
arr1 = np.array([1,2,3])#创建一维向量
arr2 = np.array([[1,2,3]])#创建行矩阵
arr3 = np.array([[1],[2],[3]])#创建列矩阵
arr4 = np.array([[1,2,3],[4,5,6]])#创建二维矩阵
n,m = 3,5
arr = np.array([0]*m for _ in range(n))
print(arr)
arr = np.array([[0 for _ in range(m)] for _ in range(n)])
arr = np.arange(1,10,2)#创建递增数组，原理与range一样

#创建随机数组
arr = np.random.random((1,15))#创建大小为[1,15]的随机数组,范围默认为0到1，数据类型为浮点数
arr = np.random.randint(10,100,(1,15))#范围为1到100的随机整数数组
arr = (90*np.random.random((1,15))).astype(int) + 10#与上一行代码等价
arr = np.random.normal(10,100,(2,3))#正态分布
arr = np.random.normal(0,1,(2,3))

#数组的索引
arr1 = np.arange(1,10)#一维向量访问与列表相同
arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2[0,2])
print(arr2[1,-1])
print(arr1[[0,2]])#花式索引，取出两个元素
print(arr2[[0,1],[0,1]])#打印[0,0]和[1,1]

#切片，与张量一样，修改切片会直接修改原数组
arr1 = np.arange(10)
arr1[1:4]
arr1[1:]#从索引1开始切到结尾
arr1[:4]#从开头到3
arr1[::2]#每两个元素采集一次
arr1[1:4:2]#1到3索引，每两个元素采集一次

#矩阵操作
arr = np.arange(1,13).reshape(3,4)
arr1 = arr.T#矩阵的转置
arr1 = np.flipud(arr)#上下翻转
arr2 = np.fliplr(arr)#左右翻转
#向量的拼接
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.concatenate([arr1,arr2])#对向量进行拼接
print(arr)
#矩阵的拼接
arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[7,8,9],[1,2,3]])
arr = np.concatenate([arr1,arr2])#默认按照行进行拼接
arr = np.concatenate([arr1,arr2],axis = 1)#按照列
#广播机制
arr1 = np.arange(3).reshape(3,1)
arr2 = np.ones((3,5))
print(arr1*arr2)
arr1 = np.arange(3)
arr2 = np.arange(3).reshape(3,1)
print(arr1*arr2)

#矩阵乘法np.dot()函数，符合线性代数的运算结果
arr1 = np.arange(5)
arr2 = np.arange(5)
print(np.dot(arr1,arr2))
arr2 = np.arange(15).reshape(5,3)
print(np.dot(arr1,arr2))#乘积里混有向量则结果一定也是向量

#数学函数
#绝对值函数
arr = np.arrar([-10,2,10])
arr1 = np.abs(arr);
print(arr1)
#三角函数
theta = np.arange(3)*np.pi/3
print(np.sin(theta))
print(np.cos(theta))
print(np.tan(theta))
#指数函数
x = np.arange(1,4)
np.exp(x)#e的x次方
2**x#2的x次方
10**x#10的x次方
#对数函数
np.log(x)#lnx
np.log(x)/np.log(2)#log2x

#聚合函数
#最大最小值函数
arr = np.random.random((2,3))
np.max(arr,axis = 0)#按维度一求解最大值，最终结果长度为3
np.max(arr,axis = 1)#按维度二求最大值，最终结果长度为2
np.max(arr)#所有值
#求和函数
arr = np.arange(10).reshape(2,5)
np.sum(arr,axis = 0)#最终的结果长度为5
np.sum(arr,axis = 1)#最终结果长度为2
np.sum(arr)#整体求均值
#求均值函数
np.mean(arr,axis = 0)#与上面的函数同理
np.mean(arr,axis = 1)
np.mean(arr)
#求标准差函数std()

#布尔型数组
arr = np.arange(1,7).reshape(2,3)
print(arr>=4)
print(arr<4 | arr>6)#或用|表示
#统计个数
arr = np.random.normal(0,1,1000)
num = np.sum(np.abs(arr)<1)#统计数组中小于1的个数
#np.any()函数只要布尔型数组中含有true就返回true，遇1则1
arr1 = np.arange(1,10)
arr2 = np.fliplr(arr1)
print(np.any(arr1 == arr2))
#np.all()函数只有所有的都是true才返回true
#使用布尔型数组进行掩码筛选操作
arr1 = np.arange(12).reshape(3,4)
print(arr1[arr>4])#打印出所有大于4的值，但是整个矩阵会退化成一个向量
arr2 = np.flipud(arr1)
print(arr1[arr1>arr2])#打印出再arr1中的所有大于arr2的元素
#使用np.where()可以返回下标
arr = np.random.normal(500,70,1000)
print(np.where(arr>600))
print(np.where(arr == np.max(arr)))#找出最高分下标在哪
print(np.where(arr>600)[0])
#np.where输出的是一个元组，元组的第一个元素是下标列表，第二个元素则是数据类型
