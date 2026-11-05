# BiLSTM 新闻分类实验

2026-11-03 完成 BiLSTM 搭建、小样本验证及 20 轮正式基线训练。验证集选出第 8 轮权重，测试准确率为 **92.0789%（6998/7600）**，比原最佳 TextCNN 高 **0.0658 个百分点**。整体指标、训练曲线和混淆矩阵见[正式实验对比](2026-11-03_textcnn_vs_bilstm.md)。

随后完成[早停、WD 与词嵌入 Dropout 的 6 组单因素实验](regularization/README.md)。验证集选出的方案保持 WD=1e-4，在词嵌入后加入 Dropout=0.2，分类层 Dropout 仍为 0.5；第 11 轮早停，保留第 8 轮权重，测试准确率为 **92.3553%（7019/7600）**。增大 WD 的两组未超过验证集基线。

当前选定方案配置为 [`bilstm_es_dropout02_20261103.json`](../../configs/bilstm_es_dropout02_20261103.json)，权重位于 `.build/task2/runs/bilstm_es_dropout02_20261103/best_accuracy.pt`。图表交付副本在 `D:\codex\BiLSTM_regularization_20261103\`。

最新方案的[错误分析与 TextCNN 对比总结](error_analysis/2026-11-03_best_bilstm_vs_textcnn.md)已保存为 Markdown：修正 192 条旧错误、新增 166 条、共同错误 415 条，附四组对比图及[全部 581 条错误原文](error_analysis/data/bilstm_all_errors.md)。

随后完成[种子 17、2024、3407 的六次重新训练与对比](../random_seeds/2026-11-03_random_seed_summary.md)。固定原数据划分后，BiLSTM 三组平均准确率为 **92.0789% ± 0.1206 个百分点**，TextCNN 为 **91.7412% ± 0.0675 个百分点**，平均优势 **0.3377 个百分点**；± 为样本标准差。各组报告、配置、图表和配对错误清单分别保存在 `experiments/random_seeds/seed_<seed>/`，原种子 42 单列为历史参考。

## TextCNN 独立归档

开始修改前，将当时的 Task 2 代码、配置、报告、实验数据、全部 TextCNN 运行目录和根目录演示权重复制到：

```text
.build/task2/archives/textcnn_20261103_183521/
├── task2_简单分类模型设计与实现/   # 修改前的项目快照
├── .build/task2/runs/textcnn_*/  # 历史权重、指标和运行记录
├── textcnn_demo.pt
└── manifest.json               # 每个文件的相对路径、大小和 SHA-256
```

共 350 个文件、880278372 字节，复制后逐项核对 SHA-256，包含历史运行目录中的嵌套评估结果和源码快照。这是本地归档，按仓库惯例保存在被 Git 忽略的 `.build/` 下；数据缓存和单独的预训练词向量目录没有复制。历史权重已包含分类模型的词嵌入参数，可继续评估和预测。

原模型源码仍为 [`models/textcnn.py`](../../news_classifier/models/textcnn.py)，原实验配置和权重继续保留。新增模型选择器按 `model.name` 构建模型；没有该字段的旧权重默认恢复为 TextCNN。

## 基线结构与控制条件

```text
input_ids [B, L]
  → Embedding [B, L, 128]
  → 按真实 lengths 打包
  → 单层双向 LSTM，每个方向隐藏维度 128
  → 拼接最后一层两个方向的末状态 [B, 256]
  → Dropout(0.5)
  → Linear(256, 4)
  → logits [B, 4]
```

模型实现见 [`bilstm.py`](../../news_classifier/models/bilstm.py)。使用 `pack_padded_sequence` 跳过填充部分，支持未排序批次；长度张量在打包时转到 CPU，模型输出保留原批次顺序。相关接口见 [PyTorch 文档](https://docs.pytorch.org/docs/stable/generated/torch.nn.utils.rnn.pack_padded_sequence.html)。单层 LSTM 不设置层间 Dropout，分类前仍保留 Dropout。

[`configs/bilstm_ag_news.json`](../../configs/bilstm_ag_news.json) 沿用原最终 TextCNN 实验的数据设置和训练超参数：随机种子 42，108000／12000／7600 条训练／验证／测试数据；训练部分建词表，实际 42396 词；最大长度 256，随机初始化 128 维词向量，batch size 64，Adam 学习率 0.001，weight decay 0.0001，20 轮，按验证损失降低学习率。测试集不参与训练和模型选择。

模型参数共 5691908 个。当前先比较随机初始化的基线，不加载 TextCNN 权重或预训练 Word2Vec。

## 运行

在仓库根目录激活现有环境并进入 Task 2：

```powershell
conda activate d2l-pytorch
cd .\task2_简单分类模型设计与实现
python -m news_classifier.train --config configs/bilstm_ag_news.json --check-config
python -m news_classifier.train --config configs/bilstm_ag_news.json
```

正式训练输出在 `.build/task2/runs/bilstm_baseline_20261103/`，分别保存 `best_loss.pt`、`best_accuracy.pt`、`metrics.csv` 和 `config.json`。重新实验时修改配置的 `experiment_name`、`output.run_dir`，训练入口会拒绝覆盖已有日志或权重。默认不带 `--config` 的旧命令仍使用 TextCNN 配置。

完成训练后，使用验证集选出的权重评估和预测：

```powershell
python -m news_classifier.evaluate --checkpoint ../.build/task2/runs/bilstm_baseline_20261103/best_accuracy.pt
python -m news_classifier.predict --checkpoint ../.build/task2/runs/bilstm_baseline_20261103/best_accuracy.pt --text "The team won the championship."
python -m unittest discover -s tests -v
```

本次正式训练已完成，以上训练输出目录已有权重和日志；再次训练前需先在配置中指定新的目录。当前 `best_loss.pt` 和 `best_accuracy.pt` 都来自第 8 轮，执行记录见 `.build/task2/runs/bilstm_baseline_20261103/training_execution.json`。

复用现有权重生成对比图，可在仓库根目录运行：

```powershell
python task2_简单分类模型设计与实现/experiments/scripts/compare_textcnn_bilstm.py
```

图表源文件保存在本目录 `assets/`，PNG／SVG 交付副本在 `D:\codex\BiLSTM_vs_TextCNN_20261103\`。

## 已完成的验证

- 新增测试覆盖未排序变长批次与单条结果一致、忽略尾部填充、两个方向均有梯度、PAD 梯度为零、非法长度、配置校验及历史 TextCNN 兼容。
- 微型数据跑通训练、两种最佳权重保存、重新加载、单条预测、独立评估和逐样本预测导出，并检查训练不读取测试集、不覆盖历史输出。
- 使用真实 AG-news 原划分建立词表，与 TextCNN 权重中的词表逐项一致；取 256 条训练和 256 条验证样本完成一轮 GPU 训练。小样本结果只验证运行流程，不作为正式实验结论。

本地验证记录位于 `.build/task2/runs/bilstm_baseline_20261103_smoke_verified/`。CPU／GPU 的 FP32 对比关闭 cuDNN TF32 后进行；正常训练保留 PyTorch 默认精度设置。
