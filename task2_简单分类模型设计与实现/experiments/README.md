# Task 2 实验记录

报告按实验目的分类：

- [调参实验报告](textcnn/tuning/README.md)：学习率、batch size、weight decay、Dropout、模型容量与卷积核组合。
- [错误分析报告](textcnn/error_analysis/README.md)：完整误分类案例、错误共性及后续对照实验。
- [Word2Vec 对照报告](textcnn/error_analysis/2026-11-03_word2vec_textcnn.md)：保持 TextCNN 不变，只替换词向量初始化；本次测试准确率 91.8553%，未超过原方案。
- [BiLSTM 正式实验对比](bilstm/2026-11-03_textcnn_vs_bilstm.md)：完成 20 轮训练，测试准确率 92.0789%；包含与原最佳 TextCNN 的整体指标、训练曲线和混淆矩阵对比。
- [BiLSTM 早停与正则化对比](bilstm/regularization/README.md)：完成 WD 和词嵌入 Dropout 单因素实验；按验证集选出的 Dropout=0.2 方案测试准确率为 92.3553%，包含 4 组对比图。
- [最新最佳 BiLSTM 错误分析](bilstm/error_analysis/2026-11-03_best_bilstm_vs_textcnn.md)：与原最佳 TextCNN 逐样本比较，修正 192 条、新增 166 条、共同错误 415 条；包含四组对比图、案例遮挡诊断及全部 581 条错误附录。
- [三组新增随机种子复现实验](random_seeds/README.md)：种子 17、2024、3407，各重新训练 TextCNN 和 BiLSTM；保持数据划分种子 42，按组保存报告，并提供跨种子汇总。

最终2/3/7卷积核方案的单次实验测试准确率为 **92.0132%（6993/7600）**，详见[最终调参记录](textcnn/tuning/2026-11-01_k237_plateau20.md)和[实验报告](../docs/report.md)。

`textcnn/assets/` 保存报告使用的对比图，`textcnn/error_analysis/data/` 保存错误清单及分析数据，`scripts/` 存放可复用的实验分析脚本。实验配置位于 `../configs/`，原始训练日志与权重位于仓库根目录 `.build/task2/runs/`。

模型按验证集指标选择后评估测试集。前期调参使用种子 42，后续补充了三个训练种子的复现实验；调参期间多次查看过测试结果；复现时使用新的输出目录，保留历史权重。
