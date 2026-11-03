"""把三步TextCNN对照的实际结果追加到同一份错误分析报告。"""
import csv
from collections import Counter
import json
from pathlib import Path
import re
import sys

import numpy as np

PROJECT=Path(__file__).resolve().parents[2]
ROOT=PROJECT.parent
sys.path.insert(0,str(PROJECT))
from news_classifier.data import LABEL_NAMES,tokenize
from news_classifier.evaluation.analysis import classification_metrics,error_groups,write_csv,write_json

DATA=PROJECT/'experiments/error_analysis/data'
REPORT=PROJECT/'experiments/error_analysis/2026-11-03_error_analysis.md'


def table(headers,rows):
    return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']+
                     ['| '+' | '.join(map(str,row))+' |' for row in rows])


def load(folder):
    metrics=json.loads((folder/'metrics.json').read_text(encoding='utf-8'))
    saved=np.load(folder/'predictions.npz')
    rows=list(csv.DictReader((folder/'all_predictions.csv').open(encoding='utf-8')))
    return metrics,saved['labels'],saved['predictions'],rows


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    kernel=json.loads((DATA/'kernel_comparison/summary.json').read_text(encoding='utf-8'))
    base,labels,baseline,rows=load(DATA/'kernel_comparison/k237')
    models={'raw128':(base,baseline,rows)}
    for mode in ['cleaning','random100','glove100']:
        metrics,ys,pred,cases=load(DATA/mode)
        assert np.array_equal(labels,ys)
        assert [r['text'] for r in rows]==[r['text'] for r in cases]
        models[mode]=(metrics,pred,cases)
    results={}
    comparisons=[('raw128','cleaning'),('raw128','random100'),('random100','glove100'),('raw128','glove100')]
    for a,b in comparisons:
        groups=error_groups(labels,models[a][1],models[b][1])
        results[a+'_to_'+b]={k:len(v) for k,v in groups.items()}
        target=DATA/b
        for kind in ['fixed','both_wrong','new_errors']:
            cases=[]
            for i in groups[kind]:
                cases.append(dict(sample_id=f'test:{i}',true_label=LABEL_NAMES[labels[i]],
                                  baseline_prediction=LABEL_NAMES[models[a][1][i]],candidate_prediction=LABEL_NAMES[models[b][1][i]],
                                  baseline_confidence=models[a][2][i]['confidence'],candidate_confidence=models[b][2][i]['confidence'],
                                  text=rows[i]['text']))
            write_csv(target/f'{a}_to_{b}_{kind}.csv',cases)
    artifact=np.array([bool(re.search(r'&(?:[a-z]+|#\d+);|#\d+;?|\b(?:quot|amp|lt|gt)\b',r['text'],re.I)) for r in rows])
    short=np.array([len(tokenize(r['text']))<=20 for r in rows])
    segments=[]
    for label,mask in [('含编码痕迹',artifact),('无编码痕迹',~artifact),('不超过20词',short),('超过20词',~short)]:
        for name,(metrics,pred,cases) in models.items():
            count=int(mask.sum());errors=int(((pred!=labels)&mask).sum())
            segments.append(dict(segment=label,model=name,samples=count,errors=errors,error_rate=errors/count))
    write_csv(DATA/'controlled_feature_segments.csv',segments)
    clean_rows=models['cleaning'][2]
    token_changes=sum(tokenize(r['text'])!=tokenize(c['processed_text']) for r,c in zip(rows,clean_rows))
    common_ids=set(int(s.split(':')[1]) for s in kernel['common_sample_ids'])
    persistence=[]
    for name,(metrics,pred,cases) in models.items():
        wrong=set(np.flatnonzero(pred!=labels).tolist())
        persistence.append(dict(model=name,corrected_common_errors=len(common_ids-wrong),remaining_common_errors=len(common_ids&wrong)))
    summary=dict(models={k:v[0] for k,v in models.items()},comparisons=results,feature_segments=segments,
                 test_token_sequences_changed_by_cleaning=token_changes,common_error_followup=persistence)
    write_json(DATA/'followup_summary.json',summary)
    model_names={'raw128':'原始随机128维','cleaning':'统一清洗128维','random100':'随机100维对照','glove100':'GloVe100维可训练'}
    headline=table(['方案','选定轮次','验证准确率','测试准确率','错误数','macro-F1','商业↔科技'],[
        [model_names[name],metrics['epoch'],f"{metrics['val_accuracy']:.4%}",f"{metrics['accuracy']:.4%}",metrics['errors'],f"{metrics['macro_f1']:.4%}",metrics['business_scitech_confusions']]
        for name,(metrics,_,_) in models.items()])
    transition=table(['对照 → 实验','修正旧错误','共同错误','新增错误','净减少错误'],[
        [model_names[a]+' → '+model_names[b],results[a+'_to_'+b]['fixed'],results[a+'_to_'+b]['both_wrong'],results[a+'_to_'+b]['new_errors'],
         results[a+'_to_'+b]['fixed']-results[a+'_to_'+b]['new_errors']] for a,b in comparisons])
    per_class=table(['方案']+list(LABEL_NAMES),[[model_names[name]]+[f"{r['f1']:.4%}" for r in metrics['per_class']]
                                           for name,(metrics,_,_) in models.items()])
    kernel_table=table(['卷积核','测试错误','测试准确率','macro-F1','仅该模型错误'],[
        ['/'.join(key[1:]),m['errors'],f"{m['accuracy']:.4%}",f"{m['macro_f1']:.4%}",kernel['unique_errors'][key]] for key,m in kernel['models'].items()])
    kernel_transitions=table(['卷积核变更','修正旧错误','共同错误','新增错误','净减少错误'],[
        [name.replace('_to_',' → '),v['fixed'],v['both_wrong'],v['new_errors'],v['fixed']-v['new_errors']] for name,v in kernel['pairwise'].items()])
    common_rows=list(csv.DictReader((DATA/'kernel_comparison/common_errors.csv').open(encoding='utf-8')))
    same_wrong=sum(r['k345_prediction']==r['k246_prediction']==r['k237_prediction'] for r in common_rows)
    common_classes=Counter(r['true_label'] for r in common_rows)
    class_common=table(['共同错误的真实类别','数量'],[[name,common_classes[name]] for name in LABEL_NAMES])
    common_examples=[]
    for sample_id in ['test:83','test:139','test:1840','test:4359','test:5467','test:2656','test:4097']:
        i=int(sample_id.split(':')[1]);r=rows[i]
        kernel_predictions=[]
        for key in ['k345','k246','k237']:
            p=np.load(DATA/f'kernel_comparison/{key}/predictions.npz')['predictions'][i]
            kernel_predictions.append(LABEL_NAMES[p])
        common_examples.append([sample_id,r['true_label']]+kernel_predictions+[LABEL_NAMES[models['cleaning'][1][i]],LABEL_NAMES[models['glove100'][1][i]]])
    case_matrix=table(['样本','真实类','3/4/5','2/4/6','2/3/7','清洗','GloVe100'],common_examples)
    persistence_table=table(['方案','修正的三卷积核共同错误','仍然错误'],[
        [model_names[r['model']],r['corrected_common_errors'],r['remaining_common_errors']] for r in persistence])
    selected=[]
    # Deterministic examples from every kind of change, including regressions.
    for a,b in [('raw128','cleaning'),('random100','glove100')]:
        groups=error_groups(labels,models[a][1],models[b][1])
        for kind in ['fixed','new_errors']:
            ranked=sorted(groups[kind],key=lambda i:-float(models[b][2][i]['confidence']))[:2]
            for i in ranked:
                selected += [f"### test:{i}：{model_names[a]} → {model_names[b]}，{'修正' if kind=='fixed' else '新增错误'}",'',
                             f"真实类 {LABEL_NAMES[labels[i]]}；原预测 {LABEL_NAMES[models[a][1][i]]}；新预测 {LABEL_NAMES[models[b][1][i]]}；新预测置信度 {float(models[b][2][i]['confidence']):.4f}。",'',rows[i]['text'],'']
    provenance={}
    for mode in ['cleaning','random100','glove100']:
        path=Path(models[mode][0]['checkpoint']).parent
        provenance[mode]=json.loads((path/'provenance.json').read_text(encoding='utf-8'))
        config=json.loads((path/'config.json').read_text(encoding='utf-8'))
        # Store a runnable copy in the config directory; its completed output is protected from overwrite.
        relative=json.loads(json.dumps(config))
        relative['data']['cache_dir']='../.build/task2/data'
        relative['output']['run_dir']='../'+path.relative_to(ROOT).as_posix()
        write_json(PROJECT/'configs'/f'textcnn_ag_news_{mode}_20261103.json',relative)
    coverage=provenance['glove100']['embedding']
    cleaning_effect=results['raw128_to_cleaning'];embedding_effect=results['random100_to_glove100']
    clean_summary=(f"统一清洗使测试错误从607变为{models['cleaning'][0]['errors']}，修正{cleaning_effect['fixed']}条旧错误，同时新增{cleaning_effect['new_errors']}条。"
                   f"本次{'取得改善' if models['cleaning'][0]['errors']<607 else '没有超过原始最优模型'}，因此不能根据编码片段个例就假定清洗一定提高整体表现。")
    embedding_summary=(f"在同为100维、其他设置一致的对照中，GloVe将错误从{models['random100'][0]['errors']}变为{models['glove100'][0]['errors']}，"
                       f"修正{embedding_effect['fixed']}条旧错误，新增{embedding_effect['new_errors']}条；"
                       f"商业与科技双向混淆从{models['random100'][0]['business_scitech_confusions']}变为{models['glove100'][0]['business_scitech_confusions']}。")
    feature_table=table(['特征组','样本数','原始错误 / 错误率','清洗错误 / 错误率'],[
        [name,next(r['samples'] for r in segments if r['segment']==name),
         next(f"{r['errors']} / {r['error_rate']:.2%}" for r in segments if r['segment']==name and r['model']=='raw128'),
         next(f"{r['errors']} / {r['error_rate']:.2%}" for r in segments if r['segment']==name and r['model']=='cleaning')]
        for name in ['含编码痕迹','无编码痕迹','不超过20词','超过20词']])
    addition=f'''
## 9. 三种卷积核模型的错误集合比较

按老师的要求，我先比较已经保存的3/4/5、2/4/6、2/3/7三种卷积核模型。三组训练设置、随机种子、词表、参数量与测试样本顺序均核对一致，区别是卷积核宽度。每组都使用按最高验证准确率选出的权重，未重新训练，也没有借测试集重新选择轮次。

{kernel_table}

至少被一组分错的新闻共762条，其中490条三组都错，106条恰好两组错，166条只在一组出错。三组都正确的有6838条。490条共同错误占最优2/3/7模型607条错误的80.72%；“换一种卷积核就能解决”只适用于部分案例，不能据此认为换成其他模型家族也会得到同样结果。

{class_common}

490条共同错误中，有{same_wrong}条三组给出完全相同的错误类别，其余共同错误的预测类别存在分歧。这比仅看整体准确率更能区分共同困难样本和结构敏感样本。

{kernel_transitions}

例如，从3/4/5换到2/3/7虽然净减少11条错误，实际发生了106条修正与95条新增错误；整体准确率的小幅提高，并不表示原来的错误几乎都被保留或单向改善。

完整结果：[共同错误](data/kernel_comparison/common_errors.csv)、[错误并集](data/kernel_comparison/error_union.csv)、[3/4/5独有错误](data/kernel_comparison/k345_unique_errors.csv)、[2/4/6独有错误](data/kernel_comparison/k246_unique_errors.csv)、[2/3/7独有错误](data/kernel_comparison/k237_unique_errors.csv)。

## 10. 统一清洗的单因素对照

固定2/3/7、128维词向量、每分支128通道、Dropout0.5、Adam学习率0.001、weight decay0.0001、batch64、20轮和原有学习率调度。清洗规则只做已知HTML实体修复、常见HTML标签去除与空白规范化，保留普通词、数字、新闻内容及标签；训练、验证、测试和单条预测使用相同规则。

初版清洗会把`<CIEN.O>`等股票代码误当作HTML标签；核验后已将规则收紧为常见HTML标签白名单，并增加测试。下表使用修正后的`known_html_tags_v2`重新训练结果；初版日志和权重保留在`.build/task2/runs/textcnn_k237_cleaning_20261103/`，不混入正式对照。权重会记录清洗版本，推理按对应版本恢复规则。

为了更严格控制变量，清洗组沿用仅由原训练集建立的42396项词表，保持初始随机参数和词编号不变。未因清洗重新生成词表。原始训练集108000条和验证集12000条的行号保持一致，测试集仍是原始7600条。清洗改变了{token_changes}条测试文本的实际分词序列；仅空白变化不会改变模型输入。

{clean_summary}

{feature_table}

表中的“含编码痕迹”按清洗前原文分组，组内分母固定，不随着模型预测变化。整体变化既包括样本输入变化，也包括模型重新学习后的参数变化；不能把某一条修正直接归因于删掉某个编码token。

## 11. 预训练词向量对照

使用官方[Stanford GloVe 6B](https://nlp.stanford.edu/projects/glove/)的100维词向量。原始最优模型是128维，因此新增随机100维对照，先保持维度一致，再比较随机初始化与GloVe初始化。其余卷积核、通道数、Dropout、优化器、学习率、训练轮数、调度器、划分和词表相同；两组均不清洗文本，词向量均继续参与训练，没有额外冻结实验。

GloVe覆盖{coverage['matched_words']}/{coverage['ordinary_vocab_size']}个普通词表项（{coverage['type_coverage']:.2%}）；未覆盖词保留与随机100维对照相同的初始化，PAD保持全零。两组非嵌入参数的初始SHA-256相同。预训练文件来自固定revision `{coverage['source']['revision']}`，压缩包与向量文件哈希保留在来源清单中。

{headline}

{embedding_summary}

原始128维与100维方案之间同时存在维度差异，因此不能把GloVe100维相对原始最优模型的全部变化都归因于预训练；预训练效应主要看随机100维与GloVe100维之间的比较。GloVe还使用了额外的外部无监督语料，本次不是仅改变随机初始化方式而保持训练数据总来源相同的比较。该实验思路参考[TextCNN原论文](https://aclanthology.org/D14-1181/)。

各类F1如下：

{per_class}

{transition}

## 12. 同一条新闻在不同方案下的预测

{case_matrix}

对于三种卷积核共同分错的490条样本，后续方案的变化如下：

{persistence_table}

共同错误表示当前这些模型的共同困难样本，不表示这些数据在任何结构和训练方式下都无法学会。局部修正也不保证整体改善，还要同时检查新增错误。

上表继续使用原始测试行号，保留所有原始类别。对语义边界与疑似标注口径问题，仍只标为复核候选，不修改标签。完整转换清单分别保存在[data/cleaning](data/cleaning/)、[data/random100](data/random100/)和[data/glove100](data/glove100/)，每组含全部7600条预测、全部错误、混淆矩阵和修正/新增错误原文。

以下例子按对应分组中新模型置信度从高到低各取2条，既列修正，也列新增错误。它们是查阅入口，不能代表错误机制的总体占比。

{chr(10).join(selected)}

## 13. 本轮核验与复现

三组新训练都完整运行20轮，按最高验证准确率、并列时最低验证损失选权重；测试结果未参与选模。分别核对训练/验证行号无重叠、词表一致、20轮CSV与所选权重、全部7600条原文与标签、错误四分组总数和混淆矩阵。原有三组卷积核权重哈希不变。结果仍是seed42单次实验，没有据微小差值推断稳定性或统计显著性。

```powershell
# 在仓库根目录比较已有三组卷积核
python task2_简单分类模型设计与实现/experiments/scripts/compare_error_sets.py
# 进入Task 2目录后运行新实验；已完成目录受保护，复现须选择新输出目录
python -m news_classifier.experiments.controlled --mode cleaning --run-dir ../.build/task2/runs/cleaning_repro
python -m news_classifier.experiments.controlled --mode random100 --run-dir ../.build/task2/runs/random100_repro
python -m news_classifier.experiments.controlled --mode glove100 --run-dir ../.build/task2/runs/glove100_repro
# 在仓库根目录重建本轮分析章节
python task2_简单分类模型设计与实现/experiments/scripts/summarize_followups.py
```

训练日志、完整配置、split_indices.npz、初始化哈希和模型位于`.build/task2/runs/textcnn_k237_<mode>_20261103/`。结构与代码入口见[源码说明](../../news_classifier/README.md)，调参报告位于[独立分类目录](../tuning/README.md)。本轮没有使用BERT，也没有生成PDF。
'''
    original=REPORT.read_text(encoding='utf-8').split('\n## 9. 三种卷积核模型的错误集合比较')[0]
    original=original.replace('本次按老师的建议，将分析重点从整体准确率转向具体错误。',
        '第1—8节记录首轮最优模型错误分析，第9—13节补充卷积核、统一清洗和预训练词向量对照。首轮按老师的建议，将分析重点从整体准确率转向具体错误。')
    original=original.replace('本次没有重新训练、搜索新参数或修改原始标签。','首轮仅做推理和错误诊断；后续训练结果见第10—13节，所有实验均保留原始标签。')
    original=original.replace('本次只分析最优模型，尚不能判断哪些样本是多种结构共有的困难样本；跨结构结论需要另外逐样本对齐其他模型预测。',
        '首轮只分析最优模型；后续第9节补充三种TextCNN卷积核变体的逐样本对比。')
    original=original.replace('但本次实验没有比较其他结构，不能把结构本身当作已经证实的原因。',
        '后续只比较了卷积核变体，仍不能把结构本身当作已经证实的原因。')
    original=original.replace('这次先完成单个最优模型的全部错误提取和共性分析。它无法回答“哪些数据在各种结构下都学不好、哪些只在特定结构下学不好”；那需要固定测试样本编号后，再逐样本对齐其他模型的结果。本次不据单模型结果作跨结构判断，也没有为了得到更低准确率而更换数据集。',
        '首轮完成单个最优模型的全部错误提取和共性分析；后续第9节固定测试样本编号，对齐三种卷积核的预测，区分共同错误与各模型独有错误。结论限定于这些TextCNN变体，没有为了得到更低准确率而更换数据集。')
    original=original.replace('python task2_简单分类模型设计与实现/experiments/analyze_errors.py --occlusion\npython task2_简单分类模型设计与实现/experiments/analyze_error_patterns.py',
        'python task2_简单分类模型设计与实现/experiments/scripts/compare_error_sets.py')
    original=original.replace('复现时在仓库根目录使用 d2l-pytorch 环境运行：','后续对齐复核可在仓库根目录使用 d2l-pytorch 环境运行：')
    REPORT.write_text(original.rstrip()+'\n'+addition,encoding='utf-8')
    print(headline,flush=True);print(transition,flush=True)


if __name__=='__main__':main()
