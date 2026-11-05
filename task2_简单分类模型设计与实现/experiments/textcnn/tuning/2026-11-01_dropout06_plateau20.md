# AG-news TextCNN：dropout06_plateau20

日期：2026-11-01。配置：[textcnn_ag_news_dropout06_plateau20.json](../../../configs/textcnn_ag_news_dropout06_plateau20.json)。

## 设置

词向量和每个卷积分支通道数均为 128，卷积核 3/4/5，参数量 5,625,220。
Dropout=0.6，weight decay=0.0001，初始学习率=0.001，batch size=64，训练 20 轮。
ReduceLROnPlateau 监控验证损失，factor=0.5、patience=1、min_lr=0.00001。随机种子 42，训练/验证/测试样本 108000/12000/7600，词表 42396。
训练进程耗时 141.8 秒。`best_accuracy.pt` 按最高验证准确率选择，同准确率选更低验证损失；`best_loss.pt` 独立保留。每次只评估本轮按验证指标选出的模型。
最低损失模型选中第 9 轮（验证损失 0.247118，准确率 91.775%）；测试结果来自最高准确率模型，不混用两份检查点的数据。

## 完整逐轮输出

```text
Epoch 01/20 | train loss: 0.6616 | train acc: 74.36% | val loss: 0.3629 | val acc: 88.02% | lr: 0.001
Epoch 02/20 | train loss: 0.3409 | train acc: 88.69% | val loss: 0.2961 | val acc: 90.00% | lr: 0.001
Epoch 03/20 | train loss: 0.2875 | train acc: 90.42% | val loss: 0.2666 | val acc: 90.92% | lr: 0.001
Epoch 04/20 | train loss: 0.2609 | train acc: 91.47% | val loss: 0.2573 | val acc: 91.41% | lr: 0.001
Epoch 05/20 | train loss: 0.2446 | train acc: 91.92% | val loss: 0.2560 | val acc: 91.44% | lr: 0.001
Epoch 06/20 | train loss: 0.2295 | train acc: 92.27% | val loss: 0.2525 | val acc: 91.53% | lr: 0.001
Epoch 07/20 | train loss: 0.2155 | train acc: 92.82% | val loss: 0.2538 | val acc: 91.14% | lr: 0.001
Epoch 08/20 | train loss: 0.2019 | train acc: 93.28% | val loss: 0.2547 | val acc: 91.39% | lr: 0.001
Epoch 09/20 | train loss: 0.1587 | train acc: 94.72% | val loss: 0.2471 | val acc: 91.77% | lr: 0.0005
Epoch 10/20 | train loss: 0.1403 | train acc: 95.34% | val loss: 0.2539 | val acc: 91.65% | lr: 0.0005
Epoch 11/20 | train loss: 0.1270 | train acc: 95.81% | val loss: 0.2651 | val acc: 91.47% | lr: 0.0005
Epoch 12/20 | train loss: 0.0952 | train acc: 97.00% | val loss: 0.2664 | val acc: 91.48% | lr: 0.00025
Epoch 13/20 | train loss: 0.0836 | train acc: 97.36% | val loss: 0.2733 | val acc: 91.55% | lr: 0.00025
Epoch 14/20 | train loss: 0.0680 | train acc: 97.98% | val loss: 0.2774 | val acc: 91.52% | lr: 0.000125
Epoch 15/20 | train loss: 0.0624 | train acc: 98.20% | val loss: 0.2809 | val acc: 91.49% | lr: 0.000125
Epoch 16/20 | train loss: 0.0536 | train acc: 98.58% | val loss: 0.2849 | val acc: 91.45% | lr: 6.25e-05
Epoch 17/20 | train loss: 0.0514 | train acc: 98.65% | val loss: 0.2880 | val acc: 91.38% | lr: 6.25e-05
Epoch 18/20 | train loss: 0.0470 | train acc: 98.82% | val loss: 0.2902 | val acc: 91.33% | lr: 3.125e-05
Epoch 19/20 | train loss: 0.0468 | train acc: 98.82% | val loss: 0.2922 | val acc: 91.43% | lr: 3.125e-05
Epoch 20/20 | train loss: 0.0446 | train acc: 98.88% | val loss: 0.2930 | val acc: 91.39% | lr: 1.5625e-05
```

## 结果与精简对比图

| 对照 | 选定轮次 | 验证损失 | 验证准确率 | 测试准确率 | 测试正确数 |
| --- | --- | --- | --- | --- | --- |
| Fixed baseline (`textcnn_wd1e4`) | 8 | 0.250798 | 91.633% | 91.750% | 6973 / 7600 |
| Previous best (`textcnn_plateau20`) | 8 | 0.244026 | 91.833% | 91.868% | 6982 / 7600 |
| Current trial (`textcnn_dropout06_plateau20`) | 9 | 0.247118 | 91.775% | 91.605% | 6962 / 7600 |

![固定基线、此前最佳与本轮实验](../assets/dropout06_plateau20_comparison.png)

每张图最多三组：固定基线、此前最佳、本轮实验，重合时合并；更早实验保留在各自记录和 `.build/task2/comparisons/full_history.csv`，不继续叠加曲线。
固定基线按最低验证损失选择，另外两组按验证准确率选择；固定基线两种指标同在第 8 轮最优。旧 10 轮实验曲线只画实际轮次。

测试准确率为 91.605263%，正确 6962 / 7600；92% 对应至少 6992 条正确，尚差 30 条，未达到目标。
本轮验证准确率与此前最佳相比变化 -0.058 个百分点。
这里只运行一个随机种子；测试集已在多轮实验中查看，不能把多轮调参后的成绩视为一次完全未见的最终评估。

## 产物与核对

原始完整控制台（含保存及调度提示）、配置、环境、逐轮全精度 CSV、两种模型和测试指标保存在 `.build/task2/runs/textcnn_dropout06_plateau20/`。
本轮汇总与 SHA-256 保存在 `.build/task2/comparisons/dropout06_plateau20/summary.json`、`summary.csv`；完整历史位于 `.build/task2/comparisons/full_history.csv`。
已核对全部 epoch 行、两种检查点选择、参数量、实际配置、调度器逐轮重放、7600 条测试样本，以及本轮开始前 11 份历史模型的权重哈希未变。

复现时在项目目录运行，使用新的输出目录保留现有结果：

```powershell
python -m news_classifier.train --config configs/textcnn_ag_news_dropout06_plateau20.json
python -m news_classifier.evaluate --checkpoint ../.build/task2/runs/textcnn_dropout06_plateau20/best_accuracy.pt
```
