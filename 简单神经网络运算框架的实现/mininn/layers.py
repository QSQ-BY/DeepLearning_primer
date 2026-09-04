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

class Conv2D:
    #输入通道数，输出通道数，卷积核大小，卷积步长，填充，随机数生成器
    def __init__(self,in_channels,out_channels,kernel_size,stride = 1,padding = 0,rng = None):
        #检查传入的参数是否都为整数
        configuration = {
            "in_channels":in_channels,
            "out_channels":out_channels,
            "kernel_size":kernel_size,
            "stride":stride,
            "padding":padding,
        }
        for parameter_name,value in configuration.items():
            #isinstance() 是 Python 的类型检查函数，
            #用来判断一个对象是否属于指定类型，或者指定类型的子类
            #如果是指定的类型就返回True否则返回False
            #因为布尔值是int的子类所以传入True或者False,isinstance(value,int)
            #都会返回True，所以后面要额外判断是否是布尔值
            if not isinstance(value,int) or isinstance(value,bool):
                raise ValueError(
                    f"{parameter_name} must be an intrger"
                )

        #检查输入、输出的通道数、卷积核大小和步长是否大于0
        if (out_channels <= 0):
            raise ValueError(
                "out_channels must be a positive integer"
            )
        if (in_channels <= 0):
            raise ValueError(
                "in_channels must be a positive integer"
            )
        if (kernel_size <= 0):
            raise ValueError(
                "kernel_size must be a positive integer"
            )
        if(stride <= 0):
            raise ValueError(
                "stride must be a positive integer"
            )
        #检查填充是否非负
        if(padding < 0):
            raise ValueError(
                "padding must be a positive integer or zero"
            )

        #存入卷积各项配置
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size
        self.stride = stride
        self.padding = padding
        self.__input = None#缓存前向传播的结果
        self.__padded_input = None
        self.__output_shape = None

        #没有传入生成器就创建默认生成器
        if(rng is None):
            rng = np.random.default_rng()
        #初始化各种参数
        fan_in = in_channels*kernel_size*kernel_size
        scale = np.sqrt(2.0 / fan_in)
        #初始化卷积核
        self.weight = rng.normal(loc = 0.0,scale = scale,size = (out_channels,in_channels,kernel_size,kernel_size)).astype(np.float64)
        self.bias = np.zeros(out_channels,dtype = np.float64)
        self.grad_weight = np.zeros_like(self.weight)
        self.grad_bias = np.zeros_like(self.bias)

    def parameters(self):
        return [self.weight,self.bias]

    def gradients(self):
        return [self.grad_weight,self.grad_bias]

    def forward(self,x):
        #输入应该为：batch_size,通道数，高度，宽度 四个维度
        x = np.asarray(x)
        if(x.ndim != 4):
            raise ValueError(
                "Conv2D input must be a 4D NCHW array"
            )

        #检查传入的通道数是否合法
        received_channels = x.shape[1]
        if(received_channels != self.in_channels):
            raise ValueError(
                f"Conv2D expected {self.in_channels} input channels, "
                f"but received {received_channels}"
            )

        #检查卷积核的尺寸是否已经超过了输入的长宽
        input_height = x.shape[2]
        input_width = x.shape[3]
        padded_height = input_height + 2*self.padding
        padded_width = input_width + 2*self.padding
        if(padded_height < self.kernel_size or padded_width<self.kernel_size):
            raise ValueError(
                f"Conv2D kernel_size {self.kernel_size} "
                f"is larger than padded input size "
                f"({padded_height}, {padded_width})"
            )

        self.__input = x#检查结束后缓存最新的输入

        #输入形状：
        #(N, C_in, H, W)
        #输出形状：
        #(N, C_out, H_out, W_out)
        #H_out = floor((H + 2P - K) / S) + 1
        #W_out = floor((W + 2P - K) / S) + 1
        #H：输入高度
        #W：输入宽度
        #P：padding，扩展的圈数
        #K：kernel_size，卷积核大小
        #S：stride，步长
        #剩余空间不足一次完整移动时，不能把卷积核的一部分放到输入外面
        #所以要进行向下取整
        batch_size = x.shape[0]
        output_height = (padded_height - self.kernel_size)//self.stride + 1
        output_width = (padded_width - self.kernel_size)//self.stride + 1
        output = np.zeros(
            (
                batch_size,
                self.out_channels,
                output_height,
                output_width,
            ),
            dtype = np.float64
        )
        self.__output_shape = output.shape#缓存输出的形状

        #进行填充
        padded_x = np.pad(
            x,
            #用 pad_width 明确表示：只填充 H 和 W。
            pad_width = (
                (0,0),#N:样本数量维度不进行填充
                (0,0),#C:通道维度前卫不进行填充
                (self.padding,self.padding),#H:上面和下面各填充padding行
                (self.padding,self.padding),#W:左边和右边各填充padding列
            ),
            mode = "constant",
            constant_values = 0,
        )

        self.__padded_input = padded_x#缓存扩展后的输入


        #每个样本 n
        #└── 每个输出通道 oc
        #    └── 每个输出行 oh
        #        └── 每个输出列 ow
        for batch_index in range(batch_size):
            for output_channel in range(self.out_channels):
                for output_row in range(output_height):
                    for output_column in range(output_width):
                        row_start = output_row * self.stride
                        row_end = row_start + self.kernel_size
                        column_start = output_column * self.stride
                        column_end = column_start + self.kernel_size
                        # 从输入中截取卷积核当前覆盖的窗口
                        input_window = padded_x[batch_index,:,row_start:row_end,column_start:column_end]

                        # 取出对应的输出通道的卷积核
                        kernel = self.weight[output_channel]

                        #进行卷积的计算
                        output[batch_index,output_channel,output_row,output_column] = (np.sum(kernel * input_window) + self.bias[output_channel])
        return output

    #偏置梯度：   上游梯度
    #权重梯度：   输入窗口 × 上游梯度
    #输入梯度：   卷积核 × 上游梯度
    def backward(self,grad_output):
        if(self.__input is None or
            self.__padded_input is None or
            self.__output_shape is None ):
            raise RuntimeError(
                "Conv2D.backward should requires forward() first"
            )
        #把输入转换为numpy数组
        grad_output = np.asarray(grad_output)
        #检查形状是否一致
        expected_shape = self.__output_shape
        actual_shape = grad_output.shape
        if(actual_shape != expected_shape):
            raise ValueError(
                f"Conv2D expected grad_output shape {expected_shape}, "
                f"but received {actual_shape}"
            )

        #计算偏置的导数
        #把每一个样本的所有计算值相加，只保留通道维度
        #axis 0 → N，样本
        #axis 1 → C_out，输出通道
        #axis 2 → H_out，输出高度
        #axis 3 → W_out，输出宽度
        self.grad_bias[...] = grad_output.sum(axis = (0,2,3))

        #计算卷积核的导数与输入变量的导数
        self.grad_weight[...] = 0.0
        grad_padded_input = np.zeros_like(self.__padded_input,dtype = np.float64)
        #就是把前向传播的窗口再提取出来做一次卷积
        batch_size = grad_output.shape[0]
        output_height = grad_output.shape[2]
        output_width = grad_output.shape[3]
        for batch_index in range(batch_size):
            for output_channel in range(grad_output.shape[1]):
                for output_row in range(output_height):
                    for output_column in range(output_width):
                        row_start = output_row*self.stride
                        row_end = row_start + self.kernel_size
                        column_start = output_column*self.stride
                        column_end = column_start + self.kernel_size
                        input_window = self.__padded_input[
                            batch_index,
                            :,
                            row_start:row_end,
                            column_start:column_end,
                        ]
                        gradient = grad_output[
                            batch_index,
                            output_channel,
                            output_row,
                            output_column,
                        ]
                        self.grad_weight[output_channel] += input_window * gradient
                        grad_padded_input[
                            batch_index,
                            :,
                            row_start:row_end,
                            column_start:column_end,
                        ] += self.weight[output_channel] * gradient

        if(self.padding == 0):
            return grad_padded_input
        return grad_padded_input[
            :,
            :,
            self.padding:-self.padding,
            self.padding:-self.padding,
        ]
    #:                              所有样本
    #:                              所有输入通道
    #padding:-padding               裁掉顶部和底部
    #padding:-padding               裁掉左侧和右侧

class Flatten:
    def __init__(self):
        self.__input_shape = None
        self.__output_shape = None

    def forward(self,x):
        x = np.asarray(x)
        batch_size = x.shape[0]
        output = x.reshape(batch_size,-1)
        self.__input_shape = x.shape
        self.__output_shape = output.shape
        return output

    def backward(self,grad_output):
        if(self.__input_shape is None or self.__output_shape is None):
            raise RuntimeError("Flatten.backward() requires forward() first")
        grad_output = np.asarray(grad_output)
        expected_shape = self.__output_shape
        actual_shape = grad_output.shape
        if actual_shape != expected_shape:
            raise ValueError(
                f"Flatten expected grad_output shape {expected_shape}, "
                f"but received {actual_shape}"
            )

        return grad_output.reshape(self.__input_shape)

    #返回空的参数层
    def parameters(self):
        return []
    def gradients(self):
        return []
