# DeepLearning

这是我的深度学习入门学习仓库，用来保存练习代码和每日学习日志。目前最完整的子项目是一个只依赖 NumPy 和 Python 标准库的简单神经网络运算框架。

## 学习路线

目前以[《动手学习深度学习（PyTorch 版本）》](https://tangshusen.me/Dive-into-DL-PyTorch/)为主要学习资料。章节进度和代码练习会按照书中的路线推进，每天再用日志整理当天实际学到的内容。

## 当前进度

| 日期 | 章节 | 学习内容 |
| --- | --- | --- |
| 2026-08-11 | 预备知识：数据操作 | 环境搭建；Tensor 的创建、运算与索引；`view()`；广播机制 |
| 2026-08-12 | 预备知识：数据操作 | 完成本节；内存开销；Tensor 与 NumPy 转换；CPU/GPU 间移动 |
| 2026-08-14 至 2026-08-16 | Python、NumPy 与自动求梯度 | 补齐 Python、NumPy 基础；学习计算图、反向传播、梯度累加与 `no_grad()` |
| 2026-08-18 至 2026-08-20 | 深度学习基础 | 从零实现线性回归及其简洁版本；学习 Softmax 原理与 Fashion-MNIST 数据加载流程 |
| 2026-08-21 至 2026-08-23 | Softmax 与神经网络框架 | 手动实现 Softmax 分类；搭建 NumPy 神经网络框架，完成 Linear 前向传播和错误输入测试 |
| 2026-08-24 | 神经网络框架：Linear 反向传播 | 推导输入、权重和偏置梯度；补齐参数接口、错误处理与有限差分梯度检查 |
| 2026-08-25 至 2026-08-30 | 多层感知机与神经网络框架 | 实现多层感知机的手写版和简洁版；为 NumPy 框架补齐 ReLU、Softmax 交叉熵、Sequential、SGD 与最小训练闭环 |
| 2026-08-31 至 2026-09-03 | 神经网络框架：Conv2D | 从零实现支持 NCHW、多样本、多通道、步幅和填充的卷积层，并完成前向与反向传播 |
| 2026-09-04 | 神经网络框架：Flatten 与小型 CNN | 实现 Flatten 的前向与反向传播；用横线、竖线合成数据跑通离线卷积网络训练闭环 |
| 2026-09-05 至 2026-09-18 | 神经网络框架：BatchNorm 与 Fashion-MNIST | 实现批量归一化、IDX 数据读取和小批量训练；在 2,000/1,000 样本上训练十分类 CNN，最高测试准确率为 82.10% |

## NumPy 神经网络运算框架项目

[`简单神经网络运算框架的实现`](简单神经网络运算框架的实现/) 是我目前写过的代码量最大、规模也最大的学习项目。我只使用 NumPy 和 Python 标准库，手动实现各层的前向传播与反向传播，再把它们接成可以训练的网络。项目没有池化、自动求导和 GPU 支持，它的重点是把公式落实到数组形状、缓存和梯度累加上。

如果是第一次看这个项目，可以先读[实验报告](简单神经网络运算框架的实现/docs/lab_report.md)，然后运行 `examples` 中的案例，最后再进入 `mininn` 阅读具体实现。

更详细的设计过程保存在 [AIGC 协作文档](简单神经网络运算框架的实现/docs/AIGC/)中。这些文件是我跟着 Codex 老师实现项目时留下的计划与教学记录，篇幅较长也很晦涩，部分内容也已经被后来的代码调整，只适合作为补充材料。

### 各目录的作用

| 目录 | 内容 |
| --- | --- |
| `mininn/` | 框架核心，包括 Linear、ReLU、Conv2D、Flatten、BatchNorm、Softmax 交叉熵、Sequential、SGD 和 IDX 数据读取 |
| `examples/` | 全连接分类、小型卷积网络和 Fashion-MNIST 的实际训练与评估脚本 |
| `tests/` | 开发期间用于拆分任务、检查梯度和防止回归的测试；读者可以按需查看 |
| `docs/` | `lab_report.md` 是最终实验报告，`AIGC/` 保存与 Codex 协作时形成的详细设计和教学文档 |

框架中的层使用同一组显式接口：`forward()` 计算输出，`backward()` 接收上游梯度并返回输入梯度，`parameters()` 和 `gradients()` 把可训练数组交给 SGD。`Sequential` 按正序完成前向传播，再按逆序传回梯度。当前完整测试共 117 项；测试也帮我弄清了各层的输入条件和异常行为。

### 运行案例

在项目目录中运行：

```powershell
cd "D:\code\DeepLearning\简单神经网络运算框架的实现"

# 完整测试
python -m unittest discover -s tests

# 全连接分类与离线小型 CNN
python examples/train_toy_classifier.py
python examples/train_toy_cnn.py
```

Fashion-MNIST 数据保存在仓库已忽略的 `.build/fashion-mnist` 中。正式训练命令为：

```powershell
python -m examples.train_fashion_mnist `
  "..\.build\fashion-mnist\train-images-idx3-ubyte.gz" `
  "..\.build\fashion-mnist\train-labels-idx1-ubyte.gz" `
  "..\.build\fashion-mnist\t10k-images-idx3-ubyte.gz" `
  "..\.build\fashion-mnist\t10k-labels-idx1-ubyte.gz"
```

当前脚本使用 2,000 个训练样本、1,000 个测试样本、batch size 32、学习率 0.05 和固定随机种子 42。10 个 epoch 后，训练损失从 `1.477389` 降到 `0.372161`，最终测试准确率为 `81.20%`。

## 目录

```text
DeepLearning/
├── source/
│   ├── 0.python&numpy入门/
│   │   ├── basic_python.py # Python 基础练习
│   │   └── basic_numpy.py  # NumPy 基础练习
│   ├── 1.预备知识/
│   │   ├── 1.数据操作.py    # Tensor 数据操作练习
│   │   ├── 2.自动求梯度.py  # PyTorch 自动求梯度练习
│   │   └── test_torch.py    # PyTorch 与 CUDA 环境检查
│   ├── 2.深度学习基础/
│   │   ├── 1.线性回归/
│   │   │   └── linear_model.py # 线性回归的手动实现与简洁实现
│   │   ├── 2.sofmtmax/
│   │   │   ├── 1.softmax_model.py          # Softmax 的手动实现
│   │   │   └── 2.softmax_simple_version.py # Softmax 的简洁实现
│   │   └── 3.多层感知机/
│   │       ├── multilayer_perceptron.py                # 多层感知机的手动实现
│   │       └── multilayer_perceptron_simple_version.py # 基于 nn.Sequential 的简洁实现
│   ├── 3.卷积神经网络/
│   │   ├── LeNet/
│   │   │   └── LeNet.py      # LeNet 练习
│   │   └── batchnormalization/
│   │       └── BatchNorm.py  # 批量归一化练习
│   └── 通用模板库/
│       └── d2lzh_pytorch.py # 数据迭代、损失函数与数据集加载工具
├── diary/
│   ├── 1.预备知识/
│   │   ├── 2026-08-11.md # 第一天学习日志
│   │   ├── 2026-08-12.md # 数据处理收尾
│   │   └── 2026-8-14_to_2026-8-16.md # Python、NumPy 与自动求梯度
│   ├── 2.深度学习基础/
│   │   ├── 2026-8-18_to_2026-8-20.md       # 线性回归与 Softmax 前的准备
│   │   ├── 2026-8-21_to_2026-8-23.md       # Softmax 与神经网络框架起步
│   │   └── 2026-08-25_to_2026-08-30.md     # 多层感知机与最小训练闭环
│   └── 简单神经网络框架的实现/
│       ├── 2026-8-23.md  # Task1 神经网络框架搭建
│       ├── 2026-08-24.md # Linear 反向传播与数值梯度检查
│       ├── 2026-08-31_to_2026-09-03.md # 从零实现 Conv2D
│       ├── 2026-09-04.md # Flatten 与离线小型 CNN
│       └── 2026-09-18.md # 项目收尾、训练闭环与测试反思
├── 简单神经网络运算框架的实现/
│   ├── docs/
│   │   ├── lab_report.md # 实验报告
│   │   └── AIGC/         # 设计、计划与教学文档
│   ├── examples/         # 训练与评估案例
│   ├── mininn/           # 框架核心源码
│   └── tests/            # 开发与回归测试
└── README.md
```

## 学习日志

- [2026-08-11：深度学习学习第一天](diary/1.预备知识/2026-08-11.md)
- [2026-08-12：数据处理收尾](diary/1.预备知识/2026-08-12.md)
- [2026-08-14 至 2026-08-16：Python、NumPy 与自动求梯度](diary/1.预备知识/2026-8-14_to_2026-8-16.md)
- [2026-08-18 至 2026-08-20：线性回归与 Softmax 前的准备](diary/2.深度学习基础/2026-8-18_to_2026-8-20.md)
- [2026-08-21 至 2026-08-23：从 Softmax 走到自己的神经网络框架](diary/2.深度学习基础/2026-8-21_to_2026-8-23.md)
- [2026-08-23：开始搭自己的神经网络运算框架](diary/简单神经网络框架的实现/2026-8-23.md)
- [2026-08-24：把 Linear 的反向传播接起来](diary/简单神经网络框架的实现/2026-08-24.md)
- [2026-08-25 至 2026-08-30：从多层感知机到自己的训练闭环](diary/2.深度学习基础/2026-08-25_to_2026-08-30.md)
- [2026-08-31 至 2026-09-03：第一次从零写完卷积层](diary/简单神经网络框架的实现/2026-08-31_to_2026-09-03.md)
- [2026-09-04：把卷积层接进第一个可训练的小型 CNN](diary/简单神经网络框架的实现/2026-09-04.md)
- [2026-09-18：写完目前最长的 NumPy 项目](diary/简单神经网络框架的实现/2026-09-18.md)
