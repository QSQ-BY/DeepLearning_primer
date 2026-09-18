# Flatten 与离线小型 CNN 设计

## 背景与顺序调整

Conv2D 已在用户调整后的范围内完成前向、反向、公共 API 和回归验收。为了在进入 BatchNorm 前看到一条真实的卷积网络训练链路，原定于 Fashion-MNIST 阶段实现的 `Flatten` 提前到当前阶段，并在其后增加一个完全离线的小型 CNN 案例。

新的顺序为：

```text
Conv2D
-> Flatten
-> 离线小型 CNN
-> BatchNorm
-> Fashion-MNIST
```

## Flatten

`Flatten` 是无参数层，遵守现有统一层接口：

```python
forward(x) -> output
backward(grad_output) -> grad_input
parameters() -> []
gradients() -> []
```

`forward()` 保留第一个批次维，把其余维度展平：NCHW 输入 `(N, C, H, W)` 变为 `(N, C * H * W)`。它缓存原始输入形状。`backward()` 要求此前成功执行过 `forward()`，验证上游梯度形状等于前向输出形状，再把梯度恢复为原始输入形状。

测试覆盖类存在、前向形状和值、反向前置条件、错误上游梯度形状、反向恢复形状和值、空参数接口和包级公开导出。

## 离线小型 CNN

新增 `examples/train_toy_cnn.py`。脚本只依赖 NumPy 和 `mininn`，自动生成固定随机种子的 `8 x 8` 单通道图像。类别 0 为竖线，类别 1 为横线；样本加入少量噪声并划分训练集和测试集，不需要网络或外部数据文件。

模型结构固定为：

```text
Conv2D(1, 2, kernel_size=3, padding=1)
-> ReLU()
-> Flatten()
-> Linear(2 * 8 * 8, 2)
```

模型通过 `Sequential` 完成统一前向与反向传播，通过 `SoftmaxCrossEntropyLoss` 计算损失，通过 `SGD` 原地更新 Conv2D 和 Linear 的参数。脚本打印 epoch、损失、训练准确率和测试准确率。

## 验收与边界

- 用小批次测试网络输出形状为 `(N, 2)`，反向梯度恢复为 NCHW 输入形状。
- 固定随机种子下，最终损失低于初始损失的 50%。
- 测试准确率至少达到 90%。
- 完整测试集继续通过。
- `mininn` 和核心测试保持 NumPy-only。
- 不在本案例中引入 BatchNorm、真实数据下载、数据文件持久化、模型保存或性能优化。
- Conv2D 有限差分与梯度引用专门测试继续按用户要求省略，不得在报告中声称已执行。

## 后续衔接

案例通过后进入 BatchNorm 课次 3.1。Fashion-MNIST 阶段直接复用这里完成的 `Flatten`，原课次 4.1 只保留完整 Fashion-MNIST 网络的组合与形状检查，不重复实现该层。
