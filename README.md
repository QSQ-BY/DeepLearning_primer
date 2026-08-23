# DeepLearning

这是我的深度学习入门学习仓库，用来保存练习代码和每日学习日志。

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
│   │   └── 2.sofmtmax/
│   │       ├── 1.softmax_model.py          # Softmax 的手动实现
│   │       └── 2.softmax_simple_version.py # Softmax 的简洁实现
│   └── 通用模板库/
│       └── d2lzh_pytorch.py # 数据迭代、损失函数与数据集加载工具
├── diary/
│   ├── 1.预备知识/
│   │   ├── 2026-08-11.md # 第一天学习日志
│   │   ├── 2026-08-12.md # 数据处理收尾
│   │   └── 2026-8-14_to_2026-8-16.md # Python、NumPy 与自动求梯度
│   └── 2.深度学习基础/
│       ├── 2026-8-18_to_2026-8-20.md # 线性回归与 Softmax 前的准备
│       └── 2026-8-21_to_2026-8-23.md # Softmax 与神经网络框架起步
├── 简单神经网络运算框架的实现/
│   ├── docs/     # 任务设计与实现计划
│   ├── examples/ # 训练示例
│   ├── mininn/   # 框架源码
│   └── tests/    # 单元测试
└── README.md
```

## 学习日志

- [2026-08-11：深度学习学习第一天](diary/1.预备知识/2026-08-11.md)
- [2026-08-12：数据处理收尾](diary/1.预备知识/2026-08-12.md)
- [2026-08-14 至 2026-08-16：Python、NumPy 与自动求梯度](diary/1.预备知识/2026-8-14_to_2026-8-16.md)
- [2026-08-18 至 2026-08-20：线性回归与 Softmax 前的准备](diary/2.深度学习基础/2026-8-18_to_2026-8-20.md)
- [2026-08-21 至 2026-08-23：从 Softmax 走到自己的神经网络框架](diary/2.深度学习基础/2026-8-21_to_2026-8-23.md)

## 运行环境

书本练习使用 Python 和 PyTorch。运行 `source/1.预备知识/test_torch.py` 可以查看本机的 PyTorch 版本、CUDA 可用状态，并执行一段基础 Tensor 运算。`简单神经网络运算框架的实现` 只使用 NumPy 和 Python 标准库，单元测试使用 `unittest`。
