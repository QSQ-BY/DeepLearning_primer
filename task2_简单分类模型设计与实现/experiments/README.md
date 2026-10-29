# 实验记录

正式训练前复制一份配置，使用不同的 `experiment_name` 和 `output.run_dir` 区分实验，避免覆盖上一轮结果。当前尚未进行 AG-news 实验。

每次实验的运行文件放在仓库根目录 `.build/task2/runs/<实验名>/`，训练流程实现时应生成：

- `config.json`：本次实际使用的完整配置。
- `metrics.csv`：每轮 epoch、train_loss、train_accuracy、val_loss、val_accuracy、learning_rate。
- `best.pt`：最佳验证模型的权重、词表、类别名称、配置和轮次。
- `environment.txt`：Python、PyTorch、datasets 版本以及设备信息。
- `test_metrics.json`：独立评估后的测试集指标。

先记录 TextCNN 初始配置的结果，再逐项比较学习率与衰减策略、Dropout、词向量维度、卷积核宽度和数量。使用相同的数据划分与评估方式，并记录随机种子。

这里可以后续添加需要纳入版本控制的简短实验总结；原始日志和模型文件保留在 `.build/`。不要把尚未运行的配置写成已经验证的结论。
