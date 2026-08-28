import numpy as np
class SoftmaxCrossEntropyLoss:
    #对向前传播的结果进行缓存
    def __init__(self):
        self.__probabilities = None
        self.__labels = None

    def forward(self,logits,labels):
        logits = np.asarray(logits)
        labels = np.asarray(labels)
        #检查logits和labels的维度
        #logits必须为2维，labels必须为1维
        if(logits.ndim != 2):
            raise ValueError(
                "logits must be a 2D array"
            )
        if(labels.ndim != 1):
            raise ValueError(
                "labels must be a 1D array"
            )

        #用于判断具体类型是否属于整数类型，而不限制它必须恰好是某一种整数宽度
        if(not np.issubdtype(labels.dtype,np.integer)):
            raise ValueError(
                "labels must contain integer class indices"
            )

        #判断样本数量是否匹配
        if labels.shape[0] != logits.shape[0]:
            raise ValueError(
                "logits and labels must have the same batch size"
            )

        #判断样本数是否为0
        if logits.shape[0] == 0:
            raise ValueError(
                "the batch must contain at least one sample"
            )

        #判断标签范围是否合法
        if(np.any(labels < 0) or np.any(labels >= logits.shape[1])):
            raise ValueError(
                "label index is outside the class range"
            )

        #具体计算流程:
        #logits
        #→ 每项取指数
        #→ 每行除以指数和，得到 Softmax 概率
        #→ 根据 labels 取出每个样本的正确类别概率
        #→ 计算 -log
        #→ 对批次求平均
        shifted_logits = logits - logits.max(
            axis=1,
            keepdims=True,
        )#对于每一行，减去该行的最大值避免造成数据超出范围，
        #相当于最后计算概率的时候上下同时除以e的max次方
        exponentials = np.exp(shifted_logits)
        #axis = 1，对每一行求和保留每一列
        sums = exponentials.sum(axis=1,keepdims = True)
        probabilities = exponentials / sums

        #缓存前向传播结果
        self.__probabilities = probabilities
        self.__labels = labels.copy()

        sample_losses = []
        for sample_index in range(logits.shape[0]):
            class_index = labels[sample_index]
            correct_shifted_logits = shifted_logits[sample_index][class_index]
            log_normalizer = np.log(sums[sample_index,0])
            sample_loss = (log_normalizer - correct_shifted_logits)
            sample_losses.append(sample_loss)
        return float(np.mean(sample_losses))

    def backward(self):
        if(self.__labels is None or self.__probabilities is None):
            raise RuntimeError(
                "SoftmaxCrossEntropyLoss.backward() "
                "requires forward() first"
            )
        gradient = self.__probabilities.copy()
        batch_size = gradient.shape[0]

        for sample_index in range(batch_size):
            correct_class = self.__labels[sample_index]
            gradient[sample_index][correct_class] -= 1.0

        gradient = gradient / batch_size
        return gradient
