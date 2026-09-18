from pathlib import Path
import sys
import numpy as np
PROJECT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0,str(PROJECT_DIR))

from mininn import (
    Conv2D,
    Flatten,
    Linear,
    ReLU,
    SGD,
    Sequential,
    SoftmaxCrossEntropyLoss,
    BatchNorm,
)

def make_dataset(rng,samples_per_class = 50,noise_std = 0.1):
    #100张图片，前50个竖线，后50个横线
    images = np.zeros(
        ((samples_per_class*2),1,8,8),
        dtype = np.float64,
    )

    #类别0:竖线
    images[:samples_per_class,0,:,3:5] = 1.0

    #类别1:横线
    images[samples_per_class:,0,3:5,:] = 1.0

    noise = rng.normal(
        loc = 0.0,
        scale = noise_std,
        size = images.shape,
    )
    images += noise
    #100个样本，前50个0，后50个1
    labels = np.repeat(
        np.arange(2),
        samples_per_class,
    )
    return (images,labels)

def main():
    rng = np.random.default_rng(42)
    (images,labels) = make_dataset(rng)
    #随机打乱样本
    indices = rng.permutation(images.shape[0])
    #训练规模为像本数量的百分之八十
    train_size = int(images.shape[0] * 0.8 + 0.5)

    train_indices = indices[:train_size]
    test_indices = indices[train_size:]

    train_images = images[train_indices]
    train_labels = labels[train_indices]
    test_images = images[test_indices]
    test_labels = labels[test_indices]

    print(f"train: {train_images.shape} , {train_labels.shape}")
    print(f"test: {test_images.shape} , {test_labels.shape}")

    #构建网络
    bn = BatchNorm(num_features = 2)
    network = Sequential(
        Conv2D(
            in_channels=1,
            out_channels=2,
            kernel_size=3,
            padding=1,
            rng=rng,
        ),
        bn,
        ReLU(),
        Flatten(),
        Linear(2 * 8 * 8, 2, rng=rng),
    )
    loss_function = SoftmaxCrossEntropyLoss()
    optimizer = SGD(
        network.parameters(),
        network.gradients(),
        learning_rate=0.05,
    )
    #train_images (80, 1, 8, 8)
    #→ network
    #train_logits (80, 2)
    #→ SoftmaxCrossEntropyLoss
    #标量损失
    bn.eval()
    train_logits = network.forward(train_images)
    initial_loss = loss_function.forward(
        train_logits,
        train_labels,
    )
    initial_accuracy = np.mean(
        np.argmax(train_logits,axis = 1) == train_labels
    )
    print(
        f"initial loss={initial_loss:.6f} "
        f"train_accuracy={initial_accuracy:.2%}"
    )

    #训练循环
    #forward
    #→ loss
    #→ loss.backward
    #→ network.backward
    #→ optimizer.step
    epochs = 11
    for epoch in range(epochs):
        #进行参数更新，使用训练模式
        bn.train()
        train_logits = network.forward(train_images)
        loss_value = loss_function.forward(train_logits,train_labels)

        grad_logits = loss_function.backward()
        network.backward(grad_logits)
        optimizer.step()

        # 参数更新结束，接下来只评估
        bn.eval()
        train_logits = network.forward(train_images)
        current_loss = loss_function.forward(train_logits,train_labels)
        train_accuracy = np.mean(
            np.argmax(train_logits,axis = 1) == train_labels
        )

        test_logits = network.forward(test_images)
        test_accuracy = np.mean(
            np.argmax(test_logits,axis = 1) == test_labels
        )

        print(
            f"epoch = {epoch:3d} "
            f"loss = {current_loss:.6f} "
            f"train_accuracy = {train_accuracy:.2%} "
            f"test_accuracy = {test_accuracy:.2%}"
        )

if __name__ == "__main__":
    main()