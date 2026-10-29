# Task 1 NumPy 神经网络框架完整教学计划

> 归档说明：本文件记录与 Codex 协作时使用的详细教学路线，项目现已完成。最终架构、实验数据和个人总结以 [`../lab_report.md`](../lab_report.md) 为准。

> **For agentic workers:** 实施本计划时使用逐课 TDD；每个复选项完成后先运行对应测试，再更新进度。本文档的默认协作方式是由 Codex 讲解并给骨架、用户逐步编写，而不是一次性生成全部实现。

**Goal:** 完成一个 NumPy-only 的教学型神经网络框架，并通过 Conv2D、BatchNorm 和 Fashion-MNIST 实验掌握完整的前向传播与反向传播。

**Architecture:** 每一层独立保存本层参数、梯度和反向传播缓存，并通过统一的显式接口组合进 `Sequential`。项目按最小训练闭环、Conv2D、Flatten 与小型 CNN、BatchNorm、Fashion-MNIST 的顺序推进；大部分功能先测试后实现，后期批次与训练脚本按用户调整直接实现。

**Tech Stack:** Python、NumPy、Python 标准库 `unittest`。

## Global Constraints

- 核心 `mininn/` 只能依赖 NumPy 和 Python 标准库。
- 核心网络层按 RED、GREEN、回归验证的顺序教学和实现；后期脚本遵循用户当次调整。
- 图像张量统一使用 NCHW，数值梯度检查统一使用 `float64`。
- 不覆盖工作区中与当前课次无关的用户修改。
- 已锁定的接口不在每次续接时重新设计。

---

> 本文档是后续教学的唯一主路线。每次继续项目时，先读取“当前进度”和对应课次，直接从第一个未完成项继续；已经锁定的接口和设计不再重新讨论。只有测试证明原设计不可行，或用户明确要求改变目标时，才修改本计划。

## 1. 项目目标

只使用 Python、NumPy 和标准库，完成一个能够显式执行前向传播、反向传播和参数更新的教学型神经网络框架，并用 Fashion-MNIST 做最终实验。

完整项目分为四个主体阶段；在 Conv2D 与 BatchNorm 之间增加一个前置扩展：

1. 基础层与最小训练闭环。
2. `Conv2D` 前向传播与反向传播；随后提前实现 `Flatten`，并完成离线小型 CNN 训练案例。
3. `BatchNorm` 的训练/推理状态、反向传播和手算确定值梯度验证。
4. Fashion-MNIST 数据处理、卷积分类实验和总结报告。

项目强调“能解释、能验证、再优化”。第一版卷积使用多重循环，不以运行速度换取难以理解的代码。

## 2. 教学协作规则

后续每一课固定使用以下流程：

1. Codex 说明本课唯一的新概念、输入输出形状和公式。
2. Codex 给出一个小测试目标；用户先写测试。
3. Codex 运行测试，确认它因目标功能尚未实现而按预期失败（RED）。
4. Codex 只给本课所需的代码骨架、变量含义和关键提示；用户填写实现。
5. Codex 检查代码并运行当前测试（GREEN）。如果失败，先解释根因，再让用户修改。
6. 当前测试通过后运行完整测试集，防止破坏旧功能。
7. Codex 用一个小例子让用户说明数据或梯度如何流动，然后进入下一课。

默认不再逐项询问设计偏好。Codex 应依据本文档推进；只有下列情况才暂停提问：

- 需要新增本文档没有授权的依赖；
- 需要改变公开接口或阶段边界；
- 用户已有修改与计划直接冲突，继续会覆盖用户代码；
- 同一个失败经过系统排查后仍无法确定应保留哪种行为。

教学过程中不一次性贴出整个阶段的最终答案。骨架应保留需要用户填写的核心表达式，但必须明确变量形状、计算目标和测试命令。

## 3. 全局技术约定

### 3.1 目录职责

```text
简单神经网络运算框架的实现/
├── mininn/
│   ├── __init__.py       # 稳定的公开导出
│   ├── layers.py         # Linear、ReLU、Conv2D、BatchNorm、Flatten
│   ├── losses.py         # SoftmaxCrossEntropyLoss
│   ├── model.py          # Sequential
│   ├── optim.py          # SGD
│   └── data.py           # IDX 图像与标签读取
├── tests/
│   ├── test_layers.py    # Linear、ReLU、Conv2D、Flatten、BatchNorm
│   ├── test_losses.py    # 损失函数
│   ├── test_training.py  # 组合、优化器与训练闭环
│   └── test_data.py      # IDX 读取与数据校验
├── examples/
│   ├── train_toy_classifier.py
│   ├── train_toy_cnn.py
│   └── train_fashion_mnist.py
└── docs/
    ├── lab_report.md
    └── AIGC/
        ├── 2026-08-23-task1-minimal-training-loop-design.md
        ├── 2026-08-23-task1-minimal-training-loop-plan.md
        └── 2026-09-02-task1-complete-teaching-plan.md
```

### 3.2 统一层接口

所有可放入 `Sequential` 的层提供：

```python
forward(x) -> output
backward(grad_output) -> grad_input
parameters() -> list[np.ndarray]
gradients() -> list[np.ndarray]
```

有参数的层必须在构造时创建参数梯度数组，`backward()` 使用 `[...]` 原地覆盖或先清零再累加，不能替换数组对象。这样，已经持有梯度引用的 `SGD` 始终读取到最新梯度。

### 3.3 数值、布局与依赖

- 参数、梯度、梯度检查统一使用 `float64`。
- 图像批次统一使用 `NCHW`：`(batch, channels, height, width)`。
- `mininn/` 不导入 PyTorch、TensorFlow、JAX、Keras 或其他深度学习框架。
- 单元测试使用标准库 `unittest`。
- 随机过程使用显式传入的 `numpy.random.Generator` 保证复现。
- 第一版不实现自动求导、公共层基类、GPU、混合精度、分组卷积、空洞卷积、动量和权重衰减。

### 3.4 固定验证命令

在 `简单神经网络运算框架的实现` 目录运行：

```powershell
python -m unittest discover -s tests -v
python examples/train_toy_classifier.py
```

依赖边界检查：

```powershell
rg -n "torch|tensorflow|keras|jax" mininn tests
```

预期没有匹配结果。

## 4. 当前进度

| 阶段 | 状态 | 当前断点 |
| --- | --- | --- |
| 第一阶段：最小训练闭环 | 已完成 | 现有 50 个相关测试通过；`Linear`、`ReLU`、损失、`Sequential`、`SGD` 已连通 |
| 第二阶段：Conv2D | 已完成（调整范围） | 75 项测试、玩具训练和依赖检查通过；按用户要求省略 Conv2D 有限差分与梯度引用专门测试 |
| 第二阶段扩展：Flatten 与小型 CNN | 实现与运行验证通过 | Flatten 前后向、公共 API 与小型 CNN 组合测试通过 |
| 第三阶段：BatchNorm | 实现与运行验证通过 | 18 项 BatchNorm 测试通过；已接入小型 CNN；概念复述尚未在本次续接中核验 |
| 第四阶段：Fashion-MNIST 与报告 | 已完成（调整范围） | 完成 IDX 读取、训练/评估脚本和 10 轮正式实验；按用户要求跳过小样本过拟合与 PyTorch 对比，最终报告已写入 `docs/lab_report.md` |

2026-09-16 续接核验：完整测试集 101 项通过；BatchNorm 测试实际位于 `tests/test_layers.py` 的 `TestBatchNorm` 中。运行 `python examples/train_toy_cnn.py`，11 轮训练后评估损失由 `0.493895` 降至 `0.060957`，训练与测试准确率均为 `100%`；全连接玩具训练最终损失 `0.013734`、准确率 `99.67%`。`rg -n "torch|tensorflow|keras|jax" mininn tests` 无匹配。以下旧课次复选框尚未逐项回填；本次只能确认当前实现与验证结果，不补记无法核实的历史 RED 过程或用户概念复述。续接从课次 4.1 开始。

2026-09-18 最终核验：正式网络使用 `392→20→10` 分类头，在 2,000/1,000 样本、batch size 32、学习率 0.05、随机种子 42 的配置下训练 10 轮。训练损失由 `1.477389` 降至 `0.372161`，最终测试准确率为 `81.20%`，最高为 `82.10%`；117 项测试全部通过，核心依赖检查无匹配。实验报告与项目日志已经完成。

2026-09-16 后续核验：用户已补齐 `TestFashionMNISTNetwork.test_backward_return_nchw_input_gradient`，检查返回梯度形状与输入 `(2, 1, 28, 28)` 一致且所有元素有限。运行 `python -m unittest discover -s tests -p test_training.py -v`，21 项通过；运行 `python -m unittest discover -s tests`，103 项通过。课次 4.1 的前后向组合检查完成，续接进入课次 4.2；尚未创建 IDX 数据读取器或相应测试。

## 5. 第一阶段：基础层与最小训练闭环

第一阶段已经完成，详细设计和历史步骤分别保存在：

- `docs/AIGC/2026-08-23-task1-minimal-training-loop-design.md`
- `docs/AIGC/2026-08-23-task1-minimal-training-loop-plan.md`

本阶段不重复执行。继续项目时以现有测试作为回归保护。

验收结果应持续满足：

- [x] `Linear` 前向、反向和有限差分梯度检查通过。
- [x] `ReLU` 前向、反向通过。
- [x] `SoftmaxCrossEntropyLoss` 数值稳定且梯度检查通过。
- [x] `Sequential` 能正向组合层并逆向传播梯度。
- [x] `SGD` 原地更新参数。
- [x] 合成三分类数据的损失下降且准确率达到既定阈值。

## 6. 第二阶段：Conv2D

### 6.1 锁定的公开接口

```python
Conv2D(
    in_channels,
    out_channels,
    kernel_size,
    stride=1,
    padding=0,
    rng=None,
)
```

本阶段所有尺寸参数只接受整数：

- `in_channels`、`out_channels`、`kernel_size`、`stride` 必须为正整数；
- `padding` 必须为非负整数；
- 布尔值虽然是 Python 的 `int` 子类，但在这里视为非法尺寸参数；
- 输入形状必须为 `(N, C_in, H, W)`；
- 权重形状为 `(C_out, C_in, K, K)`；
- 偏置形状为 `(C_out,)`；
- 权重使用标准差 `sqrt(2 / (C_in * K * K))` 的零均值正态分布初始化；
- 偏置初始化为零。

采用深度学习框架常用的互相关约定，不翻转卷积核。输出尺寸为：

```text
H_out = floor((H + 2P - K) / S) + 1
W_out = floor((W + 2P - K) / S) + 1
```

只要卷积核能在补零后的输入上至少放置一次，就允许步长不能整除剩余长度的情况；末尾放不下完整卷积核的区域自然丢弃。

### 6.2 前向传播

先通过 `np.pad` 对高和宽两侧补零，批次和通道维不补零。对每个 `n、oc、oh、ow`：

```text
h_start = oh * stride
w_start = ow * stride
window = padded_input[n, :, h_start:h_start+K, w_start:w_start+K]
output[n, oc, oh, ow] = sum(window * weight[oc]) + bias[oc]
```

`forward()` 缓存原始输入和补零输入，供 `backward()` 使用。

### 6.3 反向传播

`backward(grad_output)` 先验证其形状恰好等于最近一次前向传播的输出形状，然后将已有梯度清零。对前向传播中的同一个位置，令：

```text
g = grad_output[n, oc, oh, ow]
```

累加：

```text
grad_bias[oc] += g
grad_weight[oc] += window * g
grad_padded_input[n, :, h_start:h_start+K, w_start:w_start+K] += weight[oc] * g
```

若 `padding == 0`，直接返回 `grad_padded_input`；否则裁掉四周 padding 后返回，最终形状必须与原输入完全相同。

### 6.4 教学课次与 TDD 顺序

#### 课次 2.1：建立类和构造参数

- [x] 在 `tests/test_layers.py` 的独立 `TestConv2D` 测试类中写 `Conv2D` 类存在测试。
- [x] 运行该测试并观察到 `hasattr(layers, "Conv2D")` 为假。
- [x] 用户在 `mininn/layers.py` 中添加最小 `Conv2D` 类声明。
- [x] 运行当前测试，确认由 RED 变为 GREEN。
- [x] 添加构造函数签名、参数形状、数据类型、零偏置和可复现初始化测试。
- [x] 用户依据骨架实现构造函数，并提供顺序匹配的参数与梯度访问接口。
- [x] 运行 `test_layers.py` 和完整测试集（55 项通过）。

本课构造骨架：

```python
class Conv2D:
    def __init__(
        self,
        in_channels,
        out_channels,
        kernel_size,
        stride=1,
        padding=0,
        rng=None,
    ):
        # 1. 验证五个整数配置参数
        # 2. 创建或保存 rng
        # 3. 计算 He 初始化的 scale
        # 4. 创建 weight、bias、grad_weight、grad_bias
        # 5. 把前向缓存初始化为 None
        pass
```

#### 课次 2.2：输出尺寸与输入验证

- [x] 测试拒绝非四维输入。
- [x] 测试拒绝输入通道数不等于 `in_channels`。
- [x] 测试拒绝卷积核大于补零后输入。
- [x] 测试步长不能整除剩余长度时使用向下取整。
- [x] 用户编写输出尺寸计算和验证代码。
- [x] 运行当前文件测试；课次 2.2 共 34 项通过。

输出尺寸骨架：

```python
effective_height = input_height + 2 * self.padding
effective_width = input_width + 2 * self.padding
output_height = (effective_height - self.kernel_size) // self.stride + 1
output_width = (effective_width - self.kernel_size) // self.stride + 1
```

#### 课次 2.3：单样本、单通道前向传播

- [x] 使用全 1 卷积核和 `3 x 3` 小输入写确定值测试，并确认因前向卷积尚未实现而按预期失败。
- [x] 用户完成单批次、单输入通道、单输出通道的循环。
- [x] 检查每个窗口和输出位置是否一一对应。
- [x] 运行当前文件及完整测试集；共 66 项通过。

#### 课次 2.4：多批次、多输入和输出通道

- [x] 写两个输入通道、两个输出通道的确定值测试，并在同一测试中验证偏置只加一次。
- [x] 用户扩展循环以覆盖 `N` 和 `C_out`，输入通道在窗口乘积中统一求和。
- [x] 验证输出形状和确定值。

#### 课次 2.5：stride 与 padding

- [x] 分别为 `stride=2`、`padding=1` 写确定值测试。
- [x] 用户把起点计算和 `np.pad` 接入前向传播。
- 已按用户要求省略：`stride` 与 `padding` 同时使用的专门数值测试。
- 已按用户要求省略：原始输入不变性的专门测试。

#### 课次 2.6：反向传播前置条件和偏置梯度

- [x] 测试未调用 `forward()` 时调用 `backward()` 会抛出包含 `forward` 的 `RuntimeError`。
- [x] 测试错误 `grad_output` 形状会抛出 `ValueError`。
- [x] 用确定值上游梯度测试 `grad_bias` 等于各输出位置梯度之和。
- [x] 用户实现缓存检查、形状检查和 `grad_bias`。

#### 课次 2.7：权重梯度和输入梯度

- [x] 用最小确定值例子测试 `grad_weight`。
- [x] 用最小确定值例子测试重叠窗口产生的 `grad_input` 累加。
- [x] 用户完成三类梯度的循环累加。
- [x] 测试 padding 裁剪后的 `grad_input` 形状和值。
- 已按用户要求省略：`backward()` 原地更新梯度数组的专门测试；实现仍使用原地更新。

#### 课次 2.8：有限差分梯度检查（按用户要求省略）

本课不再加入 Conv2D 的 `weight`、`bias` 和输入有限差分测试。当前 Conv2D 反向传播以手算确定值测试覆盖偏置梯度、权重梯度、重叠输入梯度和 padding 裁剪；后续报告不得声称 Conv2D 已通过数值梯度检查。

#### 课次 2.9：公共 API 与阶段验收

- [x] 在 `mininn/__init__.py` 导出 `Conv2D`。
- [x] 测试包级属性与 `__all__` 中均包含 `Conv2D`。
- [x] 运行全部单元测试；75 项通过。
- [x] 检查核心目录没有深度学习框架依赖。
- [x] 用户能够说明一个输出梯度如何同时贡献给偏置、卷积核和输入窗口。

### 6.5 课次 2.10：Flatten

锁定接口：

```python
Flatten.forward(x) -> (N, -1)
Flatten.backward(grad_output) -> 恢复最近一次前向输入形状
Flatten.parameters() -> []
Flatten.gradients() -> []
```

- [ ] 在 `test_layers.py` 中写类存在测试并观察 RED。
- [ ] 测试 NCHW 输入按样本展平后的形状和值。
- [ ] 测试未调用 `forward()` 时拒绝 `backward()`，并测试错误梯度形状。
- [ ] 测试 `backward()` 恢复原输入形状和值。
- [ ] 用户实现 `Flatten`，加入 `mininn` 公共 API，并运行完整回归测试。

### 6.6 课次 2.11：离线小型卷积神经网络

新增 `examples/train_toy_cnn.py`。数据由程序生成，不下载文件：输入为 `8 x 8` 单通道图像，类别分别为竖线与横线，并加入固定随机种子控制的少量噪声。

模型固定为：

```text
Conv2D(1, 2, kernel_size=3, padding=1)
-> ReLU()
-> Flatten()
-> Linear(2 * 8 * 8, 2)
```

- [ ] 用小批次测试完整网络前向输出为 `(N, 2)`，反向返回 NCHW 输入梯度。
- [ ] 用户实现可复现的数据生成、训练集/测试集划分与训练循环。
- [ ] 脚本打印 epoch、损失、训练准确率和测试准确率。
- [ ] 最终损失低于初始损失的 50%，测试准确率至少达到 90%。
- [ ] 完整测试和示例运行通过后，再进入 BatchNorm 课次 3.1。

### 6.7 第二阶段及扩展验收标准

- 所有合法输入的输出形状符合公式。
- 单/多通道、单/多输出通道、stride 和 padding 的确定值测试通过。
- 参数列表与梯度列表顺序保持 `[weight, bias]`。
- Conv2D 的权重、偏置和输入梯度通过手算确定值测试；按用户要求不执行有限差分检查。
- `Flatten` 前后向正确，并能把 Conv2D 输出接入 Linear。
- 离线小型 CNN 的损失显著下降，测试准确率至少达到 90%。
- 第一阶段全部回归测试继续通过。

## 7. 第三阶段：BatchNorm

### 7.1 锁定的公开接口

```python
BatchNorm(num_features, momentum=0.9, epsilon=1e-5)
```

公开方法：

```python
forward(x) -> output
backward(grad_output) -> grad_input
train() -> None
eval() -> None
parameters() -> [gamma, beta]
gradients() -> [grad_gamma, grad_beta]
```

固定行为：

- 支持二维 `(N, C)` 和四维 `(N, C, H, W)` 输入；`C == num_features`。
- `gamma` 初始化为 1，`beta` 初始化为 0。
- `running_mean` 初始化为 0，`running_var` 初始化为 1。
- 默认处于训练模式。
- 二维输入沿轴 `(0,)` 统计；四维输入沿轴 `(0, 2, 3)` 统计。
- 方差使用总体方差，即 `ddof=0`。
- 训练时更新：`running = momentum * running + (1 - momentum) * batch_stat`。
- 推理时只使用运行均值和运行方差，不修改它们。
- 只有训练模式的前向传播能够建立反向传播缓存；在推理前向后调用 `backward()` 应抛出 `RuntimeError`。

训练前向公式：

```text
mean = reduce_mean(x)
variance = reduce_mean((x - mean)^2)
x_hat = (x - mean) / sqrt(variance + epsilon)
output = gamma * x_hat + beta
```

反向传播采用便于检查的合并公式。令每个通道参与统计的元素数为 `M`：

```text
dx_hat = grad_output * gamma
grad_input = inv_std / M * (
    M * dx_hat
    - sum(dx_hat)
    - x_hat * sum(dx_hat * x_hat)
)
grad_gamma = sum(grad_output * x_hat)
grad_beta = sum(grad_output)
```

所有求和都沿该输入布局对应的统计轴执行。

### 7.2 教学课次与 TDD 顺序

#### 课次 3.1：参数和模式状态

- [ ] 创建 `tests/test_batchnorm.py`，先写类存在测试并观察 RED。
- [ ] 添加最小类声明并观察 GREEN。
- [ ] 测试 `gamma`、`beta`、运行统计量和梯度数组的形状及初值。
- [ ] 测试默认训练模式以及 `train()`、`eval()` 切换。
- [ ] 用户依据骨架实现构造与状态切换。

#### 课次 3.2：二维训练前向传播

- [ ] 写小矩阵确定值测试。
- [ ] 测试归一化后各通道均值约为 0、方差约为 1。
- [ ] 用户实现二维统计轴和广播形状。
- [ ] 测试 `gamma`、`beta` 的缩放和平移。

#### 课次 3.3：四维训练前向传播

- [ ] 写 NCHW 输入测试，确认每个通道跨 `N、H、W` 统计。
- [ ] 用户扩展统计轴与参数广播，不复制二维算法。
- [ ] 测试错误维数和错误通道数。

#### 课次 3.4：运行统计与推理前向传播

- [ ] 固定两批数据，确定值测试运行均值和运行方差更新。
- [ ] 切换到 `eval()`，验证输出使用运行统计。
- [ ] 验证推理不会修改运行统计。
- [ ] 用户实现训练/推理分支。

#### 课次 3.5：参数梯度

- [ ] 写 `grad_beta` 等于上游梯度求和的测试。
- [ ] 写 `grad_gamma` 等于 `grad_output * x_hat` 求和的测试。
- [ ] 用户实现并原地覆盖两组参数梯度。

#### 课次 3.6：输入梯度

- [ ] 用二维小矩阵写确定值或性质测试。
- [ ] 用户按合并公式实现 `grad_input`。
- [ ] 扩展到 NCHW，并验证返回形状不变。
- [ ] 测试未完成训练前向传播时拒绝反向传播。

#### 课次 3.7：阶段验收（按用户要求省略有限差分）

按用户要求，不再添加或执行 BatchNorm 输入、`gamma` 和 `beta` 的有限差分测试。保留二维和 NCHW 的手算确定值梯度测试及异常调用测试；后续报告不得声称 BatchNorm 已通过数值梯度检查。

按用户要求，省略 `test_batchnorm_parameters_update_through_sgd` 专门测试。后续通过接入 BatchNorm 的离线小型 CNN 示例观察组合训练和推理行为，继续采用讲解、用户编写、运行检查的教学方式。

- [ ] 在 `mininn/__init__.py` 导出 `BatchNorm`。
- [ ] 运行完整测试集和依赖检查。
- [ ] 用户能够解释训练统计、运行统计与可训练参数的区别。

### 7.3 第三阶段验收标准

- 二维和 NCHW 输入的训练前向结果正确。
- 运行统计更新及推理模式结果正确，推理不污染状态。
- `gamma`、`beta` 和输入梯度通过手算确定值测试；按用户要求不执行有限差分检查。
- `BatchNorm` 能与 `Conv2D`、`ReLU`、`Sequential` 和 `SGD` 组合。
- 前两阶段全部回归测试继续通过。

## 8. 第四阶段：Fashion-MNIST 与报告

### 8.1 阶段边界

核心 `mininn` 仍只依赖 NumPy。Fashion-MNIST 数据文件采用 IDX 格式读取；下载可以使用 Python 标准库，但单元测试使用临时构造的小型 IDX 数据，不依赖网络。按用户最终调整，本阶段不再加入 PyTorch 对比。

本阶段复用在第二阶段扩展中已经完成的无参数 `Flatten`：

```python
Flatten.forward(x) -> (N, -1)
Flatten.backward(grad_output) -> 原输入形状
```

最终教学模型固定为：

```text
Conv2D(1, 4, kernel_size=3, stride=2, padding=1)
-> BatchNorm(4)
-> ReLU()
-> Conv2D(4, 8, kernel_size=3, stride=2, padding=1)
-> BatchNorm(8)
-> ReLU()
-> Flatten()
-> Linear(8 * 7 * 7, 20)
-> BatchNorm(20)
-> ReLU()
-> Linear(20, 10)
```

训练采用固定随机种子、打乱后的小批量 SGD。最终可复现实验使用 2,000 个训练样本、1,000 个测试样本、批大小 32、学习率 0.05、10 个 epoch。

### 8.2 教学课次与 TDD 顺序

#### 课次 4.1：Fashion-MNIST 卷积网络组合检查

- [x] 复用第二阶段扩展完成的 `Flatten`，不重复实现。
- [x] 用随机小批次验证完整 Fashion-MNIST 模型输出形状为 `(N, 10)`。
- [x] 验证完整网络反向传播能恢复 `(N, 1, 28, 28)` 输入梯度形状。

#### 课次 4.2：IDX 数据读取

- [x] 新建 `mininn/data.py`，接口固定为 `load_idx_images(path)` 和 `load_idx_labels(path)`。
- [x] 用 `tempfile` 和 `struct.pack` 生成极小合法 IDX 文件并先写失败测试（本次观察范围见下方核验记录）。
- [x] 测试魔数、数据长度和图像/标签样本数不一致时给出清晰错误。
- [x] 用户实现 gzip/普通文件读取、头部解析和 NumPy 数组转换。
- [x] 图像转换为 `(N, 1, 28, 28)` 的 `float64`，数值缩放到 `[0, 1]`；标签为一维整数数组。

本次续接核验：普通文件及 gzip 图像/标签读取、图像归一化和 NCHW 形状、文件头与魔数检查、数据长度检查均已通过测试。`examples/train_fashion_mnist.py` 的内部函数 `_load_dataset(image_path, label_path)` 已验证正常返回及拒绝图像/标签样本数不一致。运行 `python -m unittest discover -s tests -p test_data.py -v`，13 项通过；完整回归 116 项通过；`rg -n "torch|tensorflow|keras|jax" mininn tests` 无匹配。续接期间实际观察到标签正常读取、图像/标签 gzip 读取及样本数不匹配测试在功能缺失时失败；首次图像正常读取的历史 RED 过程未核验，不补记。用户已学习读取流程，完整流程复述仍可在后续教学中核验。

#### 课次 4.3：小批量与训练/推理切换

用户调整：移除整个 `TestBatchIndices` 测试类；批次索引生成器改为直接讲解具体实现，不再要求用户编写该类测试。此调整仅针对批次索引部分，保留其他已有测试。

- [x] 实现实验脚本内部的确定性批次索引生成器，不把数据加载职责放进模型。
- [x] 每个训练 epoch 前调用各 BatchNorm 层的 `train()`。
- [x] 评估前调用 `eval()`，评估后恢复 `train()`。
- 按用户选择跳过小样本过拟合，直接运行固定配置正式实验。

#### 课次 4.4：固定配置实验

- [x] 运行 2,000/1,000 样本配置并记录每个 epoch 的训练损失、训练准确率、测试准确率和耗时。
- [x] 最终训练损失低于首个 epoch，最终测试准确率为 `81.20%`，达到至少 70% 的要求。
- [x] 保存随机种子、Python/NumPy 版本、数据规模和超参数。
- [x] Fashion-MNIST 数据位于 Git 忽略的 `.build/`，未加入版本控制。

#### 课次 4.5：最终报告

- [x] 在 `docs/lab_report.md` 写最终实验报告，包含架构、实现、个人感受、测试方法、实验配置、结果和局限性。
- [x] 报告只记录实际运行命令和输出，不写未执行的结果。
- [x] 说明朴素循环卷积的复杂度以及 `im2col`、向量化或编译扩展方向。
- [x] 更新仓库根 `README.md` 的当前进度、目录和运行方法。
- [x] 运行完整测试、玩具训练、Fashion-MNIST 实验和依赖边界检查。

### 8.3 第四阶段验收标准

- `Flatten` 前后向正确，卷积网络能输出十分类 logits。
- IDX 读取器有离线单元测试，核心测试不依赖网络。
- 小批量训练链路可复现，损失下降，固定测试子集准确率至少 70%。
- 报告中的版本、耗时、损失和准确率均来自实际运行记录。
- 核心库保持 NumPy-only，完整回归测试通过。

## 9. 每次续接项目的固定操作

以后收到“继续完成项目”时，Codex 按以下顺序工作：

1. 读取本文件的“当前进度”。
2. 查看 `git status`，区分用户已有修改和计划内修改，绝不覆盖无关工作。
3. 运行当前阶段的目标测试，确认真实断点。
4. 找到第一个未勾选课次，说明本课概念并给出下一小步。
5. 用户写代码后，Codex检查、运行测试并给修正建议。
6. 一课完成后更新复选框和当前断点。
7. 一个阶段完成后运行该阶段验收命令，再进入下一阶段，不重新设计已经锁定的内容。

## 10. 最终完成定义

只有同时满足以下条件，整个 Task 1 才算完成：

- 四个阶段的复选项和验收标准全部完成；
- 所有单元测试通过且没有引入深度学习库到核心框架；
- 全连接玩具分类、小型 CNN 和 Fashion-MNIST 实验都能从文档命令复现；
- BatchNorm 和 Conv2D 按用户调整后的范围使用手算确定值验证，不执行有限差分检查；
- 最终报告能够说明前向传播、链式法则、参数更新、卷积窗口梯度累加以及 BatchNorm 的训练/推理差异，并如实记录仍需提示的部分；
- 最终报告中的所有数据均有对应的实际运行证据。
