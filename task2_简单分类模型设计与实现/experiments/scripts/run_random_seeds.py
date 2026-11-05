"""三个预先固定的训练种子；保持数据划分与模型超参数，最多两个 GPU 训练进程。"""

import argparse
import copy
from datetime import datetime, timezone
import hashlib
import importlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time
import traceback

PROJECT = Path(__file__).resolve().parents[2]
ROOT = PROJECT.parent
OUT = PROJECT / "experiments/random_seeds"
RUNS = ROOT / ".build/task2/runs/random_seeds_20261103"
SEEDS = (17, 2024, 3407)
BASES = {"textcnn": "textcnn_ag_news_k237_plateau20.json",
         "bilstm": "bilstm_es_dropout02_20261103.json"}
sys.path.insert(0, str(PROJECT))


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare():
    protocol = dict(training_seeds=list(SEEDS), split_seed=42, historical_seed=42,
                    training_count=6, dataset="fancyzhx/ag_news", max_parallel=2,
                    selection="max val_accuracy; tie chooses lower val_loss",
                    test_policy="Evaluate each fixed configuration once, after all six training runs complete. No seed selection.",
                    comparison="Previously selected final recipes, including BiLSTM embedding dropout and early stopping; not architecture-only ablation.",
                    sources={name: {"config": str(PROJECT / "configs" / path),
                                    "sha256": sha(PROJECT / "configs" / path)} for name, path in BASES.items()})
    path = OUT / "protocol.json"
    if path.exists() and json.loads(path.read_text(encoding="utf-8")) != protocol:
        raise FileExistsError(f"实验方案已存在且内容不同：{path}")
    write_json(path, protocol)
    for seed in SEEDS:
        for name, filename in BASES.items():
            config = copy.deepcopy(json.loads((PROJECT / "configs" / filename).read_text(encoding="utf-8")))
            config["seed"] = seed
            config["data"]["split_seed"] = 42
            config["experiment_name"] = f"{name}_seed{seed}_20261103"
            config["output"]["run_dir"] = str((RUNS / f"seed_{seed}" / name).relative_to(ROOT)).replace("\\", "/")
            config["output"]["run_dir"] = "../" + config["output"]["run_dir"]
            target = OUT / f"seed_{seed}/configs/{name}.json"
            if target.exists() and json.loads(target.read_text(encoding="utf-8")) != config:
                raise FileExistsError(f"保留修改后的配置：{target}")
            write_json(target, config)
    print("Prepared six configs; fixed split_seed=42; training seeds=17,2024,3407.", flush=True)


def run_one(seed, name):
    import torch
    from news_classifier.config import load_config
    module = importlib.import_module("news_classifier.training.train")
    config_path = OUT / f"seed_{seed}/configs/{name}.json"
    config = load_config(config_path)
    folder = Path(config["output"]["run_dir"])
    if folder.exists():
        raise FileExistsError(f"保留已有训练目录：{folder}")
    if not torch.cuda.is_available():
        raise RuntimeError("正式训练要求 CUDA")
    folder.mkdir(parents=True, exist_ok=False)
    torch.set_num_threads(4)
    status = dict(status="running", seed=seed, model=name, pid=os.getpid(),
                  started_at_utc=datetime.now(timezone.utc).isoformat(),
                  device=torch.cuda.get_device_name(), torch_version=str(torch.__version__),
                  source_sha256={str(p.relative_to(ROOT)): sha(p) for p in
                                 list((PROJECT / "news_classifier").rglob("*.py")) + [config_path, Path(__file__)]})
    status_path = folder / "execution.json"
    write_json(status_path, status)
    original_prepare = module.prepare_data

    def audited_prepare(cfg):
        data = original_prepare(cfg)
        audit = {"split_seed": cfg["data"]["split_seed"], "vocab_size": len(data.vocab),
                 "vocab_sha256": hashlib.sha256(json.dumps(data.vocab, sort_keys=True).encode()).hexdigest()}
        for split in ("train", "val", "test"):
            loader = getattr(data, f"{split}_loader")
            audit[f"{split}_samples"] = len(loader.dataset)
            audit[f"{split}_encoded_sha256"] = hashlib.sha256(json.dumps(loader.dataset, separators=(",", ":")).encode()).hexdigest()
            audit[f"{split}_sampler_seed"] = loader.generator.initial_seed()
        status["data_audit"] = audit
        assert [audit[f"{s}_samples"] for s in ("train", "val", "test")] == [108000, 12000, 7600]
        assert audit["vocab_size"] == 42396
        write_json(status_path, status)
        return data

    module.prepare_data = audited_prepare
    started = time.perf_counter()
    with (folder / "console.log").open("x", encoding="utf-8", buffering=1) as log:
        original_stdout, original_stderr = sys.stdout, sys.stderr
        sys.stdout = sys.stderr = log
        try:
            result = module.train(config)
            checkpoint = torch.load(folder / "best_accuracy.pt", map_location="cpu", weights_only=True)
            reference = torch.load(ROOT / ".build/task2/runs/textcnn_k237_plateau20/best_accuracy.pt", map_location="cpu", weights_only=True)
            assert checkpoint["vocab"] == reference["vocab"]
            status.update(status="completed", summary=result, selected_epoch=checkpoint["epoch"],
                          val_accuracy=checkpoint["val_accuracy"], val_loss=checkpoint["val_loss"],
                          elapsed_seconds=time.perf_counter() - started,
                          checkpoint_sha256=sha(folder / "best_accuracy.pt"),
                          completed_at_utc=datetime.now(timezone.utc).isoformat())
            write_json(status_path, status)
        except BaseException:
            traceback.print_exc()
            status.update(status="failed", elapsed_seconds=time.perf_counter() - started)
            write_json(status_path, status)
            raise
        finally:
            sys.stdout, sys.stderr = original_stdout, original_stderr
            module.prepare_data = original_prepare
    print(f"Completed {name} seed={seed}; selected epoch={status['selected_epoch']}; val={status['val_accuracy']:.4%}", flush=True)


def run_all():
    queue = [(seed, name) for seed in SEEDS for name in BASES]
    active = []
    try:
        while queue or active:
            while queue and len(active) < 2:
                seed, name = queue.pop(0)
                folder = RUNS / f"seed_{seed}" / name
                if folder.exists():
                    raise FileExistsError(f"保留已有结果；不可重复启动：{folder}")
                child = subprocess.Popen([sys.executable, "-u", str(Path(__file__).resolve()),
                                          "--seed", str(seed), "--model", name],
                                         creationflags=subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0)
                active.append((child, seed, name))
                print(f"Started {name} seed={seed}, pid={child.pid}", flush=True)
            for child, seed, name in active.copy():
                if child.poll() is not None:
                    active.remove((child, seed, name))
                    if child.returncode != 0:
                        raise RuntimeError(f"Training failed: {name} seed={seed}, exit={child.returncode}")
            if active:
                time.sleep(2)
    finally:
        for child, _, _ in active:
            child.terminate()
        for child, _, _ in active:
            child.wait()
    print("All six training runs completed. No test evaluation has been run by this script.", flush=True)


def main():
    os.environ.update(HF_HUB_OFFLINE="1", HF_DATASETS_OFFLINE="1", PYTHONIOENCODING="utf-8")
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prepare", action="store_true")
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--seed", type=int, choices=SEEDS)
    parser.add_argument("--model", choices=BASES)
    args = parser.parse_args()
    if args.prepare:
        prepare()
    if args.all:
        run_all()
    elif args.seed is not None and args.model:
        run_one(args.seed, args.model)
    elif not args.prepare:
        parser.error("Use --prepare, --all, or --seed and --model.")


if __name__ == "__main__":
    main()
