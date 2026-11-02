"""训练入口：python -m news_classifier.train --check-config。"""

import argparse

import csv
import json
import random
import torch
from .data import prepare_data
from .model import TextCNN
from .engine import train_one_epoch,evaluate
from .config import DEFAULT_CONFIG, load_config
from pathlib import Path

def train(config: dict) -> None:
    """组装数据、模型、训练循环和实验记录。

    1. 固定 Python/PyTorch 随机种子，解析 auto/cpu/cuda 设备。
    2. prepare_data(config)，据词表大小创建 TextCNN 和 Adam。
    3. 逐轮训练和验证，可根据验证损失调整下一轮的学习率。
    4. 保存每轮指标，分别保留最低验证损失和最高验证准确率模型。
    5. 权重文件一并保存词表、类别名称、配置和最佳轮次。
    测试集评估放在独立入口，不参与训练时的模型选择。
    """
    training_config = config["training"]
    scheduler_config = training_config.get("scheduler", {})
    scheduler_name = scheduler_config.get("name", "none")
    if scheduler_name not in ("none", "reduce_on_plateau"):
        raise ValueError(f"不支持的 training.scheduler.name：{scheduler_name}")

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
    model = TextCNN(
        vocab_size = len(data.vocab),
        model_config = config["model"],
        pad_id = config["data"]["pad_id"],
    ).to(device)
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


    run_dir = Path(config["output"]["run_dir"])
    run_dir.mkdir(parents=True, exist_ok=True)

    checkpoint_path = run_dir / config["output"]["checkpoint_name"]
    accuracy_checkpoint_path = run_dir / config["output"].get(
        "accuracy_checkpoint_name", "best_accuracy.pt"
    )
    if accuracy_checkpoint_path == checkpoint_path:
        raise ValueError("两种最佳模型必须使用不同的权重文件名")

    best_val_loss = float("inf")
    best_val_accuracy = float("-inf")
    best_accuracy_loss = float("inf")

    metrics_path = run_dir / config["output"]["log_name"]
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
    epochs = training_config["epochs"]

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


def main() -> None:
    parser = argparse.ArgumentParser(description="Task 2 AG-news TextCNN 训练入口")
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
