
from pathlib import Path
import sys

import numpy as np


PROJECT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_DIR))

from mininn import Linear, ReLU, SGD, Sequential, SoftmaxCrossEntropyLoss
#网络由 Linear(2,16)、ReLU 和 Linear(16,3) 三层组成。
#数据集包含300个样本，每个样本有两个输入特征，所以输入形状为 (300,2)。
#第一层把每个样本的两个特征映射为16个隐藏特征，输出形状为 (300,16)。
#随后ReLU将小于等于0的值变成0，引入非线性。第二个线性层再把16个隐藏特征映射为三个类别分数，
#最终输出形状为 (300,3)。每一行对应一个样本对三个类别的 logits，
#取最大分数所在的位置作为预测类别。

#logits
#-> 损失函数forward
#-> 损失函数backward
#-> Sequential.backward
#-> 第二个Linear.backward
#-> ReLU.backward
#-> 第一个Linear.backward
#-> SGD.step

def make_dataset(rng):
    centers = np.array([
        [-1.0, -1.0],
        [1.0, -1.0],
        [0.0, 1.0],
    ])
    features = np.vstack([
        rng.normal(center, 0.35, size=(100, 2))
        for center in centers
    ])
    #0到2三个标签每个标签重复100次，一共300个样本，每一个标签对应100个样本
    labels = np.repeat(np.arange(3), 100)
    return features, labels


def main():
    rng = np.random.default_rng(42)
    features, labels = make_dataset(rng)
    network = Sequential(
        Linear(2, 16, rng=rng),
        ReLU(),
        Linear(16, 3, rng=rng),
    )
    loss_function = SoftmaxCrossEntropyLoss()
    optimizer = SGD(
        network.parameters(),
        network.gradients(),
        learning_rate=0.1,
    )

    #网络先通过两个线性层和ReLU完成前向传播，得到每个样本对三个类别的预测分数。
    #Softmax交叉熵损失函数根据这些分数和真实标签计算平均损失，
    #并求出损失对 logits 的梯度。随后网络按照相反的层顺序传播梯度，
    #依次计算第二个线性层、ReLU和第一个线性层的梯度，
    #同时得到四组参数梯度 dW2、db2、dW1、db1。
    #最后，SGD沿梯度的反方向更新 W1、b1、W2、b2。重复这一过程，损失逐渐下降，
    #分类准确率逐渐提高。
    for epoch in range(301):
        logits = network.forward(features)
        loss_value = loss_function.forward(logits, labels)
        network.backward(loss_function.backward())
        optimizer.step()

        if epoch % 50 == 0:
            accuracy = np.mean(
                np.argmax(logits, axis=1) == labels
            )
            print(
                f"epoch={epoch:3d} "
                f"loss={loss_value:.6f} "
                f"accuracy={accuracy:.2%}"
            )

if __name__ == "__main__":
    main()
