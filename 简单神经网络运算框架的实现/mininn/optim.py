class SGD:#随机梯度下降优化器
    def __init__(self,parameters,gradients,learning_rate):
        self.parameters = list(parameters)
        self.gradients = list(gradients)

        #检测参数和梯度数量是不是匹配的
        if(len(self.parameters) != len(self.gradients)):
            raise ValueError(
                "parameters and gradients must have equal counts"
            )

        #检测每一个对应的参数和梯度的形状是不是匹配的
        for parameter, gradient in zip(self.parameters,self.gradients):
            if(parameter.shape == gradient.shape):
                continue
            raise ValueError(
                "parameter shape and gradient shape should be equal"
            )

        #检测学习率是否为正数
        if(learning_rate <=0):
            raise ValueError(
                "learning_rate must be positive"
            )
        self.learning_rate = learning_rate

    def step(self):
        #向梯度的反方向更新参数
        for parameter,gradient in zip(self.parameters,self.gradients):
            parameter -= self.learning_rate * gradient
