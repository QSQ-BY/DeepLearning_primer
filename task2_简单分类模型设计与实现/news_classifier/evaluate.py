"""独立测试入口，评估训练时选出的最佳模型。"""

import argparse
from pathlib import Path

from .config import project_path


def evaluate_checkpoint(checkpoint_path: Path) -> dict[str, float]:
    """TODO：从 checkpoint 恢复配置、词表、类别和模型，评估官方测试集。

    复用训练时的数据预处理，不重新构建词表，不再用测试集选超参数。
    将真实测试指标写入实验目录，返回 loss、accuracy 等指标。
    """
    raise NotImplementedError("待实现：最佳模型加载和测试集评估")


def main() -> None:
    parser = argparse.ArgumentParser(description="Task 2 AG-news 测试集评估入口")
    parser.add_argument("--checkpoint", required=True, help="最佳模型权重路径")
    args = parser.parse_args()
    evaluate_checkpoint(project_path(args.checkpoint))


if __name__ == "__main__":
    main()
