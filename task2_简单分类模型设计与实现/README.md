# Task 2 简单分类模型设计与实现

本项目选择 AG-news 新闻四分类，以 TextCNN 作为首个模型。当前完成项目骨架，数据处理、网络和训练逻辑留有明确的待实现接口，后续按模块逐步完成。

## 项目结构

```text
task2_简单分类模型设计与实现/
├── configs/
│   └── textcnn_ag_news.json   # 数据、模型和训练配置
├── news_classifier/
│   ├── __init__.py
│   ├── config.py             # 读取配置并解析输出路径
│   ├── data.py               # 数据读取、分词、词表和批次填充
│   ├── model.py              # TextCNN 定义
│   ├── engine.py             # 单轮训练与评估
│   ├── train.py              # 训练命令行入口
│   ├── evaluate.py           # 最佳模型的测试集评估入口
│   └── predict.py            # 单条新闻预测入口
├── docs/
│   └── report.md             # 任务报告模板
├── experiments/
│   └── README.md             # 实验记录约定
├── requirements.txt
└── README.md
```

运行时生成的数据、权重和日志放在仓库根目录的 `.build/task2/`，该目录已被 Git 忽略。配置里的相对路径以本项目目录为基准，与启动命令的位置无关。

## 环境与入口检查

在 PowerShell 中进入本项目，使用已有的 PyTorch 环境：

```powershell
conda activate d2l-pytorch
cd "D:\code\DeepLearning\task2_简单分类模型设计与实现"

# 检查配置，无需下载数据或安装 datasets
python -m news_classifier.train --check-config
python -m news_classifier.train --help
python -m news_classifier.evaluate --help
python -m news_classifier.predict --help
```

后续接入数据前安装依赖：

```powershell
python -m pip install -r requirements.txt
```

目前 `--check-config` 和各入口的 `--help` 可以运行。训练、测试和预测的核心接口会明确抛出 `NotImplementedError`，提示需要完成的模块；骨架阶段尚无正式实验结果。

## 建议实现顺序

1. **数据处理**：在 `data.py` 接入 `fancyzhx/ag_news`。从训练集按类别划分验证集，测试集保留用于最终评估；先划分，再只从训练部分构建词表。
2. **词表和批次**：实现统一分词、未知词映射、长度截断、PAD 填充。返回 `input_ids [B,L]`、真实 `lengths [B]` 和 `labels [B]`，标签使用 0 到 3。
3. **TextCNN**：参考原有练习，依次完成 Embedding、多尺度 Conv1d、按长度掩码的最大池化、拼接、Dropout 和四分类线性层。先检查形状与梯度。
4. **训练循环**：在 `engine.py` 实现单轮训练和无梯度评估，在 `train.py` 组装数据、模型、Adam、学习率策略和最佳模型保存。先验证小样本能够拟合，再训练完整数据。
5. **测试与预测**：加载最佳验证模型及其词表、配置，在 `evaluate.py` 评估测试集，在 `predict.py` 复用相同预处理预测新闻类别。
6. **实验和报告**：记录基线，再逐项比较超参数调整，填写 `docs/report.md`。

核心逻辑补齐后的命令约定如下，现在直接运行会提示待实现内容：

```powershell
python -m news_classifier.train --config configs/textcnn_ag_news.json
python -m news_classifier.evaluate --checkpoint ../.build/task2/runs/textcnn_baseline/best.pt
python -m news_classifier.predict --checkpoint ../.build/task2/runs/textcnn_baseline/best.pt --text "Scientists announce a new discovery"
```

## 模块之间的约定

- `prepare_data(config)` 返回训练、验证、测试三个 DataLoader，以及词表和类别名称；所有批次使用同一种格式。
- `TextCNN.forward(input_ids, lengths)` 返回 `[B,4]` 的原始 logits。训练损失直接接收 logits，展示概率时再做 Softmax。
- `train_one_epoch()` 和 `evaluate()` 都返回平均损失、准确率及样本数量。准确率取值为 0 到 1，显示时再转换为百分比。
- 根据验证集指标选择最佳模型。保存模型权重时一并保存词表、配置和类别名称，独立评估和预测时不重新构建词表。
- 训练入口负责设置随机种子、选择设备和写日志。导入模块不启动训练、不下载数据。

## 与任务要求对应

任务允许在 AG-news 与 CIFAR-100 中任选一个数据集，也允许使用基础模型。本项目先完成 AG-news + TextCNN，不要求同时实现 LSTM 或预训练语言模型。

AG-news 的 92% 是文档给出的参考成绩。最终提交应包含源码和任务报告，说明网络设计、超参数选择、实际问题与解决方法，并提供每轮 loss、accuracy 等可复现记录。配置文件中的数值是初始试验设置，效果需要实际训练验证。

数据来源：[AG-news 数据集说明](https://huggingface.co/datasets/fancyzhx/ag_news)。原有学习实现：[textcnn.py](../source/4.自然语言处理/3.textcnn/textcnn.py)。
