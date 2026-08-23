# Task 1 基础层与最小训练闭环设计

## 目标

仅使用 Python、NumPy 和标准库，实现一个可导入的最小神经网络库。第一阶段完成全连接层、ReLU、Softmax 交叉熵、Sequential 模型容器和 SGD，并在合成分类数据上验证损失能够下降。

本阶段采用教学式协作：用户负责编写代码，Codex 先解释公式和接口、提供代码骨架并检查结果。每次只实现一个可测试行为。

## 阶段边界

完整 Task 1 分为四个阶段：

1. 基础层与最小训练闭环。
2. Conv2D 前向传播、反向传播和梯度检查。
3. BatchNorm 训练/推理状态、反向传播和梯度检查。
4. Fashion-MNIST 实验、性能对比和任务报告。

当前只实施第一阶段。自动求导、复杂基类、向量化卷积、Jupyter Notebook、深度学习库和复杂打包配置均不在本阶段范围内。

## 目录结构

```text
简单神经网络运算框架的实现/
├── mininn/
│   ├── __init__.py
│   ├── layers.py
│   ├── losses.py
│   ├── model.py
│   └── optim.py
├── tests/
│   ├── test_layers.py
│   ├── test_losses.py
│   └── test_training.py
└── examples/
    └── train_toy_classifier.py
```

各文件职责如下：

- `layers.py`：实现 `Linear` 和 `ReLU`；后续阶段再加入 `Conv2D` 和 `BatchNorm`。
- `losses.py`：实现数值稳定的 `SoftmaxCrossEntropyLoss`。
- `model.py`：实现按顺序组合层的 `Sequential`。
- `optim.py`：实现最小 SGD 参数更新器。
- `tests/`：保存确定值测试、梯度检查和训练闭环测试。
- `examples/`：展示如何使用库训练模型，不承载层或优化器的内部逻辑。

## 层接口

普通层遵循以下接口：

```text
forward(input) -> output
backward(grad_output) -> grad_input
parameters() -> list[numpy.ndarray]
gradients() -> list[numpy.ndarray]
```

不要求所有层继承共同基类，只要求行为一致。

### Linear

`Linear(in_features, out_features, rng=None)` 保存 `weight`、`bias`、`grad_weight` 和 `grad_bias`。`weight` 形状为 `(in_features, out_features)`，使用标准差 `sqrt(2 / in_features)` 的零均值正态分布初始化；`bias` 初始化为零。参数和梯度使用 `float64`。可选的 NumPy `Generator` 用于可复现初始化。

- `forward(x)` 计算 `x @ weight + bias`，并缓存输入 `x`。
- `backward(grad_output)` 计算：
  - `grad_input = grad_output @ weight.T`
  - `grad_weight = x.T @ grad_output`
  - `grad_bias = grad_output.sum(axis=0)`
- `parameters()` 按 `[weight, bias]` 的顺序返回参数。
- `gradients()` 按 `[grad_weight, grad_bias]` 的顺序返回梯度。

`grad_weight` 和 `grad_bias` 在构造时分配为零数组，`backward()` 使用切片原地覆盖其中的值。这样，优化器在构造时保存的梯度引用始终有效。

第一阶段的 `Linear` 只接受二维批量输入 `(batch_size, in_features)`，不自动展平高维输入。

### ReLU

- `forward(x)` 计算 `maximum(0, x)`，并缓存 `x > 0` 的布尔掩码。
- `backward(grad_output)` 将非正输入位置的梯度置零。
- `parameters()` 和 `gradients()` 返回空列表。

输入恰好等于零时，导数约定为零。

## 损失函数接口

`SoftmaxCrossEntropyLoss` 使用以下接口：

```text
forward(logits, labels) -> float
backward() -> grad_logits
```

- `logits` 形状为 `(batch_size, num_classes)`。
- `labels` 形状为 `(batch_size,)`，保存整数类别编号。
- 前向传播先从每行 logits 中减去该行最大值，再计算 softmax；损失值通过 log-sum-exp 形式直接从平移后的 logits 计算，不对可能下溢为零的概率取对数。
- 前向传播缓存概率和标签。
- 反向传播返回 `(probabilities - one_hot_labels) / batch_size`。

损失函数与 softmax 合并实现，避免对极小概率直接取对数造成数值不稳定。

## 模型与优化器接口

`Sequential(*layers)` 保存有序层列表：

- `forward(x)` 按正序调用各层的 `forward()`。
- `backward(grad_output)` 按逆序调用各层的 `backward()`。
- `parameters()` 和 `gradients()` 分别汇总所有层的参数与梯度，保持二者顺序一致。

`SGD(parameters, gradients, learning_rate)` 保存参数列表、梯度列表和学习率。`step()` 对每一对参数和梯度原地执行：

```text
parameter -= learning_rate * gradient
```

第一阶段不实现动量、权重衰减、学习率调度和梯度清零。每次 `backward()` 直接覆盖对应梯度，不累加梯度。

## 训练数据流

最小训练循环遵循以下顺序：

```text
logits = model.forward(x)
loss_value = loss.forward(logits, labels)
grad_logits = loss.backward()
model.backward(grad_logits)
optimizer.step()
```

训练示例使用二维三分类合成数据和以下模型。数据由三个各含 100 个样本的高斯簇组成，中心分别为 `(-1, -1)`、`(1, -1)` 和 `(0, 1)`，每一维标准差为 `0.35`：

```text
Linear(2, 16) -> ReLU -> Linear(16, 3)
```

示例固定 NumPy 随机种子，使训练结果可以复现。

## 错误处理

- `Linear.forward(x)` 在输入不是二维数组或第二维不等于 `in_features` 时抛出 `ValueError`。
- 层或损失函数在尚未完成对应前向传播时调用 `backward()`，抛出 `RuntimeError`。
- 损失函数在 logits 不是二维数组、labels 不是一维整数数组、样本数不一致或类别编号越界时抛出 `ValueError`。
- `SGD` 在参数和梯度数量不一致，或对应形状不一致时抛出 `ValueError`。
- 框架不自动展平、广播标签或纠正错误形状，避免隐藏调用错误。

## 测试策略

测试使用 Python 标准库 `unittest`，运行命令为：

```powershell
python -m unittest discover -s "简单神经网络运算框架的实现/tests" -v
```

开发严格遵循 Red-Green-Refactor：

1. 先写一个描述目标行为的测试。
2. 运行并确认测试因为功能缺失而按预期失败。
3. 编写让该测试通过的最少实现。
4. 重新运行当前测试和完整测试集。
5. 仅在测试全部通过后整理命名与重复代码。

测试分为三层：

- 确定值测试：使用小矩阵验证 `Linear`、`ReLU` 和损失函数的前向、反向结果。
- 数值梯度检查：使用中心差分验证 `Linear` 与 `SoftmaxCrossEntropyLoss` 的解析梯度。
- 训练闭环测试：固定随机种子，训练合成分类数据并验证最终损失显著低于初始损失。

数值梯度检查使用 `float64` 和相对误差，默认通过标准为相对误差小于 `1e-6`。

## 第一阶段验收标准

- `简单神经网络运算框架的实现/mininn` 能作为普通 Python 包导入。
- Task 1 目录中不导入 PyTorch、TensorFlow 或其他深度学习库。
- `Linear`、`ReLU`、`SoftmaxCrossEntropyLoss`、`Sequential` 和 `SGD` 均通过确定值测试。
- `Linear` 和损失函数通过有限差分梯度检查。
- 合成三分类模型的最终损失低于初始损失的 50%，且训练准确率至少达到 85%。
- 所有测试可由一条 `unittest discover` 命令重复运行。
- 用户能够解释一次训练迭代中数据和梯度经过各组件的顺序。
