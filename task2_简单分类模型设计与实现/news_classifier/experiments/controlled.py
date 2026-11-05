"""固定划分和超参数，执行清洗或词向量单因素对照。

在Task 2目录运行：python -m news_classifier.experiments.controlled --mode cleaning
mode还可选random100、glove100、random128、word2vec128。
"""
import argparse
import copy
import csv
from functools import partial
import hashlib
import json
from pathlib import Path
import platform
import random
import sys
import time

import numpy as np
import torch
from torch.utils.data import DataLoader

from ..data import NewsSample,build_vocab,collate_batch,encode,LABEL_NAMES
from ..training.engine import train_one_epoch,evaluate
from ..evaluation.analysis import ROOT,cached_split,infer_checkpoint,write_json
from ..data.preprocessing import clean_text
from ..data.embeddings import load_pretrained_vectors
from ..models import TextCNN
from ..config import project_path


def tensor_hash(state,exclude_embedding=False):
    digest=hashlib.sha256()
    for name,tensor in sorted(state.items()):
        if exclude_embedding and name.startswith('embedding.'): continue
        digest.update(name.encode());digest.update(tensor.detach().cpu().numpy().tobytes())
    return digest.hexdigest()


def run(mode,epochs=None,smoke=False,output_dir=None,vectors=None):
    source=ROOT/'.build/task2/runs/textcnn_k237_plateau20/best_accuracy.pt'
    source_hash=hashlib.sha256(source.read_bytes()).hexdigest()
    checkpoint=torch.load(source,map_location='cpu',weights_only=True)
    config=copy.deepcopy(checkpoint['config'])
    name='textcnn_k237_'+mode+'_20261103'+('_smoke' if smoke else '')
    run_dir=project_path(output_dir) if output_dir else ROOT/'.build/task2/runs'/name
    if (run_dir/'metrics.csv').exists(): raise FileExistsError(f'保留已有实验，请使用新目录：{run_dir}')
    run_dir.mkdir(parents=True,exist_ok=True)
    config['experiment_name']=name
    config['output']['run_dir']=str(run_dir)
    initialization={'glove100':'glove_6B_100d','word2vec128':'word2vec_ag_news_train_128d'}.get(mode,'random')
    config['experiment']={'clean_text':mode=='cleaning','vocabulary':'fixed_baseline_training_only',
                          'cleaning_version':'known_html_tags_v2',
                          'embedding_initialization':initialization,
                          'freeze_embeddings':False}
    if mode in ['random100','glove100']:config['model']['embed_dim']=100
    if epochs is not None:config['training']['epochs']=epochs
    if smoke:config['training']['epochs']=1
    write_json(run_dir/'config.json',config)
    random.seed(config['seed']);torch.manual_seed(config['seed']);np.random.seed(config['seed'])
    if torch.cuda.is_available():torch.cuda.manual_seed_all(config['seed'])
    torch.set_num_threads(4)
    raw=cached_split('train',config['data']['cache_dir'])
    raw=raw.add_column('source_row',list(range(len(raw))))
    split=raw.train_test_split(test_size=config['data']['val_ratio'],seed=config['seed'],stratify_by_column='label')
    train_ids=np.array(split['train']['source_row']);val_ids=np.array(split['test']['source_row'])
    assert len(train_ids)==108000 and len(val_ids)==12000
    assert len(set(train_ids)&set(val_ids))==0
    assert len(set(train_ids)|set(val_ids))==120000
    train_samples=[NewsSample(r['text'],r['label']) for r in split['train']]
    vocab=checkpoint['vocab']
    assert build_vocab(train_samples,config)==vocab,'训练划分未复现原始词表'
    np.savez_compressed(run_dir/'split_indices.npz',train=train_ids,validation=val_ids)
    model=TextCNN(len(vocab),config['model'],config['data']['pad_id'])
    initial_full_hash=tensor_hash(model.state_dict())
    non_embedding_hash=tensor_hash(model.state_dict(),exclude_embedding=True)
    vector_metadata={}
    if mode=='glove100':
        vector_path=ROOT/'.build/task2/pretrained/glove/glove.6B.100d.txt'
        weights,vector_metadata=load_pretrained_vectors(vector_path,vocab,model.embedding.weight.detach())
        model.embedding.weight.data.copy_(weights)
        vector_metadata['source']=json.loads((vector_path.parent/'source_manifest.json').read_text(encoding='utf-8'))
        write_json(run_dir/'embedding_initialization.json',vector_metadata)
    if mode=='word2vec128':
        from .word2vec import load_word2vec_initialization
        vector_path=project_path(vectors) if vectors else ROOT/'.build/task2/pretrained/word2vec_ag_news128_20261103/vectors.txt'
        weights,vector_metadata=load_word2vec_initialization(
            vector_path,vocab,model.embedding.weight.detach(),hashlib.sha256(train_ids.tobytes()).hexdigest())
        model.embedding.weight.data.copy_(weights)
        write_json(run_dir/'embedding_initialization.json',vector_metadata)
    print(f'{name}: {len(vocab)}词，参数{sum(p.numel() for p in model.parameters())}，epochs={config["training"]["epochs"]}',flush=True)
    process=clean_text if mode=='cleaning' else lambda text:text
    changed={}
    def make_loader(part,shuffle):
        texts=list(part['text']);labels=list(part['label'])
        changed['train' if shuffle else 'validation']=sum(process(t)!=t for t in texts)
        samples=[(encode(process(text),vocab,config['data']['max_length']),y) for text,y in zip(texts,labels)]
        if smoke:samples=samples[:256]
        return DataLoader(samples,batch_size=config['training']['batch_size'],shuffle=shuffle,num_workers=0,
                          collate_fn=partial(collate_batch,min_length=max(config['model']['kernel_sizes'])),
                          generator=torch.Generator().manual_seed(config['seed']))
    train_loader=make_loader(split['train'],True);val_loader=make_loader(split['test'],False)
    device=torch.device('cuda' if torch.cuda.is_available() else 'cpu');model=model.to(device)
    optimizer=torch.optim.Adam(model.parameters(),lr=config['training']['learning_rate'],weight_decay=config['training']['weight_decay'])
    sc=config['training']['scheduler']
    scheduler=torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer,mode='min',factor=sc['factor'],patience=sc['patience'],min_lr=sc['min_lr'])
    manifest=dict(source_checkpoint=str(source),source_checkpoint_sha256=source_hash,
                  initial_random_state_sha256=initial_full_hash,initial_non_embedding_sha256=non_embedding_hash,
                  actual_initial_state_sha256=tensor_hash(model.state_dict()),vocab_size=len(vocab),
                  split_train_sha256=hashlib.sha256(train_ids.tobytes()).hexdigest(),
                  split_validation_sha256=hashlib.sha256(val_ids.tobytes()).hexdigest(),
                  train_samples=len(train_loader.dataset),validation_samples=len(val_loader.dataset),
                  changed_text_rows=changed,python=platform.python_version(),torch=torch.__version__,
                  gpu=torch.cuda.get_device_name() if device.type=='cuda' else 'cpu',embedding=vector_metadata)
    write_json(run_dir/'provenance.json',manifest)
    fields=['epoch','train_loss','train_accuracy','val_loss','val_accuracy','learning_rate']
    best_accuracy=float('-inf');best_loss=float('inf');best_accuracy_loss=float('inf')
    started=time.perf_counter()
    with (run_dir/'metrics.csv').open('w',encoding='utf-8',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=fields);writer.writeheader();stream.flush()
        for epoch in range(1,config['training']['epochs']+1):
            lr=optimizer.param_groups[0]['lr']
            train_metrics=train_one_epoch(model,train_loader,optimizer,device)
            val_metrics=evaluate(model,val_loader,device)
            record=dict(epoch=epoch,train_loss=train_metrics.loss,train_accuracy=train_metrics.accuracy,
                        val_loss=val_metrics.loss,val_accuracy=val_metrics.accuracy,learning_rate=lr)
            writer.writerow(record);stream.flush()
            print(f"Epoch {epoch:02d}/{config['training']['epochs']} | train {train_metrics.loss:.4f}/{train_metrics.accuracy:.4%} | val {val_metrics.loss:.4f}/{val_metrics.accuracy:.4%} | lr {lr:.7f} | {time.perf_counter()-started:.1f}s",flush=True)
            saved=dict(model_state_dict=model.state_dict(),config=config,vocab=vocab,label_names=LABEL_NAMES,
                       epoch=epoch,val_loss=val_metrics.loss,val_accuracy=val_metrics.accuracy,learning_rate=lr)
            if val_metrics.loss<best_loss:
                best_loss=val_metrics.loss;torch.save(dict(saved,selection_metric='val_loss'),run_dir/'best_loss.pt')
            if val_metrics.accuracy>best_accuracy or (val_metrics.accuracy==best_accuracy and val_metrics.loss<best_accuracy_loss):
                best_accuracy=val_metrics.accuracy;best_accuracy_loss=val_metrics.loss
                torch.save(dict(saved,selection_metric='val_accuracy'),run_dir/'best_accuracy.pt')
            scheduler.step(val_metrics.loss)
    write_json(run_dir/'training_execution.json',dict(elapsed_seconds=time.perf_counter()-started,completed_epochs=config['training']['epochs']))
    assert source_hash==hashlib.sha256(source.read_bytes()).hexdigest()
    if not smoke:
        output=(run_dir/'evaluation') if output_dir else ROOT/'task2_简单分类模型设计与实现/experiments/textcnn/error_analysis/data'/mode
        infer_checkpoint(run_dir/'best_accuracy.pt',output)
    return run_dir


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mode',choices=['cleaning','random100','glove100','random128','word2vec128'],required=True)
    parser.add_argument('--smoke',action='store_true')
    parser.add_argument('--run-dir',help='新的输出目录，相对Task 2目录解析；不覆盖已有实验')
    parser.add_argument('--epochs',type=int,help='覆盖训练轮数，默认沿用原始20轮')
    parser.add_argument('--vectors',help='Word2Vec vectors.txt路径，需配套来源清单；相对Task 2目录解析')
    args=parser.parse_args();run(args.mode,epochs=args.epochs,smoke=args.smoke,output_dir=args.run_dir,vectors=args.vectors)


if __name__=='__main__':main()
