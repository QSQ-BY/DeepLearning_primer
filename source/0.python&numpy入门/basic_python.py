#变量
a=1#声明一个变量名为a的变量
a = 3.14
a = True#布尔值头大写
print(a)
a = "Hello\nWorld"#字符串，python没有字符变量
a = """

1
2
3
Hello World

4


"""#多行字符串
print(a)
a=[1,2,3]#列表list
a =(1,2,3)#元组tuple
a={1,2,3}#集合set
a = {
    "name":"Mike",
    "age":18
}
#字典dict，相当于C++中的map
#区间
x = range(5)#for(int i=0;i<5;i++)
x = range(2,5)#for(int i=2;i<5;i++)
x = range(0,5,2)#for(int i=0;i<5;i+=2)
x = range(5,0,-1)#for(int i=5;i>0;i--) 
#空
x = None#x=NULL
#变量的类型转换
x = 1
x = float(x)#变为浮点数
x = str(x)#变为字符串
x = bool(x)#转为布尔值，任何变量都可以转换为布尔值
#特殊赋值方式
x,y = 1,2#等价于x=1,y=2
x,y = y,x#快速交换变量的值
x,*y = 1,2,3,4#用*号给一个变量赋多个值x=1 y=[2,3,4]列表
x,*y,z = 1,2,3,4#x=1,z = 4,y=[2,3]


#运算符
#除法运算
x = 2
y = 1
result = y/x#会保留小数点，结果为0.5
result = y//x#与C相同
#逻辑运算符
x and y#与
x or y#或
not x#非
y = [1,2,3]
x in y#x属于y
x not in y#x不属于y
y = 2
x is y#地址相同
x is not y#地址不相同

#控制语句
if (x>0):
    print("正数")
elif (x<0):
    print("负数")
else:
    pass#如果什么都不做，要写上pass，不能什么都不写
#switch_case语句
match x:
    case 0:
        pass
    case 1:
        pass
    case _:#case_相当于C中的default
        pass
#while循环
while(x!=0):
    x -=1
#for循环
n = 10
for i in range(n):
    x +=1


#函数
#C中的声明和实现可以分开，python必须写在一起
def f():
    print(x)
    return
def g():
    return 0
#默认参数
def t(x,y = 1):
    return x+y
t(x=2)#关键字参数
t(1,2)#位置参数
#变长参数
def f(*args):
    pass
def g(**kwargs):
    pass
f(1,2,3)#args是一个元组(0,1,2,3)
g(x=1,y=2,z=3)#kwargs是一个字典

#结构体与类
class Point:
    #构造函数,不需要声明成员变量，只需要在构造函数的时候进行初始化
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def add(self):
        return self.x+self.y
p = Point(1,2)
result = p.add()
print(p.x)
print(p.y)
print(p.x+p.y)
#类的继承
class Person:
    def __init__(self,name):
        self.name = name
        return
    def introduce(self):
        print(f"我是{self.name}")
        #f可以让输出的字符串打印变量或者表达式
        #否则就会直接输出我是{self.name}
class Student(Person):
    def introduce(self):
        print(f"我是学生{self.name}")#函数的重写


#迭代
x = [1,2,3]
for i in x:
    print(i)#遍历输出一个列表
#返回多个值的函数
def f():
    yield 1
    yield 2
    yield 3
for i in f():
    print(i)


#容器
#列表，与数组类似
x = [1,2,3]
print(x[0])
x.append(4)#相当于push_back
x.pop()
print(x.index(1))#获取元素的下标
a = []
for i in range(5):
    a.append(i)


#集合，与C中的集合类似不能有重复元素且有序
a = {3,4,2,1,2}
a.add(7)
print(a)
b = a.pop()#移除最小的元素并返回他
print(b)
c = a.copy()#复制一个集合
c.update({8,9})#在c中再加入两个元素
a.remove(2)#移除某个值
a.union(c)#求解交集
a.intersection(c)#求解并集
a.difference(c)#求解差集
a.issubset(c)#判断a是否是c的子集
#字典
a = {
    "name":"Mike",
    "age":18
}
print(a["age"])
a[1] = 2#和map一样添加元素
for i in a:#遍历所有的键
    pass
for i in a.values():#遍历所有的值
    pass
for key,value in a.items():#遍历所有的键值对
    pass
a.get(0,99)#同C++的at,后一位参数为默认值，键不存在返回默认值

#索引
a = "Hello"
print(f"{a[-1]}")#最后一个字符
print(f"{a[-2]}")#倒数第二个字符
#切片：截取多个元素
a = [1,2,3,4,5,6]
print(a[1:3])#下标1到2,不是下标1到3
a[1:3] = [5,6,7]
print(a)#a会变为1 5 6 7 4 5


#字符串与格式化输出
a = "world"
b = "hello"
print(a+b)
print("abcabcabc".count("abc",1,7))#统计某一个序列出现的次数，可以传入开始索引和结束索引
print("abc".count("a"))

#格式化输出
#第一种
print("Hello,{}".format("world"))
print("Hello,{}".format(a))
print("{0}{1}{2}{0}".format("x","y","z"))#0表示第一个参数，后续同理

#第二种
print("Hello,%s" % "world")#类似C,后面用%链接
print("%s %s" % ("a","b"))
print("%.2f" % (3.1415926))

#第三种(推荐)
name = "steve"
x = f"Hello,{name}"
pi = 3.1415
print(f"{pi:.2f}")

y = len(name)#获取长度
print("Hello,World".find("world",0,10))#查找字符串
"hello".replace("l","x",2)#把2个l换成x

#内存管理
def f(x):
    x = 1
a=0
f(a)
print(a)#输出为0,不会修改原来的值
def f(x):
    x.append(0)
a = []
f(a)
print(a)#输出“[0]”

#输入
a = int(input())
b= float(input())#需要对输入的变量进行类型转换