"""分类模型。"""
from .textcnn import TextCNN
from .bilstm import BiLSTM


def build_model(vocab_size: int, model_config: dict, pad_id: int = 0):
    """按配置恢复模型；缺少名称的历史权重仍使用 TextCNN。"""
    name = model_config.get("name", "textcnn")
    model_types = {"textcnn": TextCNN, "bilstm": BiLSTM}
    if name not in model_types:
        raise ValueError(f"不支持的 model.name：{name}")
    return model_types[name](vocab_size, model_config, pad_id)
