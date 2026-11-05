"""独立测试入口，评估训练时选出的最佳模型。"""
import torch
import argparse
from pathlib import Path
from ..models import build_model
from ..config import project_path, min_sequence_length
from functools import partial
from datasets import load_dataset
from torch.utils.data import DataLoader
import json
from ..training.engine import evaluate
from ..data import encode,collate_batch
from ..data.preprocessing import clean_text

def evaluate_checkpoint(checkpoint_path: Path) -> dict[str, float|int]:
    checkpoint = torch.load(
        checkpoint_path,
        map_location = "cpu",
        weights_only = True,
    )
    config = checkpoint["config"]
    vocab = checkpoint["vocab"]
    label_names = checkpoint["label_names"]

    print(f"模型保存轮次：{checkpoint['epoch']}")
    print(f"词表大小：{len(vocab)}")
    print(f"类别名称：{label_names}")

    model = build_model(
        vocab_size = len(vocab),
        model_config = config["model"],
        pad_id = config["data"]["pad_id"]
    )
    #把保存好的模型数据加载进模型
    model.load_state_dict(checkpoint["model_state_dict"])

    device = torch.device(
        "cuda" if torch.cuda.is_available() else "cpu"
    )
    model = model.to(device)
    model.eval()
    print(f"评估设备：{device}")
    print("模型参数恢复完成")

    data_config = config["data"]

    # 只读取官方测试集。
    test_dataset = load_dataset(
        data_config["dataset_name"],
        cache_dir=data_config["cache_dir"],
        split="test",
    )

    # 使用训练时保存的词表和长度限制进行编码。
    test_samples = [
        (
            encode(
                clean_text(row["text"], version=config["experiment"].get("cleaning_version", "legacy_all_tags_v1")) if config.get("experiment", {}).get("clean_text", False) else row["text"],
                vocab,
                data_config["max_length"],
            ),
            row["label"],
        )
        for row in test_dataset
    ]

    collate_fn = partial(
        collate_batch,
        min_length=min_sequence_length(config["model"]),
    )

    test_loader = DataLoader(
        test_samples,
        batch_size=config["training"]["batch_size"],
        shuffle=False,
        num_workers=config["training"]["num_workers"],
        collate_fn=collate_fn,
    )
    print(f"测试样本数量：{len(test_loader.dataset)}")

    # 遍历测试集，计算平均损失和准确率。
    metrics = evaluate(
        model=model,
        loader=test_loader,
        device=device,
    )

    result = {
        "loss": metrics.loss,
        "accuracy": metrics.accuracy,
        "num_samples": metrics.num_samples,
    }

    # 保存在当前权重文件旁边。
    metrics_path = checkpoint_path.parent / "test_metrics.json"

    with metrics_path.open("w", encoding="utf-8") as file:
        json.dump(result, file, ensure_ascii=False, indent=2)
        file.write("\n")

    print(
        f"测试损失：{metrics.loss:.4f} | "
        f"测试准确率：{metrics.accuracy:.2%} | "
        f"测试样本数：{metrics.num_samples}"
    )
    print(f"测试指标已保存：{metrics_path}")

    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="Task 2 AG-news 测试集评估入口")
    parser.add_argument("--checkpoint", required=True, help="最佳模型权重路径")
    args = parser.parse_args()
    evaluate_checkpoint(project_path(args.checkpoint))


if __name__ == "__main__":
    main()
