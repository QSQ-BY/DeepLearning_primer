"""独立核对对照实验的来源、选模、全部预测、指标及目录链接。"""
from collections import Counter
import csv
import hashlib
import json
from pathlib import Path
import re
import sys

import numpy as np
import torch

PROJECT=Path(__file__).resolve().parents[2]
ROOT=PROJECT.parent
sys.path.insert(0,str(PROJECT))
from news_classifier.data import LABEL_NAMES
from news_classifier.evaluation.analysis import cached_split
from news_classifier.experiments.controlled import tensor_hash
from news_classifier.models import TextCNN


def main():
    sys.stdout.reconfigure(encoding='utf-8');torch.set_num_threads(4)
    data=PROJECT/'experiments/textcnn/error_analysis/data'
    source=cached_split('test')
    kernel=json.loads((data/'kernel_comparison/summary.json').read_text(encoding='utf-8'))
    checks={};split_reference=None;initial100=None
    for name,folder in [('k345',data/'kernel_comparison/k345'),('k246',data/'kernel_comparison/k246'),
                         ('k237',data/'kernel_comparison/k237'),('cleaning',data/'cleaning'),
                         ('random100',data/'random100'),('glove100',data/'glove100')]:
        metrics=json.loads((folder/'metrics.json').read_text(encoding='utf-8'))
        arrays=np.load(folder/'predictions.npz')
        rows=list(csv.DictReader((folder/'all_predictions.csv').open(encoding='utf-8')))
        error_rows=list(csv.DictReader((folder/'all_errors.csv').open(encoding='utf-8')))
        assert len(rows)==len(source)==7600
        cm=Counter();wrong=set()
        pred=arrays['logits'].argmax(1)
        for i,(record,item) in enumerate(zip(rows,source)):
            y=item['label'];p=int(pred[i])
            assert record['sample_id']==f'test:{i}' and record['text']==item['text']
            assert record['true_label']==LABEL_NAMES[y] and record['predicted_label']==LABEL_NAMES[p]
            assert arrays['labels'][i]==y and arrays['predictions'][i]==p
            assert (record['correct']=='True')==(y==p)
            cm[y,p]+=1
            if y!=p:wrong.add(f'test:{i}')
        expected=[[cm[i,j] for j in range(4)] for i in range(4)]
        assert metrics['confusion_matrix']==expected
        assert len(wrong)==metrics['errors']==len(error_rows)
        assert wrong=={r['sample_id'] for r in error_rows}
        assert abs(metrics['accuracy']-(7600-len(wrong))/7600)<1e-12
        assert metrics['business_scitech_confusions']==cm[2,3]+cm[3,2]
        f1s=[]
        for c in range(4):
            tp=cm[c,c];fp=sum(cm[r,c] for r in range(4) if r!=c);fn=sum(cm[c,j] for j in range(4) if j!=c)
            f1s.append(2*tp/(2*tp+fp+fn))
        assert abs(metrics['macro_f1']-sum(f1s)/4)<1e-12
        path=Path(metrics['checkpoint'])
        assert hashlib.sha256(path.read_bytes()).hexdigest()==metrics['checkpoint_sha256']
        checkpoint=torch.load(path,map_location='cpu',weights_only=True)
        if name in ['cleaning','random100','glove100']:
            log=list(csv.DictReader((path.parent/'metrics.csv').open(encoding='utf-8')))
            assert len(log)==20 and [int(r['epoch']) for r in log]==list(range(1,21))
            chosen=max(log,key=lambda row:(float(row['val_accuracy']),-float(row['val_loss'])))
            assert int(chosen['epoch'])==checkpoint['epoch']==metrics['epoch']
            assert float(chosen['val_accuracy'])==checkpoint['val_accuracy']
            split=np.load(path.parent/'split_indices.npz')
            assert len(split['train'])==108000 and len(split['validation'])==12000
            assert len(set(split['train'])&set(split['validation']))==0
            if split_reference is None:split_reference=(split['train'],split['validation'])
            else:
                assert np.array_equal(split_reference[0],split['train'])
                assert np.array_equal(split_reference[1],split['validation'])
            provenance=json.loads((path.parent/'provenance.json').read_text(encoding='utf-8'))
            if name in ['random100','glove100']:
                if initial100 is None:initial100=provenance['initial_non_embedding_sha256']
                else:assert initial100==provenance['initial_non_embedding_sha256']
            torch.manual_seed(42)
            initial=TextCNN(len(checkpoint['vocab']),checkpoint['config']['model'])
            assert tensor_hash(initial.state_dict())==provenance['initial_random_state_sha256']
        checks[name]=dict(samples=7600,errors=len(wrong),accuracy=metrics['accuracy'],source_rows_checked=7600,
                          checkpoint_hash_unchanged=True)
    missing=[]
    files=[ROOT/'README.md']+list(PROJECT.rglob('*.md'))
    for path in files:
        text=path.read_text(encoding='utf-8')
        for link in re.findall(r'!?\[[^\]\n]*\]\(([^\)\n]+)\)',text):
            if re.match(r'^[a-zA-Z]+:|^#',link):continue
            target=link.split('#')[0]
            if not (path.parent/target).resolve().exists():missing.append((str(path),target))
    if missing:raise AssertionError(f'失效链接：{missing}')
    assert not list((PROJECT/'experiments').rglob('*.pdf'))
    assert not (PROJECT/'news_classifier/data.py').exists()
    assert (PROJECT/'news_classifier/data/dataset.py').is_file()
    assert len(list((PROJECT/'experiments/textcnn/tuning').glob('2026-11-01*.md')))==11
    result=dict(status='passed',models=checks,source_rows_compared=7600*6,
                all_three_new_runs_completed_20_epochs=True,shared_train_validation_indices=True,
                random100_glove100_non_embedding_initialization_identical=True,missing_markdown_links=0,
                tuning_reports_preserved=12,no_generated_pdf=True)
    (data/'verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__=='__main__':main()
