import numpy as np

class Linear:
    def __init__(self,in_features,out_features,rng = None):
        #self：当前创建的 Linear 对象，由 Python 自动传入。
        #in_features：输入特征数。
        #out_features：输出特征数。
        #rng=None：可选随机数生成器，暂时不用。
        if(rng is None):
            rng = np.random.default_rng()
            #如果没有传入生成器就自己创建，生成器的种子为python自己的随机熵

        scale = np.sqrt(2.0 / in_features)
        ##loc = 0.0正态分布的均值为0
        #scale：正态分布的标准差
        #这里使用：sqrt(2.0 / in_features)
        #这是适合 ReLU 网络的 He 初始化。
        #它根据输入特征数控制权重大小，
        #避免网络变深后数值迅速变得过大或过小。
        self.weight = rng.normal(
            loc = 0.0,
            scale = scale,
            size = (in_features,out_features),
        ).astype(np.float64)
        self.bias = np.zeros((out_features),dtype = np.float64,)
        self.grad_weight = np.zeros_like(self.weight)
        self.grad_bias = np.zeros_like(self.bias)
        self.__input = None#创建时还没有任何的输入

    #前向传播函数,y = X @ w + b
    def forward(self,x):
        #检查输入是否是二维
        if(x.ndim != 2):#ndim函数表示数组维度
            raise ValueError(
                "Linear input must be a 2D array"
            )

        #检查输入输出的形状是否匹配
        expected_features = self.weight.shape[0]
        received_features = x.shape[1]
        if(received_features != expected_features):
            raise ValueError(
                f"Linear expected {expected_features} input features, "
                f"but received {received_features}"
            )

        #必须保存X因为反向传播要计算grad_weight = X.T @ grad_output
        self.__input = x#缓存输入
        #计算并返回矩阵运算的结果
        return x @ self.weight + self.bias

    #反向传播
    def backward(self,grad_output):
        #检查在反向传播之前是否已经进行了前向传播
        if(self.__input is None):
            raise RuntimeError(
                "Linear.backward() requires forward() first"
            )

        #即使调用者传入 Python 列表，后续也能统一使用 .shape 和矩阵运算
        grad_output = np.asarray(grad_output)

        #检查矩阵的形状是否相吻合
        expected_shape = (
            self.__input.shape[0],
            self.weight.shape[1],
        )
        actual_shape = grad_output.shape
        if(actual_shape != expected_shape):
            raise ValueError(
                f"Linear Model expected grad_output shape {expected_shape},"
                f"but received {actual_shape}"
            )

        #计算梯度
        #grad_weight = X.T @ grad_output
        self.grad_weight[::] = self.__input.T @ grad_output
        #grad_bias = sum(grad_output(axis = 0))
        self.grad_bias[::] = grad_output.sum(axis = 0)
        return grad_output @ self.weight.T
        #grad_input = grad_ouput @ W.T（数学推导得出）

    #把参数和其所对应的梯度打包成可迭代容器
    def parameters(self):
        return [self.weight,self.bias]
    def gradients(self):
        return [self.grad_weight,self.grad_bias]

class ReLU:
    def __init__(self):
        self.__positive_mask = None

    def forward(self,x):
        x = np.asarray(x)
        self.__positive_mask = x>0#正值掩码，一个布尔类型矩阵
        return np.maximum(0,x)

    def backward(self,grad_output):
        if(self.__positive_mask is None):
            raise RuntimeError(
                "ReLU.backward() requires forward() first"
            )

        grad_output = np.asarray(grad_output)

        expected_shape = self.__positive_mask.shape
        actual_shape = grad_output.shape
        if(actual_shape != expected_shape):
            raise ValueError(
                f"ReLU expected grad_output shape {expected_shape}, "
                f"but received {actual_shape}"
            )
        #布尔值参与乘法时，False 相当于 0，True 相当于 1。
        return grad_output * self.__positive_mask

    #提供空的参数和梯度接口，后续各个层进行链接的时候
    #有参数的层返回参数数组，没参数的层返回空列表，Sequential 不需要知道当前层究竟是什么类型。
    #可以直接统一extend
    def parameters(self):
        return []
    def gradients(self):
        return []
