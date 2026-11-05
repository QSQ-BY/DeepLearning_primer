"""BiLSTM 的早停、WD 与词嵌入 Dropout 单因素实验入口。"""

import argparse
import copy
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import sys
import time
import traceback

import torch

from ..config import PROJECT_DIR, load_config
from ..training.train import train


SETTINGS = {
    "baseline": (0.0001, 0.0),
    "wd3e4": (0.0003, 0.0),
    "wd1e3": (0.001, 0.0),
    "dropout01": (0.0001, 0.1),
    "dropout02": (0.0001, 0.2),
    "dropout03": (0.0001, 0.3),
}


def make_config(run_id: str) -> dict:
    if run_id not in SETTINGS:
        raise ValueError(f"未知实验：{run_id}")
    config = copy.deepcopy(load_config("configs/bilstm_ag_news.json"))
    wd, dropout = SETTINGS[run_id]
    config["experiment_name"] = f"bilstm_es_{run_id}_20261103"
    config["model"]["embedding_dropout"] = dropout
    config["training"]["weight_decay"] = wd
    config["training"]["early_stopping"] = {
        "enabled": True, "monitor": "val_loss", "patience": 3, "min_delta": 0.001,
    }
    config["output"]["run_dir"] = f"../.build/task2/runs/{config['experiment_name']}"
    # 配置文件保留可移植的项目相对路径。
    config["data"]["cache_dir"] = "../.build/task2/data"
    return config


def config_path(run_id: str) -> Path:
    return PROJECT_DIR / "configs" / f"bilstm_es_{run_id}_20261103.json"


def write_configs() -> None:
    for run_id in SETTINGS:
        path = config_path(run_id)
        contents = json.dumps(make_config(run_id), ensure_ascii=False, indent=2) + "\n"
        if path.exists() and path.read_text(encoding="utf-8") != contents:
            raise FileExistsError(f"保留已修改的实验配置：{path}")
        path.write_text(contents, encoding="utf-8")


def run_experiment(run_id: str) -> dict:
    config = load_config(config_path(run_id))
    run_dir = Path(config["output"]["run_dir"])
    if run_dir.exists():
        raise FileExistsError(f"保留已有实验，请使用新目录：{run_dir}")
    if not torch.cuda.is_available():
        raise RuntimeError("正式实验需要已验证的 CUDA 设备")
    run_dir.mkdir(parents=True, exist_ok=False)
    torch.set_num_threads(4)
    root = PROJECT_DIR.parent
    sources = list((PROJECT_DIR / "news_classifier").rglob("*.py")) + [config_path(run_id)]
    status = dict(status="running", run_id=run_id, pid=os.getpid(),
                  started_at=datetime.now(timezone.utc).isoformat(),
                  device=torch.cuda.get_device_name(), torch=str(torch.__version__),
                  source_sha256={str(path.relative_to(root)): hashlib.sha256(path.read_bytes()).hexdigest() for path in sources})
    status_path = run_dir / "execution.json"
    def save_status():
        status_path.write_text(json.dumps(status, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    save_status()
    started = time.perf_counter()
    with (run_dir / "console.log").open("x", encoding="utf-8", buffering=1) as log:
        original_stdout, original_stderr = sys.stdout, sys.stderr
        sys.stdout = sys.stderr = log
        try:
            print(f"{run_id} started at {status['started_at']}", flush=True)
            result = train(config)
            # 所有组训练完后才由汇总脚本选方案，此处不评估测试集。
            checkpoint = torch.load(run_dir / "best_accuracy.pt", map_location="cpu", weights_only=True)
            baseline = torch.load(root / ".build/task2/runs/bilstm_baseline_20261103/best_accuracy.pt", map_location="cpu", weights_only=True)
            assert checkpoint["vocab"] == baseline["vocab"]
            status.update(status="completed", summary=result, elapsed_seconds=time.perf_counter()-started,
                          completed_at=datetime.now(timezone.utc).isoformat(), vocabulary_matches_baseline=True,
                          selected_epoch=checkpoint["epoch"], val_accuracy=checkpoint["val_accuracy"], val_loss=checkpoint["val_loss"])
            save_status()
            print(json.dumps({key: value for key, value in status.items() if key != "source_sha256"}, ensure_ascii=False, indent=2), flush=True)
        except BaseException:
            traceback.print_exc()
            status.update(status="failed", elapsed_seconds=time.perf_counter()-started)
            save_status()
            raise
        finally:
            sys.stdout, sys.stderr = original_stdout, original_stderr
    return status


def main():
    os.environ["HF_HUB_OFFLINE"] = "1"
    os.environ["HF_DATASETS_OFFLINE"] = "1"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-id", choices=list(SETTINGS))
    parser.add_argument("--write-configs", action="store_true")
    args = parser.parse_args()
    if args.write_configs:
        write_configs()
    if args.run_id:
        run_experiment(args.run_id)
    elif not args.write_configs:
        parser.error("请提供 --run-id 或 --write-configs")


if __name__ == "__main__":
    main()
