"""读取实验配置；所有相对路径以 Task 2 项目目录为基准。"""

import json
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent.parent
DEFAULT_CONFIG = PROJECT_DIR / "configs" / "textcnn_ag_news.json"


def project_path(path: str | Path) -> Path:
    """解析项目内的相对路径，不创建目录。"""
    path = Path(path)
    return (path if path.is_absolute() else PROJECT_DIR / path).resolve()


def load_config(path: str | Path = DEFAULT_CONFIG) -> dict:
    """读取 JSON 并检查骨架所需的基本配置约束。"""
    config_path = project_path(path)
    with config_path.open(encoding="utf-8") as file:
        config = json.load(file)

    for name in ("experiment_name", "seed", "data", "model", "training", "output"):
        if name not in config:
            raise ValueError(f"配置缺少字段：{name}")

    data, model = config["data"], config["model"]
    if not 0 < data["val_ratio"] < 1:
        raise ValueError("data.val_ratio 必须在 0 和 1 之间")
    if data["pad_id"] != 0 or data["unk_id"] != 1:
        raise ValueError("当前接口约定 PAD_ID=0，UNK_ID=1")
    if model["num_classes"] != 4:
        raise ValueError("AG-news 分类输出必须为 4 类")
    if not model["kernel_sizes"] or any(k < 1 for k in model["kernel_sizes"]):
        raise ValueError("model.kernel_sizes 必须是非空的正整数列表")
    if data["max_length"] < max(model["kernel_sizes"]):
        raise ValueError("data.max_length 不能小于最大卷积核宽度")

    config["data"]["cache_dir"] = str(project_path(data["cache_dir"]))
    config["output"]["run_dir"] = str(project_path(config["output"]["run_dir"]))
    return config
