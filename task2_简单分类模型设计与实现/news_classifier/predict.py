"""单条英文新闻预测入口。"""

import argparse
from pathlib import Path
import torch
from .model import TextCNN
from .config import project_path
from .data import encode,collate_batch

def predict(checkpoint_path: Path, text: str) -> tuple[str, list[float]]:
    #加载并恢复最佳训练模型
    checkpoint = torch.load(
        checkpoint_path,
        map_location="cpu",
        weights_only=True,
    )
    config = checkpoint["config"]
    vocab = checkpoint["vocab"]
    label_names = checkpoint["label_names"]
    model = TextCNN(
        vocab_size=len(vocab),
        model_config=config["model"],
        pad_id=config["data"]["pad_id"],
    )
    model.load_state_dict(checkpoint["model_state_dict"])
    device = torch.device(
        "cuda" if torch.cuda.is_available() else "cpu"
    )
    model = model.to(device)
    model.eval()
    #input_ids：形状 [1, L]
    #lengths：  形状 [1]
    token_ids = encode(
        text,vocab,config["data"]["max_length"],
    )

    # 组成只有一条样本的批次。
    input_ids, lengths, _ = collate_batch(
        [(token_ids, 0)],
        min_length=max(config["model"]["kernel_sizes"]),
    )
    input_ids = input_ids.to(device)
    lengths = lengths.to(device)

    #dim=1：沿类别维度计算 Softmax，四个概率加起来约等于 1。
    #argmax(dim=1)：找出概率最大的类别编号。
    #.item()：将只有一个元素的张量取成 Python 数值。
    #.squeeze(0)：移除大小为 1 的批次维度，将 [1,4] 变为 [4]。
    #.cpu().tolist()：将结果移到 CPU，再转换成普通列表。
    with torch.no_grad():
        logits = model(input_ids, lengths)
        probabilities = torch.softmax(logits, dim=1)

    predicted_id = probabilities.argmax(dim=1).item()
    predicted_label = label_names[predicted_id]
    probability_list = probabilities.squeeze(0).cpu().tolist()

    return predicted_label, probability_list

def main() -> None:
    parser = argparse.ArgumentParser(description="Task 2 AG-news 单条新闻预测入口")
    parser.add_argument("--checkpoint", required=True, help="最佳模型权重路径")
    parser.add_argument("--text", required=True, help="一条英文新闻")
    args = parser.parse_args()
    if not args.text.strip():
        parser.error("--text 不能为空")
    label,probabilities = predict(project_path(args.checkpoint), args.text)
    print(f"预测类别：{label}")
    print(f"类别概率：{probabilities}")


if __name__ == "__main__":
    main()
