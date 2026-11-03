# 新闻分类代码结构

```text
news_classifier/
├── config.py                 # 配置读取与路径解析
├── data/
│   ├── dataset.py            # AG-news划分、词表、编码和DataLoader
│   ├── preprocessing.py      # 对照实验使用的统一文本清洗
│   └── embeddings.py         # 按训练词表导入预训练词向量
├── models/
│   └── textcnn.py            # TextCNN模型
├── training/
│   ├── engine.py             # 单轮训练与评估
│   └── train.py              # 训练流程、学习率调度与最佳权重保存
├── evaluation/
│   ├── evaluate.py           # 保存模型的独立测试
│   ├── predict.py            # 单条新闻预测
│   └── analysis.py           # 全量预测导出、指标与错误集合比较
├── experiments/
│   ├── controlled.py         # 清洗、随机词向量、GloVe及Word2Vec对照实验
│   └── word2vec.py           # 仅用固定训练文本预训练128维Skip-gram
└── train.py / evaluate.py / predict.py / model.py / engine.py
                              # 保留原有命令和导入的兼容入口
```

在Task 2目录运行，原命令仍然有效：

```powershell
python -m news_classifier.train --config configs/textcnn_ag_news_k237_plateau20.json --check-config
python -m news_classifier.evaluate --checkpoint ../.build/task2/runs/textcnn_k237_plateau20/best_accuracy.pt
python -m news_classifier.predict --checkpoint ../.build/task2/runs/textcnn_k237_plateau20/best_accuracy.pt --text "The team won the championship."
```

对照实验使用独立入口，默认保留已有输出、拒绝覆盖训练日志：

```powershell
python -m news_classifier.experiments.controlled --mode cleaning --run-dir ../.build/task2/runs/cleaning_repro
python -m news_classifier.experiments.controlled --mode random100 --run-dir ../.build/task2/runs/random100_repro
python -m news_classifier.experiments.controlled --mode glove100 --run-dir ../.build/task2/runs/glove100_repro
python -m news_classifier.experiments.word2vec --output-dir ../.build/task2/pretrained/word2vec_repro
python -m news_classifier.experiments.controlled --mode random128 --run-dir ../.build/task2/runs/random128_repro
python -m news_classifier.experiments.controlled --mode word2vec128 --vectors ../.build/task2/pretrained/word2vec_repro/vectors.txt --run-dir ../.build/task2/runs/word2vec128_repro
```

`glove100`需要本地官方GloVe 6B 100维词向量与来源清单。数据缓存、预训练词向量和训练权重均放在仓库`.build/task2/`。实验报告与错误清单见[错误分析目录](../experiments/error_analysis/README.md)。代码目录不保存生成的数据和训练日志。

清洗组权重会记录`experiment.clean_text`和`cleaning_version`；独立测试、单条预测和错误导出都会恢复同一处理规则。当前规则只去除常见HTML标签，保留`<CIEN.O>`等股票代码；初版权重仍可按其原始规则复核。导入包不会触发训练或下载。

Word2Vec预训练需要`gensim==4.4.0`，可用`python -m pip install gensim==4.4.0`安装。它只使用108000条固定训练文本，不读取验证、测试文本或标签；分类阶段保留原TextCNN结构、128维度和微调设置。向量导入会核对训练行号摘要与文件哈希。默认正式预训练目录中的可加载模型是`word2vec_portable.model`；新复现实验直接生成`word2vec.model`。正式结果见[Word2Vec实验报告](../experiments/error_analysis/2026-11-03_word2vec_textcnn.md)。
