# TextCNN 与 BiLSTM 随机种子复现实验

[三组新增随机种子结果分析报告](2026-11-03_random_seed_summary.md)

已完成种子 17、2024、3407 的六次训练。BiLSTM 平均准确率 92.0789%，TextCNN 为 91.7412%；平均差值 +0.3377 个百分点。

- [种子 17 的独立报告](seed_17/2026-11-03_textcnn_vs_bilstm.md)。
- [种子 2024 的独立报告](seed_2024/2026-11-03_textcnn_vs_bilstm.md)。
- [种子 3407 的独立报告](seed_3407/2026-11-03_textcnn_vs_bilstm.md)。

配置、原始评估数据和图表分别位于各组目录；跨种子统计在本目录 `data/`，权重与完整训练日志在仓库根目录 `.build/task2/runs/random_seeds_20261103/`。主统计只包含新增三组，历史种子 42 单列参考，不选择测试成绩最高的种子。
