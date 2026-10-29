"""训练入口：python -m news_classifier.train --check-config。"""

import argparse
import json

from .config import DEFAULT_CONFIG, load_config


def train(config: dict) -> None:
    """TODO：组装完整实验流程。

    1. 固定 Python/PyTorch 随机种子，解析 auto/cpu/cuda 设备。
    2. prepare_data(config)，据词表大小创建 TextCNN 和 Adam。
    3. 逐轮调用 train_one_epoch() 和 evaluate()，按配置调整学习率。
    4. 在 run_dir 保存配置与每轮指标，按验证损失保留 best.pt。
    5. 权重文件一并保存词表、类别名称、配置和最佳轮次。
    测试集评估放在独立入口，不参与训练时的模型选择。
    """
    raise NotImplementedError("项目骨架已就绪，请先完成 data.py、model.py 和 engine.py")


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
