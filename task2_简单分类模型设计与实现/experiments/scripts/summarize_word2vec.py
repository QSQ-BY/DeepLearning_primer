"""对齐 Word2Vec 与同入口随机对照，导出全部错误及分析所需数据。"""
import csv
import hashlib
import json
from pathlib import Path
import shutil
import sys

import numpy as np
import torch

PROJECT = Path(__file__).resolve().parents[2]
ROOT = PROJECT.parent
sys.path.insert(0, str(PROJECT))
from news_classifier.data import LABEL_NAMES, collate_batch, encode, tokenize
from news_classifier.evaluation.analysis import error_groups, write_csv, write_json
from news_classifier.models import TextCNN

DATA = PROJECT / 'experiments/error_analysis/data'


def load(folder):
    metrics = json.loads((folder / 'metrics.json').read_text(encoding='utf-8'))
    with (folder / 'all_predictions.csv').open(encoding='utf-8', newline='') as stream:
        rows = list(csv.DictReader(stream))
    arrays = np.load(folder / 'predictions.npz')
    return metrics, arrays['labels'], arrays['predictions'], rows


def bank_probe(metrics, row):
    """保留已定位案例的原文与 bank 遮挡输入，检查预测是否仍对局部词敏感。"""
    checkpoint = torch.load(metrics['checkpoint'], map_location='cpu', weights_only=True)
    config = checkpoint['config']
    model = TextCNN(len(checkpoint['vocab']), config['model']).eval()
    model.load_state_dict(checkpoint['model_state_dict'])
    ids = encode(row['text'], checkpoint['vocab'], config['data']['max_length'])
    positions = [i for i, word in enumerate(tokenize(row['text'])) if word == 'bank']
    variants = [('original', ids)]
    for position in positions:
        masked = ids.copy()
        masked[position] = checkpoint['vocab']['<UNK>']
        variants.append((f'bank_at_{position}_to_UNK', masked))
    input_ids, lengths, _ = collate_batch([(values, 0) for _, values in variants],
                                         min_length=max(config['model']['kernel_sizes']))
    with torch.inference_mode():
        probabilities = model(input_ids, lengths).softmax(1).numpy()
    return [dict(variant=name, prediction=LABEL_NAMES[int(probs.argmax())],
                 probabilities=probs.tolist()) for (name, _), probs in zip(variants, probabilities)]


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    torch.set_num_threads(4)
    models = {}
    locations = {'original128': DATA / 'kernel_comparison/k237',
                 'random128': DATA / 'random128', 'word2vec128': DATA / 'word2vec128'}
    for name, folder in locations.items():
        models[name] = load(folder)
    original, labels, _, rows = models['original128']
    for metrics, ys, pred, cases in models.values():
        assert np.array_equal(labels, ys)
        assert [r['text'] for r in rows] == [r['text'] for r in cases]
    comparisons = {}
    for before, after in [('original128', 'random128'), ('random128', 'word2vec128'),
                          ('original128', 'word2vec128')]:
        groups = error_groups(labels, models[before][2], models[after][2])
        name = f'{before}_to_{after}'
        comparisons[name] = {key: len(value) for key, value in groups.items()}
        for kind in ['fixed', 'both_wrong', 'new_errors']:
            records = [dict(sample_id=f'test:{i}', true_label=LABEL_NAMES[labels[i]],
                            baseline_prediction=LABEL_NAMES[models[before][2][i]],
                            candidate_prediction=LABEL_NAMES[models[after][2][i]],
                            candidate_confidence=models[after][3][i]['confidence'], text=rows[i]['text'])
                       for i in groups[kind]]
            if records:
                write_csv(DATA / after / f'{name}_{kind}.csv', records)
    kernel = json.loads((DATA / 'kernel_comparison/summary.json').read_text(encoding='utf-8'))
    common = np.asarray([int(value.split(':')[1]) for value in kernel['common_sample_ids']])
    source = torch.load(original['checkpoint'], map_location='cpu', weights_only=True)
    vocab = source['vocab']
    short = np.asarray([len(tokenize(row['text'])) <= 20 for row in rows])
    no_oov = np.asarray([all(word in vocab for word in tokenize(row['text'])) for row in rows])
    segments = []
    persistence = {}
    for name, (metrics, ys, pred, cases) in models.items():
        persistence[name] = dict(corrected=int((pred[common] == labels[common]).sum()),
                                 remaining_wrong=int((pred[common] != labels[common]).sum()))
        for label, mask in [('不超过20词', short), ('超过20词', ~short),
                            ('没有未知词', no_oov), ('至少一个未知词', ~no_oov)]:
            count = int(mask.sum())
            errors = int(((pred != labels) & mask).sum())
            segments.append(dict(model=name, segment=label, samples=count, errors=errors,
                                 error_rate=errors / count))
    target = DATA / 'word2vec128'
    run_dir = Path(models['word2vec128'][0]['checkpoint']).parent
    embedding = json.loads((run_dir / 'embedding_initialization.json').read_text(encoding='utf-8'))
    write_json(target / 'embedding_initialization.json', embedding)
    write_csv(target / 'feature_segments.csv', segments)
    # 所有错误原文在独立附件中保留，正文只引用少量案例。
    contents = ['# Word2Vec 128维 TextCNN：全部预测错误', '',
                '使用官方测试行号，保留原始标签；按测试顺序排列。', '']
    for row in models['word2vec128'][3]:
        if row['correct'] == 'True':
            continue
        contents += [f"## {row['sample_id']}：{row['true_label']} → {row['predicted_label']}", '',
                     f"预测置信度：{float(row['confidence']):.4f}", '', row['text'], '']
    (target / 'all_errors.md').write_text('\n'.join(contents), encoding='utf-8')
    from gensim.models import Word2Vec
    pretraining_dir = Path(embedding['vector_path']).parent
    source_manifest = json.loads((pretraining_dir / 'source_manifest.json').read_text(encoding='utf-8'))
    pretrained = Word2Vec.load(str(pretraining_dir / source_manifest.get('portable_model_file', 'word2vec.model')))
    neighbors = {word: pretrained.wv.most_similar(word, topn=8)
                 for word in ['bank', 'chip', 'software', 'profit', 'football', 'google']
                 if word in pretrained.wv}
    write_json(target / 'word_neighbors.json', neighbors)
    examples = []
    for i in [139, 1011, 1840, 4359, 5467, 6592]:
        examples.append(dict(sample_id=f'test:{i}', true_label=LABEL_NAMES[labels[i]],
                             predictions={name: LABEL_NAMES[item[2][i]] for name, item in models.items()},
                             text=rows[i]['text']))
    probes = {name: bank_probe(item[0], rows[139]) for name, item in models.items()}
    summary = dict(models={name: item[0] for name, item in models.items()}, comparisons=comparisons,
                   common_490_followup=persistence, feature_segments=segments,
                   embedding=embedding, pretrained_source_manifest=source_manifest,
                   selected_cases=examples, bank_probe=probes)
    write_json(target / 'summary.json', summary)
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    figure, axes = plt.subplots(1, 2, figsize=(10, 3.7), layout='constrained')
    for mode, label, color, marker in [('random128', 'Random 128d', '#235b8e', 'o'),
                                      ('word2vec128', 'Word2Vec 128d', '#ad521c', 's')]:
        run = Path(models[mode][0]['checkpoint']).parent
        with (run / 'metrics.csv').open(encoding='utf-8') as stream:
            log = list(csv.DictReader(stream))
        epochs = [int(row['epoch']) for row in log]
        for axis, field, multiplier in [(axes[0], 'val_accuracy', 100), (axes[1], 'val_loss', 1)]:
            axis.plot(epochs, [float(row[field]) * multiplier for row in log],
                      label=label, color=color, marker=marker, markersize=3, linewidth=1.5)
            axis.set_xlabel('TextCNN training epoch')
            axis.set_xticks([1, 4, 8, 12, 16, 20])
            axis.grid(alpha=0.22)
        chosen_epoch = models[mode][0]['epoch']
        chosen = log[chosen_epoch - 1]
        axes[0].scatter([chosen_epoch], [float(chosen['val_accuracy']) * 100],
                        color=color, marker='*', s=130, edgecolors='black', linewidths=0.5, zorder=5)
    axes[0].set_ylabel('Validation accuracy (%)')
    axes[1].set_ylabel('Validation cross-entropy')
    axes[0].set_title('Stars mark checkpoints selected by validation accuracy')
    axes[1].set_title('Validation loss across the same 20 epochs')
    axes[0].legend(frameon=False)
    figure.suptitle('AG-news TextCNN: fixed split and seed 42')
    figure.savefig(PROJECT / 'experiments/assets/word2vec_validation.png', dpi=180)
    plt.close(figure)
    # 每次实验保存源码和配置，重现时不依赖后续可能改动的工作区。
    sources = ['news_classifier/experiments/controlled.py', 'news_classifier/experiments/word2vec.py',
               'news_classifier/data/dataset.py', 'news_classifier/data/embeddings.py',
               'news_classifier/models/textcnn.py', 'news_classifier/training/engine.py',
               'news_classifier/evaluation/analysis.py', 'experiments/scripts/summarize_word2vec.py',
               'experiments/scripts/verify_word2vec.py']
    for mode in ['random128', 'word2vec128']:
        run = Path(models[mode][0]['checkpoint']).parent
        snapshot = run / 'source_snapshot'
        hashes = {}
        for relative in sources:
            destination = snapshot / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(PROJECT / relative, destination)
            hashes[relative] = hashlib.sha256(destination.read_bytes()).hexdigest()
        write_json(run / 'source_snapshot_sha256.json', hashes)
        config = json.loads((run / 'config.json').read_text(encoding='utf-8'))
        config['data']['cache_dir'] = '../.build/task2/data'
        config['output']['run_dir'] = '../' + run.relative_to(ROOT).as_posix()
        write_json(PROJECT / 'configs' / f'textcnn_ag_news_{mode}_20261103.json', config)
    print(json.dumps({key: summary[key] for key in ['comparisons', 'common_490_followup', 'selected_cases', 'bank_probe']},
                     ensure_ascii=False, indent=2), flush=True)


if __name__ == '__main__':
    main()
