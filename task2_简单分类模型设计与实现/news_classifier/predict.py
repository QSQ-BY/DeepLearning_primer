"""单条英文新闻预测入口。"""

import argparse
from pathlib import Path

from .config import project_path


def predict(checkpoint_path: Path, text: str) -> tuple[str, list[float]]:
    """TODO：恢复模型和词表，共用 encode()/collate_batch()，返回类别及概率。

    推理时使用 eval() 和 no_grad()，概率顺序与保存的 label_names 一致。
    """
    raise NotImplementedError("待实现：模型加载与单条新闻预测")


def main() -> None:
    parser = argparse.ArgumentParser(description="Task 2 AG-news 单条新闻预测入口")
    parser.add_argument("--checkpoint", required=True, help="最佳模型权重路径")
    parser.add_argument("--text", required=True, help="一条英文新闻")
    args = parser.parse_args()
    if not args.text.strip():
        parser.error("--text 不能为空")
    predict(project_path(args.checkpoint), args.text)


if __name__ == "__main__":
    main()
