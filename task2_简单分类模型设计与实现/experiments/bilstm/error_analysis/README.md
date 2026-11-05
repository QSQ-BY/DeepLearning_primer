# 最新最佳 BiLSTM 错误分析

[总结报告：最新最佳 BiLSTM 与原最佳 TextCNN 对比](2026-11-03_best_bilstm_vs_textcnn.md)

本轮选用验证集确定的 `bilstm_es_dropout02_20261103/best_accuracy.pt`：WD=1e-4、词嵌入 Dropout=0.2，第 8 轮权重，第 11 轮早停。官方测试准确率为 **92.3553%（7019/7600）**，原最佳 TextCNN 为 **92.0132%（6993/7600）**。

- 修正 TextCNN 错误 **192 条**，新增 **166 条**，共同错误 **415 条**，净减少 **26 条**。
- [全部 581 条错误原文与预测](data/bilstm_all_errors.md)。
- [全部 7600 条配对预测](data/paired_predictions.csv)、[修正](data/fixed.csv)、[新增](data/new_errors.csv)、[共同错误](data/both_wrong.csv)。
- `assets/` 包含四组 PNG/SVG：错误交换、混淆矩阵、错误方向变化、长度与未知词分层错误率。
- [汇总数据](data/summary.json)、[遮挡推理记录](data/masking_probes.json)、[复核结果](data/verification.json)。

报告只分析已有权重，保留官方标签。单个随机种子的结果不足以说明模型具有稳定优势，详细限制与后续实验建议见正文。
