"""从缓存、权重及逐行预测独立核验 Word2Vec 对照，不修改训练结果。"""
from collections import Counter
import csv
import hashlib
import json
from pathlib import Path
import re
import sys

import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score
import torch

PROJECT = Path(__file__).resolve().parents[2]
ROOT = PROJECT.parent
sys.path.insert(0, str(PROJECT))
from news_classifier.data import LABEL_NAMES, tokenize
from news_classifier.evaluation.analysis import cached_split, write_json
from news_classifier.experiments.controlled import tensor_hash
from news_classifier.experiments.word2vec import load_word2vec_initialization
from news_classifier.models import TextCNN


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    torch.set_num_threads(4)
    data = PROJECT / 'experiments/textcnn/error_analysis/data'
    summary = json.loads((data / 'word2vec128/summary.json').read_text(encoding='utf-8'))
    official = cached_split('test')
    labels = np.asarray(official['label'])
    outputs = {}
    checkpoints = {}
    provenances = {}
    splits = {}
    checks = {}
    for name, location in [('original128', 'kernel_comparison/k237'),
                           ('random128', 'random128'), ('word2vec128', 'word2vec128')]:
        folder = data / location
        arrays = np.load(folder / 'predictions.npz')
        with (folder / 'all_predictions.csv').open(encoding='utf-8', newline='') as stream:
            rows = list(csv.DictReader(stream))
        pred = arrays['logits'].argmax(axis=1)
        assert len(rows) == len(pred) == len(labels) == 7600
        assert np.array_equal(arrays['labels'], labels)
        assert np.array_equal(arrays['predictions'], pred)
        for i, (row, original) in enumerate(zip(rows, official)):
            assert row['sample_id'] == f'test:{i}'
            assert row['text'] == row['processed_text'] == original['text']
            assert row['true_label'] == LABEL_NAMES[labels[i]]
            assert row['predicted_label'] == LABEL_NAMES[pred[i]]
            assert (row['correct'] == 'True') == bool(pred[i] == labels[i])
        metrics = summary['models'][name]
        assert metrics['accuracy'] == accuracy_score(labels, pred)
        assert abs(metrics['macro_f1'] - f1_score(labels, pred, average='macro')) < 1e-15
        assert np.array_equal(metrics['confusion_matrix'], confusion_matrix(labels, pred))
        per_class = f1_score(labels, pred, average=None)
        assert np.allclose([item['f1'] for item in metrics['per_class']], per_class, rtol=0, atol=1e-15)
        assert metrics['errors'] == int((labels != pred).sum())
        path = Path(metrics['checkpoint'])
        assert metrics['checkpoint_sha256'] == hashlib.sha256(path.read_bytes()).hexdigest()
        checkpoint = torch.load(path, map_location='cpu', weights_only=True)
        checkpoints[name] = checkpoint
        outputs[name] = pred
        if name != 'original128':
            run = path.parent
            with (run / 'metrics.csv').open(encoding='utf-8') as stream:
                log = list(csv.DictReader(stream))
            assert [int(row['epoch']) for row in log] == list(range(1, 21))
            best = max(log, key=lambda row: (float(row['val_accuracy']), -float(row['val_loss'])))
            assert int(best['epoch']) == checkpoint['epoch'] == metrics['epoch']
            assert float(best['val_accuracy']) == checkpoint['val_accuracy']
            split = np.load(run / 'split_indices.npz')
            assert len(split['train']) == 108000 and len(split['validation']) == 12000
            assert not set(split['train']) & set(split['validation'])
            assert len(set(split['train']) | set(split['validation'])) == 120000
            splits[name] = split
            provenances[name] = json.loads((run / 'provenance.json').read_text(encoding='utf-8'))
            with (folder / 'all_errors.csv').open(encoding='utf-8', newline='') as stream:
                error_rows = list(csv.DictReader(stream))
            assert {row['sample_id'] for row in error_rows} == {
                f'test:{i}' for i in np.flatnonzero(pred != labels)}
            hashes = json.loads((run / 'source_snapshot_sha256.json').read_text(encoding='utf-8'))
            for relative, digest in hashes.items():
                assert digest == hashlib.sha256((run / 'source_snapshot' / relative).read_bytes()).hexdigest()
        checks[name] = dict(samples=7600, errors=metrics['errors'], metrics_independently_recomputed=True)
    random = checkpoints['random128']
    word2vec = checkpoints['word2vec128']
    for key in ['seed', 'model', 'data', 'training']:
        assert random['config'][key] == word2vec['config'][key]
    assert random['vocab'] == word2vec['vocab'] == checkpoints['original128']['vocab']
    assert set(random['model_state_dict']) == set(word2vec['model_state_dict'])
    assert all(random['model_state_dict'][key].shape == word2vec['model_state_dict'][key].shape
               for key in random['model_state_dict'])
    assert provenances['random128']['initial_random_state_sha256'] == provenances['word2vec128']['initial_random_state_sha256']
    assert provenances['random128']['initial_non_embedding_sha256'] == provenances['word2vec128']['initial_non_embedding_sha256']
    for key in ['train', 'validation']:
        assert np.array_equal(splits['random128'][key], splits['word2vec128'][key])
    embedding = summary['embedding']
    pretrained = Path(embedding['vector_path']).parent
    source = embedding['source']
    assert source['corpus_rows'] == 108000 and not source['labels_used'] and not source['external_corpus_used']
    assert source['parameters']['workers'] == 1 and source['parameters']['sg'] == 1
    assert source['parameters']['epochs'] == 10 and source['parameters']['vector_size'] == 128
    split = np.load(pretrained / 'split_indices.npz')
    assert np.array_equal(split['train'], splits['word2vec128']['train'])
    assert np.array_equal(split['validation'], splits['word2vec128']['validation'])
    digest = hashlib.sha256()
    tokens = 0
    for row in cached_split('train').select(split['train']):
        words = tokenize(row['text'])
        digest.update((' '.join(words) + '\n').encode('utf-8'))
        tokens += len(words)
    assert digest.hexdigest() == source['corpus_sha256']
    assert tokens == source['corpus_tokens']
    assert source['model_sha256'] == hashlib.sha256((pretrained / 'word2vec.model').read_bytes()).hexdigest()
    portable_source = summary['pretrained_source_manifest']
    assert portable_source['vectors_sha256'] == source['vectors_sha256']
    assert portable_source['portable_model_sha256'] == hashlib.sha256(
        (pretrained / portable_source['portable_model_file']).read_bytes()).hexdigest()
    from gensim.models import Word2Vec
    portable_model = Word2Vec.load(str(pretrained / portable_source['portable_model_file']))
    assert len(portable_model.wv) == 42394
    torch.manual_seed(42)
    initial = TextCNN(len(word2vec['vocab']), word2vec['config']['model'])
    assert tensor_hash(initial.state_dict()) == provenances['word2vec128']['initial_random_state_sha256']
    weights, _ = load_word2vec_initialization(pretrained / 'vectors.txt', word2vec['vocab'],
                                             initial.embedding.weight.detach(), source['train_indices_sha256'])
    initial.embedding.weight.data.copy_(weights)
    for word, index in word2vec['vocab'].items():
        if index >= 2:
            assert np.array_equal(portable_model.wv[word], weights[index].numpy())
    assert tensor_hash(initial.state_dict()) == provenances['word2vec128']['actual_initial_state_sha256']
    assert torch.count_nonzero(word2vec['model_state_dict']['embedding.weight'][0]) == 0
    assert not torch.equal(weights, word2vec['model_state_dict']['embedding.weight'])
    for name, groups in summary['comparisons'].items():
        before, after = name.split('_to_')
        b = outputs[before] == labels
        c = outputs[after] == labels
        expected = dict(both_correct=int((b & c).sum()), fixed=int((~b & c).sum()),
                        both_wrong=int((~b & ~c).sum()), new_errors=int((b & ~c).sum()))
        assert groups == expected
    kernel = json.loads((data / 'kernel_comparison/summary.json').read_text(encoding='utf-8'))
    common = [int(value.split(':')[1]) for value in kernel['common_sample_ids']]
    assert len(common) == 490
    for name, pred in outputs.items():
        assert summary['common_490_followup'][name]['corrected'] == int((pred[common] == labels[common]).sum())
    verification_path = data / 'word2vec128/verification.json'
    write_json(verification_path, dict(status='checking_report_links'))
    checked_files = [PROJECT / 'news_classifier/README.md', PROJECT / 'experiments/textcnn/error_analysis/README.md',
                     PROJECT / 'experiments/textcnn/error_analysis/2026-11-03_word2vec_textcnn.md',
                     PROJECT / 'experiments/textcnn/error_analysis/2026-11-03_error_analysis.md', PROJECT / 'docs/report.md']
    for path in checked_files:
        content = path.read_bytes()
        assert not content.startswith(b'\xef\xbb\xbf')
        for target in re.findall(r'!?\[[^\]\n]*\]\(([^\)\n]+)\)', content.decode('utf-8')):
            if re.match(r'^[a-zA-Z]+:|^#', target):
                continue
            assert (path.parent / target.split('#')[0]).resolve().exists(), (path, target)
    result = dict(status='passed', models=checks, official_test_rows_checked=22800,
                  pretraining_corpus_rows_rehashed=108000, pretraining_corpus_tokens=tokens,
                  same_architecture_and_training_configuration=True,
                  same_random_and_non_embedding_initialization=True,
                  no_validation_or_test_text_in_word2vec_training=True,
                  embedding_finetuning_confirmed=True,
                  portable_pretrained_model_matches_all_42394_imported_vectors=True,
                  original_control_prediction_disagreements=int((outputs['original128'] != outputs['random128']).sum()),
                  all_new_runs_completed_20_epochs=True, validation_only_checkpoint_selection=True)
    write_json(verification_path, result)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
