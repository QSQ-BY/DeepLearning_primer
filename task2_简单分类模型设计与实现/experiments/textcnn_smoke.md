# TextCNN AG-news 单轮试跑

日期：2026-11-01。配置：[textcnn_ag_news_smoke.json](../configs/textcnn_ag_news_smoke.json)。

本次运行用于检查真实数据上的完整训练流程，仅训练一个 epoch。验证集用于检查模型表现，官方测试集未参与评估。

## 运行方式

在 Task 2 项目目录，使用 `d2l-pytorch` 环境运行：

```powershell
$env:HF_HOME = "D:\code\DeepLearning\.build\task2\huggingface"
python -m news_classifier.train --config configs/textcnn_ag_news_smoke.json
```

## 数据与环境

- 官方训练集划分为 108,000 条训练样本和 12,000 条验证样本，官方测试集 7,600 条保持独立。
- 实际词表大小为 42,396；随机种子 42，批量大小 64，学习率 0.001。
- Python 3.12.13，PyTorch 2.13.0+cu130，datasets 5.1.0。
- 使用 NVIDIA GeForce RTX 5070 Ti Laptop GPU，设备为 CUDA。

## 实际结果

| Epoch | 训练损失 | 训练准确率 | 验证损失 | 验证准确率 |
| --- | --- | --- | --- | --- |
| 1 | 0.613857 | 76.62% | 0.334090 | 88.75% |

结果目录为仓库根目录下的 `.build/task2/runs/textcnn_smoke/`：

- `metrics.csv`：本轮完整精度的训练与验证指标。
- `best.pt`：模型权重、词表、类别名称、配置和验证指标。
- `config.json`、`environment.txt`：本次验证时补充保存的配置与环境记录。

已检查 CSV 与权重文件中的轮次及验证指标一致；模型权重可重新加载，并对两条文本完成有限值、四分类输出检查。依赖检查 `python -m pip check` 通过。

本次结果是单轮验证集成绩，尚无官方测试集成绩。后续继续实现独立评估和预测入口，再运行多轮基线实验。
