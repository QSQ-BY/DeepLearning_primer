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

    #前向传播函数,y = X @ w + b
    def forward(self,x):
        if(x.ndim != 2):#ndim函数表示数组维度
            raise ValueError(
                "Linear input must be a 2D array"
            )

        expected_features = self.weight.shape[0]
        received_features = x.shape[1]
        if(received_features != expected_features):
            raise ValueError(
                f"Linear expected {expected_features} input features, "
                f"but received {received_features}"
            )
        return x @ self.weight + self.bias