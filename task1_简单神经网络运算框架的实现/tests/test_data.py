import numpy as np
import unittest
import tempfile
import struct
from pathlib import Path
from mininn import data
import gzip#读取压缩文件 → 解压得到原始 IDX 字节 → 解析文件头和标签
from mininn.data import load_idx_images
from mininn.data import load_idx_labels

from examples import train_fashion_mnist
class TestIDXImages(unittest.TestCase):
    def test_load_images_return_normalized_nchw(self):
        images = np.zeros(shape = (2,28,28),dtype = np.uint8)
        images[1] = 255
        #这里的 ">4I" 可以拆开理解：
        #符号	含义
        #>	使用大端字节序
        #4	后面有四个整数
        #I	每个数用一个 4 字节无符号整数表示
        header = struct.pack(">4I",2051,2,28,28)

        #会在系统的临时文件位置创建一个目录，
        #temp_dir 得到这个目录的路径字符串。
        #这里的 with 负责管理目录的生命周期：
        #进入 with → 创建临时目录
        #执行缩进内的代码 → 在目录里写入、读取测试文件
        #退出 with → 自动删除临时目录及其中的文件
        with tempfile.TemporaryDirectory() as temp_dir:
            #Path(temp_dir) 将路径字符串转换成一个路径对象。
            #对于 Path 对象，/ 被定义为拼接路径。这里并不是做除法。
            path = Path(temp_dir)/"images.idx3-ubyte"
            #把numpy数组转换为像素字节 images.tobytes()
            #tobytes() 默认按 C 顺序展开数组。对于这里的图片，可以理解为：先逐行写完第一张，再逐行写第二张。
            #所以得到的像素字节是：
            #第一张：784 个 0
            #第二张：784 个 255
            #tobytes() 只保存元素的原始字节，不保存数组形状。 
            #这就是为什么文件头需要记录图片数量、行数和列数：
            #读取器要靠这些信息恢复形状。
            #write_bytes() 会打开这个路径对应的文件，写入字节，
            #然后关闭文件。如果文件不存在，会创建它。
            #后面的读取器将执行相反的过程：
            #读取前 16 字节
            #    → 解析魔数、图片数量、行数和列数
            #读取剩余像素
            #    → 按 uint8 解释
            #    → 恢复图片形状
            #    → 转成 float64 并除以 255
            #    → 返回 (2, 1, 28, 28)
            path.write_bytes(header + images.tobytes())

            actual = load_idx_images(path)
            #检查是否补上了通道维
            self.assertEqual(actual.shape,(2,1,28,28))
            #检查是否转换成了框架使用的浮点类型
            self.assertEqual(actual.dtype,np.dtype(np.float64))

            #检查两张图片的全部像素
            np.testing.assert_array_equal(actual[0], np.zeros((1, 28, 28)))
            np.testing.assert_array_equal(actual[1], np.ones((1, 28, 28)))

    def test_load_images_uses_count_from_header(self):
        images = np.zeros((3,28,28),dtype = np.uint8)
        header= struct.pack(">4I",2051,3,28,28)
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir)/"images.idx3-ubyte"
            path.write_bytes(header + images.tobytes())

            actual = load_idx_images(path)

            self.assertEqual(actual.shape,(3,1,28,28))

    #检查是否拒绝了错误的魔数
    def test_load_images_reject_wrong_magic_number(self):
        images = np.zeros((2,28,28),dtype = np.uint8)
        #只更改魔数其他保持不变
        header = struct.pack(">4I",2026,2,28,28)
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir)/"images.idx3-ubyte"
            path.write_bytes(header + images.tobytes())

            try:
                load_idx_images(path)
            except ValueError as error:
                self.assertIn("magic number",str(error))
            else:
                self.fail("load_idx_images() should reject wrong magic number")

    def test_load_images_rejects_incompelete_header(self):
        header = struct.pack(">4I",2025,2,28,28)
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir)/"imaghes.idx3-ubyte"
            path.write_bytes(header[:12])
            try:
                load_idx_images(path)
            except ValueError as error:
                self.assertIn("header" , str(error))
            else:
                self.fail("load_idx_iamges() should reject incompelete header")

    def test_load_images_rejects_truncated_pixels_data(self):
        images = np.zeros((2,28,28),dtype = np.uint8)
        header = struct.pack(">4I",2051,2,28,28)
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir)/"images.idx3-ubyte"
            path.write_bytes(header + images.tobytes()[:-1])

            try:
                load_idx_images(path)
            except ValueError as error:
                self.assertIn("pixels",str(error))
            else:
                self.fail("load_idx_iamges() should reject_truncated_pixels_data")

    def test_load_images_rejects_extra_pixel_data(self):
        images = np.zeros((2, 28, 28), dtype=np.uint8)
        header = struct.pack(">4I", 2051, 2, 28, 28)

        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "images.idx3-ubyte"

            # 在完整数据后额外添加一个字节
            path.write_bytes(header + images.tobytes() + b"\x00")

            with self.assertRaisesRegex(ValueError, "pixels"):
                load_idx_images(path)

class TestIDXLabels(unittest.TestCase):
    def test_load_labels_returns_integer_vector(self):
        #给读取器一个存有 [0, 3, 9] 的标签文件，
        # 它应该返回形状为 (3,)、数值仍为 [0, 3, 9] 的整数数组。
        labels = np.array([0,3,9],dtype = np.uint8)
        #两个大端无符号整数共8个字节
        #写法	            含义
        #>	            使用大端字节序
        #2I	            两个无符号整数，每个占 4 字节
        #2049	      标签文件的魔数
        #3	            文件中有 3 个标签
        header = struct.pack(">2I",2049,3)

        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir)/"labels.idx-ubyte"
            path.write_bytes(header + labels.tobytes())
            load_idx_labels = getattr(data,"load_idx_labels",None)
            self.assertTrue(callable(load_idx_labels))
            actual = load_idx_labels(path)

            self.assertEqual(actual.shape,(3,))

            self.assertTrue(
                np.issubdtype(actual.dtype,np.integer)
            )
            np.testing.assert_array_equal(actual,labels)

    def test_load_labels_rejects_truncated_data(self):
        labels = np.array([0,3,9],dtype = np.uint8)
        header = struct.pack(">2I",2049,3)

        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir)/"label.idx1-ubyte"

            #头文件有三个标签，实际只写入两个
            path.write_bytes(header + labels.tobytes()[:-1])

            try:
                load_idx_labels(path)
            except ValueError as error:
                self.assertIn("labels length",str(error))
            else:
                self.fail("load_idx_labels should rejects truncated_data")

    def test_load_labels_rejects_invalid_files(self):
        labels = np.array([0,3,9],dtype = np.uint8)
        header = struct.pack(">2I",2049,3)
        payload = labels.tobytes()

        cases = [
            ("short_header",header[:4],"header"),
            ("wrong_magic_number",struct.pack(">2I",2026,3)+payload,"magic number"),
            ("extra_label",header + payload + b"\x00","labels length"),
        ]

        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir)/"labels.idx-ubyte"

            for name,content,message in cases:
                with self.subTest(case = name):
                    path.write_bytes(content)
                    try:
                        load_idx_labels(path)
                    except ValueError as error:
                        self.assertIn(message,str(error))
                    else:
                        self.fail(
                            f"load_idx_labels() should reject {name}"
                        )

    def test_load_labels_reads_gzip_file(self):
        labels = np.array([0,3,9],dtype = np.uint8)
        header = struct.pack(">2I",2049,3)

        #先构造完整压缩内容再进行gzip读取
        compressed = gzip.compress(header + labels.tobytes())

        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir)/"labels.idx1-ubyte.gz"
            path.write_bytes(compressed)

            actual = load_idx_labels(path)

            self.assertEqual(actual.shape,(3,))
            self.assertTrue(
                np.issubdtype(actual.dtype,np.integer)
            )
            np.testing.assert_array_equal(actual,labels)

    #.gz 文件 → 解压 → 解析 IDX → 恢复 NCHW → 转成 float64 → 除以 255
    def test_load_images_reads_gzip_file(self):
        #第一张：左上角像素是 128，其余是 0。
        #第二张：所有像素都是 255。
        images = np.zeros((2,28,28),dtype= np.uint8)
        images[1] = 255
        images[0,0,0] = 128

        header = struct.pack(">4I",2051,2,28,28)
        compressed = gzip.compress(header + images.tobytes())

        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir)/"iamges.idx3-ubyte.gz"
            path.write_bytes(compressed)

            actual = load_idx_images(path)

            self.assertEqual(actual.shape,(2,1,28,28))
            self.assertEqual(actual.dtype,np.dtype(np.float64))

            #索引部分	作用
            #第一个 :	保留所有图片
            #np.newaxis	插入一个长度为 1 的新维度
            #后两个 :	保留所有行和列
            expected = images[:, np.newaxis, :, :].astype(np.float64) / 255.0
            np.testing.assert_allclose(actual, expected)

class TestFashionMNISTData(unittest.TestCase):
    def test_rejectes_mismatched_sample_counts(self):
        images = np.zeros((2,28,28),dtype = np.uint8)
        labels = np.array([0,3,9],dtype = np.uint8)
        images_header = struct.pack(">4I",2051,2,28,28)
        labels_header = struct.pack(">2I",2049,3)
        with tempfile.TemporaryDirectory() as temp_dir:
            image_path = Path(temp_dir)/"images.idx3-ubyte"
            label_path = Path(temp_dir)/"labels.idx3-ubyte"

            image_path.write_bytes(images_header + images.tobytes())
            label_path.write_bytes(labels_header + labels.tobytes())
            
            loader = getattr(train_fashion_mnist,"_load_dataset",None)
            self.assertTrue(callable(loader))

            try:
                loader(image_path,label_path)
            except ValueError as error:
                self.assertIn("sample count",str(error))
            else:
                self.fail("Should reject mismatched image and label counts")

    def test_load_dataset_returns_matched_images_and_labels(self):
        images = np.zeros((2, 28, 28), dtype=np.uint8)
        images[1] = 255
        labels = np.array([3, 9], dtype=np.uint8)

        with tempfile.TemporaryDirectory() as temp_dir:
            image_path = Path(temp_dir) / "images.idx3-ubyte"
            label_path = Path(temp_dir) / "labels.idx1-ubyte"

            image_path.write_bytes(
                struct.pack(">4I", 2051, 2, 28, 28) + images.tobytes()
            )
            label_path.write_bytes(
                struct.pack(">2I", 2049, 2) + labels.tobytes()
            )

            actual_images, actual_labels = (
                train_fashion_mnist._load_dataset(image_path, label_path)
            )

            expected_images = (
                images[:, np.newaxis, :, :].astype(np.float64) / 255.0
            )

            self.assertEqual(actual_images.shape, (2, 1, 28, 28))
            self.assertEqual(actual_labels.shape, (2,))
            np.testing.assert_allclose(actual_images, expected_images)
            np.testing.assert_array_equal(actual_labels, labels)

if __name__ == "__main__":
    unittest.main()





