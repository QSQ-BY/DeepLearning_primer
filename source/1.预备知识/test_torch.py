import torch

print("PyTorch 版本：", torch.__version__)
print("CUDA 是否可用：", torch.cuda.is_available())

if torch.cuda.is_available():
    print("当前显卡：", torch.cuda.get_device_name(0))

x = torch.tensor([1.0, 2.0, 3.0])
print("计算结果：", x * 2)