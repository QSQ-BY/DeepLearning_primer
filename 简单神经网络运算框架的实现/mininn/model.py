class Sequential:
    def __init__(self,*layers):
        if(len(layers) == 0):
            raise ValueError(
                "Sequential requires at least one layer"
            )
        self.layers = list(layers)

    def forward(self,x):
        #output = x：第一层接收模型输入
        #for layer in self.layers：按照保存顺序取出每一层
        #output = layer.forward(output)：上一层输出成为下一层输入
        #return output：返回最后一层的结果
        output = x
        for layer in self.layers:
            output = layer.forward(output)

        return output

    def backward(self,grad_output):
        gradient = grad_output
        #反向对每一层进行遍历
        for layer_index in range(len(self.layers)-1,-1,-1):
            layer = self.layers[layer_index]
            gradient = layer.backward(gradient)
        return gradient

    def parameters(self):
        parameters = []
        #遍历 Sequential 中的每一层
        #→ 调用当前层的 parameters()
        #→ 遍历该层返回的参数列表
        #→ 把参数逐个加入汇总列表
        for layer in self.layers:
            layer_parameters = layer.parameters()
            for parameter in layer_parameters:
                parameters.append(parameter)
        return parameters

    def gradients(self):
        gradients = []
        #遍历每一层
        #→ 获取该层的梯度列表
        #→ 将梯度数组逐个加入汇总列表
        #→ 返回完整梯度列表
        for layer in self.layers:
            layer_gradients = layer.gradients()
            for gradient in layer_gradients:
                gradients.append(gradient)
        return gradients
