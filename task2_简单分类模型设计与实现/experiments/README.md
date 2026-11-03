# Task 2 实验记录

报告按实验目的分类：

- [调参实验报告](tuning/README.md)：学习率、batch size、weight decay、Dropout、模型容量与卷积核组合。
- [错误分析报告](error_analysis/README.md)：完整误分类案例、错误共性及后续对照实验。
- [Word2Vec 对照报告](error_analysis/2026-11-03_word2vec_textcnn.md)：保持 TextCNN 不变，只替换词向量初始化；本次测试准确率 91.8553%，未超过原方案。

最终2/3/7卷积核方案的单次实验测试准确率为 **92.0132%（6993/7600）**，详见[最终调参记录](tuning/2026-11-01_k237_plateau20.md)和[实验报告](../docs/report.md)。

`assets/` 保存报告使用的对比图，`error_analysis/data/` 保存错误清单及分析数据，`scripts/` 存放可复用的实验分析脚本。实验配置位于 `../configs/`，原始训练日志与权重位于仓库根目录 `.build/task2/runs/`。

模型按验证集指标选择后评估测试集。现有结果来自单个随机种子，调参期间多次查看过测试结果；复现时使用新的输出目录，保留历史权重。
