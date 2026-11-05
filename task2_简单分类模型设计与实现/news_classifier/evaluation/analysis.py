"""分类模型逐样本预测导出、指标统计和错误集合比较。"""
import csv
from functools import partial
import hashlib
import json
from pathlib import Path

import numpy as np
import torch
from datasets import Dataset
from torch.utils.data import DataLoader

from ..data import LABEL_NAMES, collate_batch, encode
from ..models import build_model
from ..config import min_sequence_length
from ..data.preprocessing import clean_text

ROOT=Path(__file__).resolve().parents[3]



def error_groups(labels,baseline,candidate):
    if not len(labels)==len(baseline)==len(candidate):
        raise ValueError('预测与真实标签长度必须一致')
    groups={name:[] for name in ['both_correct','fixed','both_wrong','new_errors']}
    for i,(y,b,c) in enumerate(zip(labels,baseline,candidate)):
        key=('both_correct' if b==y else 'fixed') if c==y else ('new_errors' if b==y else 'both_wrong')
        groups[key].append(i)
    return groups


def classification_metrics(labels,predictions):
    labels=np.asarray(labels,dtype=np.int64)
    predictions=np.asarray(predictions,dtype=np.int64)
    if labels.shape!=predictions.shape or not len(labels):
        raise ValueError('真实标签和预测必须非空且形状一致')
    cm=np.zeros((4,4),dtype=np.int64)
    np.add.at(cm,(labels,predictions),1)
    classes=[]
    for c,name in enumerate(LABEL_NAMES):
        correct=int(cm[c,c]); support=int(cm[c].sum()); selected=int(cm[:,c].sum())
        precision=correct/selected if selected else 0.
        recall=correct/support if support else 0.
        f1=2*precision*recall/(precision+recall) if precision+recall else 0.
        classes.append(dict(label=name,support=support,errors=support-correct,precision=precision,recall=recall,f1=f1))
    return dict(num_samples=len(labels),correct=int(cm.trace()),errors=int(len(labels)-cm.trace()),
                accuracy=float(cm.trace()/len(labels)),macro_f1=float(np.mean([r['f1'] for r in classes])),
                business_scitech_confusions=int(cm[2,3]+cm[3,2]),confusion_matrix=cm.tolist(),per_class=classes)



def write_json(path,value):
    Path(path).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')


def write_csv(path,rows):
    if not rows: return
    with Path(path).open('w',encoding='utf-8',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=list(rows[0]))
        writer.writeheader();writer.writerows(rows)


def cached_split(name,cache_dir=None):
    cache_dir=Path(cache_dir or ROOT/'.build/task2/data')
    paths=list(cache_dir.rglob(f'ag_news-{name}.arrow'))
    if len(paths)!=1: raise RuntimeError(f'找不到唯一的官方{name}缓存：{paths}')
    return Dataset.from_file(str(paths[0]))


def infer_checkpoint(path,output):
    """恢复配置和词表，按官方测试行号保存全部预测；不覆盖原测试指标。"""
    path=Path(path).resolve();output=Path(output)
    output.mkdir(parents=True,exist_ok=True)
    digest=hashlib.sha256(path.read_bytes()).hexdigest()
    checkpoint=torch.load(path,map_location='cpu',weights_only=True)
    config=checkpoint['config'];vocab=checkpoint['vocab']
    dataset=cached_split('test',config['data']['cache_dir'])
    texts=list(dataset['text']);labels=list(dataset['label'])
    experiment=config.get('experiment',{})
    process=partial(clean_text,version=experiment.get('cleaning_version','legacy_all_tags_v1')) if experiment.get('clean_text',False) else lambda text:text
    samples=[(encode(process(text),vocab,config['data']['max_length']),y) for text,y in zip(texts,labels)]
    loader=DataLoader(samples,batch_size=config['training']['batch_size'],shuffle=False,num_workers=0,
                      collate_fn=partial(collate_batch,min_length=min_sequence_length(config['model'])))
    device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model=build_model(len(vocab),config['model'],config['data']['pad_id']).to(device)
    model.load_state_dict(checkpoint['model_state_dict']);model.eval()
    logits=[]
    with torch.inference_mode():
        for ids,lengths,_ in loader: logits.append(model(ids.to(device),lengths.to(device)).cpu())
    logits=torch.cat(logits);probabilities=logits.softmax(1).numpy();predictions=probabilities.argmax(1)
    metrics=classification_metrics(labels,predictions)
    metrics['loss']=float(torch.nn.functional.cross_entropy(logits,torch.tensor(labels)))
    metrics.update(epoch=checkpoint['epoch'],val_accuracy=checkpoint['val_accuracy'],
                   parameters=sum(p.numel() for p in model.parameters()),checkpoint=str(path),checkpoint_sha256=digest)
    rows=[]
    for i,text in enumerate(texts):
        rows.append(dict(sample_id=f'test:{i}',test_index=i,true_label=LABEL_NAMES[labels[i]],
                         predicted_label=LABEL_NAMES[predictions[i]],correct=bool(labels[i]==predictions[i]),
                         confidence=float(probabilities[i].max()),
                         **{f'prob_{name}':float(probabilities[i,c]) for c,name in enumerate(LABEL_NAMES)},
                         processed_text=process(text),text=text))
    write_csv(output/'all_predictions.csv',rows)
    write_csv(output/'all_errors.csv',[r for r in rows if not r['correct']])
    write_json(output/'metrics.json',metrics)
    np.savez_compressed(output/'predictions.npz',labels=np.array(labels),predictions=predictions,
                        logits=logits.numpy(),probabilities=probabilities)
    assert digest==hashlib.sha256(path.read_bytes()).hexdigest()
    print(f'{path.parent.name}: {metrics["correct"]}/{len(texts)}, errors={metrics["errors"]}, macro-F1={metrics["macro_f1"]:.6f}',flush=True)
    return metrics,predictions,rows
