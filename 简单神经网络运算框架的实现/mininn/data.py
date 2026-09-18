import struct
from pathlib import Path
import numpy as np
import gzip

def load_idx_images(path):
    path= Path(path)
    if (path.suffix == ".gz"):
        with gzip.open(path,"rb") as file:
            raw = file.read()
    else:
        raw = path.read_bytes()

    if(len(raw) < 16):
        raise ValueError(
            f"Incomplete image header: expected at least 16 bytes, "
            f"but received {len(raw)}"
        )
    actual_pixels_length = len(raw) - 16
    #从前16个字节中解析出四个整数
    magic_number,count,height,width = struct.unpack(">4I",raw[:16])
    if(magic_number != 2051):
        raise ValueError(
            f"Invalid magic number:expected 2051 , but received {magic_number}"
        )
    if(actual_pixels_length != count*height*width):
        raise ValueError(
            f"wrong pixels length: expected {count*height*width}, "
            f"but received {actual_pixels_length}"
        )

    #将头文件之后的原始字节解释为uint8像素
    #pixels:像素
    pixels= np.frombuffer(raw[16:],dtype = np.uint8)


    #这里有三个步骤：
    #1. 解释像素字节。 np.frombuffer 按指定类型读取内存中的字节。
    # uint8 每个元素占一个字节，所以本次得到形状为 (1568,) 的一维数组。
    #2. 恢复形状。 reshape 不改变像素顺序，只改变组织方式。
    # 四个维度依次填写 count、灰度图通道数 1、height、width。
    #3. 转换并归一化。 astype 的目标类型填 np.float64，除数填 255.0。
    # 于是黑色像素变为 0.0，白色像素变为 1.0。
    #恢复为nchw
    images = pixels.reshape((count,1,height,width))
    #uint8每个像素用一个字节存储，能表示的整数范围是 0～255，
    # 最后一整个除以255化为0到1范围的数字方便计算
    images = images.astype(np.float64)/255
    return images

def load_idx_labels(path):
    path = Path(path)
    if(path.suffix == ".gz"):
        with gzip.open(path,"rb") as file:
            raw = file.read()
    else:
        raw = path.read_bytes()
    
    #检查头文件是否完整
    if(len(raw) < 8):
        raise ValueError(f"header length must be at least 8 bytes but received {len(raw)}")

    #检查魔数是否正确
    magic_number , labels_count = struct.unpack(">2I",raw[:8])
    if(magic_number != 2049):
        raise ValueError(f"magic number error: expected 2049, but received {magic_number}")

    #检查标签数量是否对的上
    actual_labels_count = len(raw) - 8
    if(labels_count != actual_labels_count):
        raise ValueError(
            f"Wrong labels length: expected {labels_count}, "
            f"but received {actual_labels_count}"
        )

    #将头文件之后的字节统一解释为整数数组
    labels = np.frombuffer(
        raw[8:],
        dtype = np.uint8,
    )

    return labels