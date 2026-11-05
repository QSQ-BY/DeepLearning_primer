"""按验证损失的有效改善控制停止时机，与最佳权重保存相互独立。"""

import math
from numbers import Real


class EarlyStopping:
    def __init__(self, patience: int = 3, min_delta: float = 0.001):
        if type(patience) is not int or patience < 1:
            raise ValueError("early_stopping.patience 必须是正整数")
        if isinstance(min_delta, bool) or not isinstance(min_delta, Real) or not math.isfinite(min_delta) or min_delta < 0:
            raise ValueError("early_stopping.min_delta 必须是非负有限数")
        self.patience = patience
        self.min_delta = float(min_delta)
        self.best = float("inf")
        self.bad_epochs = 0

    def step(self, val_loss: float) -> bool:
        if not math.isfinite(val_loss):
            raise ValueError("早停收到非有限的 val_loss")
        if val_loss < self.best - self.min_delta:
            self.best = val_loss
            self.bad_epochs = 0
        else:
            self.bad_epochs += 1
        return self.bad_epochs >= self.patience


def build_early_stopping(settings: dict | None) -> EarlyStopping | None:
    if settings is None:
        return None
    if not isinstance(settings, dict) or type(settings.get("enabled", False)) is not bool:
        raise ValueError("training.early_stopping 必须是字典，enabled 必须是布尔值")
    if not settings.get("enabled", False):
        return None
    if settings.get("monitor", "val_loss") != "val_loss":
        raise ValueError("early_stopping.monitor 当前只支持 val_loss")
    return EarlyStopping(settings.get("patience", 3), settings.get("min_delta", 0.001))
