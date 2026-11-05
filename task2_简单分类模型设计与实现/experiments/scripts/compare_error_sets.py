"""按固定官方测试行号比较已有3种TextCNN卷积核的错误集合。"""
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys
import numpy as np
import torch

PROJECT=Path(__file__).resolve().parents[2]
ROOT=PROJECT.parent
sys.path.insert(0,str(PROJECT))
from news_classifier.evaluation.analysis import infer_checkpoint,write_csv,write_json,error_groups


def main():
    sys.stdout.reconfigure(encoding='utf-8');torch.set_num_threads(4)
    output=PROJECT/'experiments/textcnn/error_analysis/data/kernel_comparison'
    output.mkdir(parents=True,exist_ok=True)
    models={'k345':'textcnn_plateau20','k246':'textcnn_k246_plateau20','k237':'textcnn_k237_plateau20'}
    metrics={};predictions={};source=None;all_rows=None
    for key,run in models.items():
        path=ROOT/'.build/task2/runs'/run/'best_accuracy.pt'
        checkpoint=torch.load(path,map_location='cpu',weights_only=True)
        comparable={k:v for k,v in checkpoint['config'].items() if k not in ('experiment_name','output')}
        comparable['model']=dict(comparable['model']);comparable['model'].pop('kernel_sizes')
        if source is None: source=(comparable,checkpoint['vocab'])
        else: assert source==(comparable,checkpoint['vocab']), '三组训练设置或词表不一致'
        metrics[key],predictions[key],rows=infer_checkpoint(path,output/key)
        expected=json.loads((path.parent/'test_metrics.json').read_text(encoding='utf-8'))
        assert metrics[key]['accuracy']==expected['accuracy']
        if all_rows is not None:
            assert [r['text'] for r in all_rows]==[r['text'] for r in rows]
        all_rows=rows
    labels=np.load(output/'k237/predictions.npz')['labels']
    old=np.load(ROOT/'.build/task2/error_analysis/2026-11-03/predictions.npz')
    assert np.array_equal(old['predictions'],predictions['k237'])
    errors={key:set(np.flatnonzero(pred!=labels).tolist()) for key,pred in predictions.items()}
    common=set.intersection(*errors.values());union=set.union(*errors.values())
    unique={key:sorted(group-set.union(*(errors[other] for other in errors if other!=key))) for key,group in errors.items()}
    comparisons={}
    for a,b in [('k345','k246'),('k345','k237'),('k246','k237')]:
        groups=error_groups(labels,predictions[a],predictions[b])
        comparisons[a+'_to_'+b]={key:len(ids) for key,ids in groups.items()}
        for kind in ['fixed','new_errors']:
            write_csv(output/f'{a}_to_{b}_{kind}.csv',[dict(all_rows[i],baseline_prediction=['World','Sports','Business','Sci/Tech'][predictions[a][i]],
                       candidate_prediction=['World','Sports','Business','Sci/Tech'][predictions[b][i]]) for i in groups[kind]])
    combined=[]
    for i in sorted(union):
        row=dict(all_rows[i]);row.pop('correct');row.pop('predicted_label');row.pop('confidence')
        for name,pred in predictions.items():
            row[name+'_prediction']=['World','Sports','Business','Sci/Tech'][pred[i]]
            row[name+'_wrong']=i in errors[name]
        row['wrong_model_count']=sum(i in group for group in errors.values())
        combined.append(row)
    write_csv(output/'error_union.csv',combined)
    write_csv(output/'common_errors.csv',[r for r in combined if r['test_index'] in common])
    for name,ids in unique.items():write_csv(output/f'{name}_unique_errors.csv',[r for r in combined if r['test_index'] in ids])
    summary=dict(models=metrics,common_errors=len(common),union_errors=len(union),
                 all_correct=len(labels)-len(union),unique_errors={k:len(v) for k,v in unique.items()},
                 error_multiplicity=dict(Counter(r['wrong_model_count'] for r in combined)),
                 pairwise=comparisons,common_sample_ids=[f'test:{i}' for i in sorted(common)],
                 comparison_scope='仅三种TextCNN卷积核变体，固定单种子；不含BERT或其他模型家族')
    write_json(output/'summary.json',summary)
    print(json.dumps({k:v for k,v in summary.items() if k not in ['models','common_sample_ids']},ensure_ascii=False,indent=2),flush=True)


if __name__=='__main__':main()
