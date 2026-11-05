"""训练入口：python -m news_classifier.train --check-config。"""

import argparse

import csv
import json
import random
import hashlib
import torch
from ..data import prepare_data
from ..models import build_model
from ..training.engine import train_one_epoch,evaluate
from ..config import DEFAULT_CONFIG, load_config
from pathlib import Path
from .early_stopping import EarlyStopping, build_early_stopping

def train(config: dict) -> dict:
    """组装数据、模型、训练循环和实验记录。

    1. 固定 Python/PyTorch 随机种子，解析 auto/cpu/cuda 设备。
    2. prepare_data(config)，据配置创建分类模型和 Adam。
    3. 逐轮训练和验证，可根据验证损失调整下一轮的学习率。
    4. 保存每轮指标，分别保留最低验证损失和最高验证准确率模型。
    5. 权重文件一并保存词表、类别名称、配置和最佳轮次。
    测试集评估放在独立入口，不参与训练时的模型选择。
    """
    if config.get("experiment"):
        raise ValueError("清洗或预训练词向量配置请使用 news_classifier.experiments.controlled，以恢复对应的预处理与初始化规则")
    training_config = config["training"]
    early_stopping = build_early_stopping(training_config.get("early_stopping"))
    epochs = training_config["epochs"]
    if type(epochs) is not int or epochs < 1:
        raise ValueError("training.epochs 必须是正整数")
    scheduler_config = training_config.get("scheduler", {})
    scheduler_name = scheduler_config.get("name", "none")
    if scheduler_name not in ("none", "reduce_on_plateau"):
        raise ValueError(f"不支持的 training.scheduler.name：{scheduler_name}")

    # 在读取数据前拒绝覆盖历史模型和日志。
    run_dir = Path(config["output"]["run_dir"])
    checkpoint_path = run_dir / config["output"]["checkpoint_name"]
    accuracy_checkpoint_path = run_dir / config["output"].get("accuracy_checkpoint_name", "best_accuracy.pt")
    metrics_path = run_dir / config["output"]["log_name"]
    if accuracy_checkpoint_path == checkpoint_path:
        raise ValueError("两种最佳模型必须使用不同的权重文件名")
    if any(path.exists() for path in (checkpoint_path, accuracy_checkpoint_path, metrics_path, run_dir / "config.json")):
        raise FileExistsError(f"保留已有实验，请配置新的 output.run_dir：{run_dir}")

    #固定随机种子
    seed = config["seed"]
    random.seed(seed)
    torch.manual_seed(seed)
    if(torch.cuda.is_available()):
        torch.cuda.manual_seed_all(seed)

    device_name = config["training"]["device"]
    if(device_name == "auto"):
        device_name = "cuda" if torch.cuda.is_available() else "cpu"

    device = torch.device(device_name)
    print(f"随机种子:{seed}")
    print(f"训练设备:{device_name}")

    #创建数据、模型以及优化器
    data = prepare_data(config)
    model = build_model(
        vocab_size = len(data.vocab),
        model_config = config["model"],
        pad_id = config["data"]["pad_id"],
    ).to(device)
    initial_hash = hashlib.sha256()
    for name, tensor in sorted(model.state_dict().items()):
        initial_hash.update(name.encode("utf-8"))
        initial_hash.update(tensor.detach().cpu().numpy().tobytes())
    optimizer = torch.optim.Adam(
        model.parameters(),
        lr = training_config["learning_rate"],
        weight_decay = training_config["weight_decay"],
    )
    scheduler = None
    if scheduler_name == "reduce_on_plateau":
        scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
            optimizer,
            mode="min",
            factor=scheduler_config.get("factor", 0.5),
            patience=scheduler_config.get("patience", 1),
            min_lr=scheduler_config.get("min_lr", 1e-5),
        )
    print(f"词表大小：{len(data.vocab)}")
    print(f"训练样本：{len(data.train_loader.dataset)}")
    print(f"验证样本：{len(data.val_loader.dataset)}")
    print(f"测试样本：{len(data.test_loader.dataset)}")
    print(f"模型：{type(model).__name__}，参数：{sum(p.numel() for p in model.parameters())}")
    if early_stopping is not None:
        print(f"早停：val_loss，patience={early_stopping.patience}，min_delta={early_stopping.min_delta}")


    run_dir = Path(config["output"]["run_dir"])
    run_dir.mkdir(parents=True, exist_ok=True)

    (run_dir / "config.json").write_text(
        json.dumps(config, ensure_ascii=False, indent=2) + "\n", encoding="utf-8",
    )

    best_val_loss = float("inf")
    best_val_accuracy = float("-inf")
    best_accuracy_loss = float("inf")

    fieldnames = [
        "epoch",
        "train_loss",
        "train_accuracy",
        "val_loss",
        "val_accuracy",
        "learning_rate",
    ]

    # 每次开始训练时创建本次实验日志，并写入表头。
    with metrics_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

    #正式开始训练循环
    stopped_early = False

    for epoch in range(1,epochs+1):
        epoch_lr = optimizer.param_groups[0]["lr"]
        train_metrics = train_one_epoch(
            model = model,
            loader = data.train_loader,
            optimizer = optimizer,
            device = device,
        )

        val_metrics = evaluate(
            model = model,
            loader = data.val_loader,
            device = device,
        )

        # 每轮追加一行原始指标，准确率保持在 0 到 1 之间。
        row = {
            "epoch": epoch,
            "train_loss": train_metrics.loss,
            "train_accuracy": train_metrics.accuracy,
            "val_loss": val_metrics.loss,
            "val_accuracy": val_metrics.accuracy,
            "learning_rate": epoch_lr,
        }

        with metrics_path.open("a", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(row)

        #打印本轮训练数据
        print(
            f"Epoch {epoch:02d}/{epochs} | "
            f"train loss: {train_metrics.loss:.4f} | "
            f"train acc: {train_metrics.accuracy:.2%} | "
            f"val loss: {val_metrics.loss:.4f} | "
            f"val acc: {val_metrics.accuracy:.2%} | "
            f"lr: {epoch_lr:.6g}"
        )

        checkpoint = {
            "model_state_dict": model.state_dict(),
            "config": config,
            "vocab": data.vocab,
            "label_names": data.label_names,
            "epoch": epoch,
            "val_loss": val_metrics.loss,
            "val_accuracy": val_metrics.accuracy,
            "learning_rate": epoch_lr,
        }

        #保存最佳训练模型数据
        if(val_metrics.loss < best_val_loss):
            best_val_loss = val_metrics.loss
            torch.save(dict(checkpoint, selection_metric="val_loss"), checkpoint_path)

            print(
                f"  已保存最低损失模型：第 {epoch} 轮，"
                f"验证损失 {best_val_loss:.4f}"
            )

        # 准确率相同时，保留验证损失更低的模型。
        if val_metrics.accuracy > best_val_accuracy or (
            val_metrics.accuracy == best_val_accuracy
            and val_metrics.loss < best_accuracy_loss
        ):
            best_val_accuracy = val_metrics.accuracy
            best_accuracy_loss = val_metrics.loss
            torch.save(
                dict(checkpoint, selection_metric="val_accuracy"),
                accuracy_checkpoint_path,
            )
            print(
                f"  已保存最高准确率模型：第 {epoch} 轮，"
                f"验证准确率 {best_val_accuracy:.2%}"
            )

        # 本轮统计记录实际使用的学习率；调度结果从下一轮生效。
        if scheduler is not None:
            scheduler.step(val_metrics.loss)
            next_lr = optimizer.param_groups[0]["lr"]
            if next_lr != epoch_lr:
                print(f"  学习率调整：{epoch_lr:.6g} -> {next_lr:.6g}（下一轮生效）")

        # 权重先按真实指标保存；min_delta 只影响早停的改善计数。
        if early_stopping is not None and early_stopping.step(val_metrics.loss):
            stopped_early = epoch < epochs
            print(f"早停触发：第 {epoch} 轮，连续 {early_stopping.bad_epochs} 轮无有效验证损失改善。")
            break

    summary = {
        "completed_epochs": epoch,
        "max_epochs": epochs,
        "stopped_early": stopped_early,
        "best_val_loss": best_val_loss,
        "best_val_accuracy": best_val_accuracy,
        "initial_parameter_sha256": initial_hash.hexdigest(),
        "early_stopping": None if early_stopping is None else {
            "monitor": "val_loss", "patience": early_stopping.patience,
            "min_delta": early_stopping.min_delta, "reference_loss": early_stopping.best,
            "bad_epochs": early_stopping.bad_epochs,
        },
    }
    (run_dir / "training_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8",
    )
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Task 2 AG-news TextCNN / BiLSTM 训练入口")
    parser.add_argument("--config", default=str(DEFAULT_CONFIG), help="实验 JSON 配置")
    parser.add_argument(
        "--check-config", action="store_true", help="仅读取并打印配置，不下载数据或训练"
    )
    args = parser.parse_args()
    config = load_config(args.config)
    if args.check_config:
        print(json.dumps(config, ensure_ascii=False, indent=2))
        return
    train(config)


if __name__ == "__main__":
    main()
