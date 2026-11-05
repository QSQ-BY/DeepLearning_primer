"""读取实验配置；所有相对路径以 Task 2 项目目录为基准。"""

import json
from pathlib import Path
from .training.early_stopping import build_early_stopping


PROJECT_DIR = Path(__file__).resolve().parent.parent
DEFAULT_CONFIG = PROJECT_DIR / "configs" / "textcnn_ag_news.json"


def project_path(path: str | Path) -> Path:
    """解析项目内的相对路径，不创建目录。"""
    path = Path(path)
    return (path if path.is_absolute() else PROJECT_DIR / path).resolve()


def min_sequence_length(model_config: dict) -> int:
    """TextCNN 需要容纳最大卷积核；BiLSTM 只需至少一个词元。"""
    name = model_config.get("name", "textcnn")
    if name == "textcnn":
        return max(model_config["kernel_sizes"])
    if name == "bilstm":
        return 1
    raise ValueError(f"不支持的 model.name：{name}")


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
    name = model.get("name", "textcnn")
    if name not in ("textcnn", "bilstm"):
        raise ValueError(f"不支持的 model.name：{name}")
    dimensions = ["embed_dim"] + (["hidden_size", "num_layers"] if name == "bilstm" else ["num_filters"])
    for field in dimensions:
        value = model.get(field)
        if type(value) is not int or value < 1:
            raise ValueError(f"model.{field} 必须是正整数")
    if not 0 <= model["dropout"] < 1:
        raise ValueError("model.dropout 必须在 [0, 1) 之间")
    if name == "bilstm" and not 0 <= model.get("embedding_dropout", 0.0) < 1:
        raise ValueError("model.embedding_dropout 必须在 [0, 1) 之间")
    if name == "textcnn":
        kernels = model.get("kernel_sizes")
        if not kernels or any(type(k) is not int or k < 1 for k in kernels):
            raise ValueError("model.kernel_sizes 必须是非空的正整数列表")
    if data["max_length"] < min_sequence_length(model):
        raise ValueError("data.max_length 不能小于模型要求的最小序列长度")
    build_early_stopping(config["training"].get("early_stopping"))

    config["data"]["cache_dir"] = str(project_path(data["cache_dir"]))
    config["output"]["run_dir"] = str(project_path(config["output"]["run_dir"]))
    return config
