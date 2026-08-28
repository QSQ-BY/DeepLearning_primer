import unittest
from mininn import losses
import numpy as np
class TestSoftmaxCrossEntropyLoss(unittest.TestCase):
    def test_loss_class_is_available(self):
        self.assertTrue(hasattr(losses,"SoftmaxCrossEntropyLoss"))

    #测试softmax交叉熵计算的正确性
    def test_equal_logits_have_log_class_count_loss(self):
        loss = losses.SoftmaxCrossEntropyLoss()

        forward = getattr(loss,"forward",None)
        self.assertTrue(callable(forward))

        #logits不是概率。它们是模型输出的原始分数，
        #可以是任意实数，不要求位于0到1之间，也不要求总和为1
        logits = np.zeros((2,3))#一共两组样本，共有三个类别
        #第一个样本的正确类别：类别 0
        #第二个样本的正确类别：类别 2
        labels = np.array([0,2])

        actual = forward(logits,labels)
        self.assertAlmostEqual(actual,np.log(3.0))

    #检测前向传播在面对较大的计算值的时候是否稳定
    def test_forward_is_stable_for_large_logits(self):
        loss = losses.SoftmaxCrossEntropyLoss()

        logits = np.array([
            [1000.0,1001.0,1002.0]
        ])
        labels = np.array([2])

        actual = loss.forward(logits,labels)
        self.assertTrue(np.isfinite(actual))

    #检测正确类数值远低于最大值的时候计算是否稳定
    def test_forward_is_stable_when_correct_class_is_far_below_max(self):
        loss = losses.SoftmaxCrossEntropyLoss()
        logits = np.array([
            [1000.0,-1000.0],
        ])
        labels = np.array([1])
        actual = loss.forward(logits,labels)
        self.assertAlmostEqual(actual,2000.0)

    #检测计算数据是否是2维
    def test_forward_rejects_non_2d_logits(self):
        loss = losses.SoftmaxCrossEntropyLoss()
        logits = np.zeros(3)
        labels = np.array([0])

        try:
            loss.forward(logits,labels)
        except ValueError as error:
            self.assertIn("2D",str(error))
        else:
            self.fail(
                "SoftmaxCrossEntropyLoss.forward() "
                "should reject non-2D logits"
            )

    #检测标签是否是一维
    def test_forward_rejects_non_1d_labels(self):
        loss = losses.SoftmaxCrossEntropyLoss()

        logits = np.zeros((2,3))
        labels = np.array([
            [1,2],
            [0,1]
        ])

        try:
            loss.forward(logits,labels)
        except ValueError as error:
            self.assertIn("1D",str(error))
        else:
            self.fail(
                "SoftmaxCrossEntropyLoss.forward() "
                "should reject non-1D labels"
            )

    #检测标签是否全部是整数
    def test_forward_rejects_noninteger_labels(self):
        loss = losses.SoftmaxCrossEntropyLoss()

        logits = np.zeros((2,3))
        labels = np.array([0.0,1.0])

        try:
            loss.forward(logits,labels)
        except Exception as error:
        #Exception是一个包含了常见错误的类，
        #只要实际错误是这些常见错误之一它就会捕获
            self.assertIsInstance(error,ValueError)
            self.assertIn("integer",str(error))
        else:
            self.fail(
                "SoftmaxCrossEntropyLoss.forward() "
                "should reject noninteger labels"
            )

    #检测样本数是否匹配
    def test_forward_rejects_mismatched_batch_size(self):
        loss = losses.SoftmaxCrossEntropyLoss()

        logits = np.zeros((2,3))
        labels = np.array([0])

        try:
            loss.forward(logits,labels)
        except Exception as error:
            self.assertIsInstance(error,ValueError)
            self.assertIn("same batch size",str(error))
        else:
            self.fail(
                "SoftmaxCrossEntropyLoss.forward() should "
                "reject mismatched batch sizes"
            )

    #检测样本数是否为空
    def test_forward_rejects_empty_batch(self):
        loss = losses.SoftmaxCrossEntropyLoss()

        logits = np.empty((0, 3))
        labels = np.array([], dtype=int)

        try:
            loss.forward(logits, labels)
        except ValueError as error:
            self.assertIn("at least one sample", str(error))
        else:
            self.fail(
                "SoftmaxCrossEntropyLoss.forward() "
                "should reject an empty batch"
            )

    #判断标签是否合法
    def test_forward_rejects_negative_label(self):
        loss = losses.SoftmaxCrossEntropyLoss()

        logits = np.zeros((1, 3))
        labels = np.array([-1])

        try:
            loss.forward(logits, labels)
        except ValueError as error:
            self.assertIn("outside", str(error))
        else:
            self.fail(
                "SoftmaxCrossEntropyLoss.forward() "
                "should reject negative labels"
            )

    def test_forward_rejects_label_exceed_range(self):
        loss = losses.SoftmaxCrossEntropyLoss()

        logits = np.zeros((1, 3))
        labels = np.array([3])

        try:
            loss.forward(logits, labels)
        except Exception as error:
            self.assertIsInstance(error, ValueError)
            self.assertIn("outside", str(error))
        else:
            self.fail(
                "SoftmaxCrossEntropyLoss.forward() "
                "should reject labels at the class count"
            )

    #检测反向传播能否正确计算导数
    def test_backward_returns_mean_logits_gradient(self):
        loss = losses.SoftmaxCrossEntropyLoss()
        logits = np.zeros((2,2))
        labels = np.array([0,1])
        loss.forward(logits,labels)

        backward = getattr(loss,"backward",None)
        self.assertTrue(callable(backward))

        actual = backward()
        expected = np.array([
            [-0.25,0.25],
            [0.25,-0.25]
        ])
        np.testing.assert_allclose(actual,expected)

    #检测反向传播i之前有没有进行正向传播
    def test_backward_requires_a_previous_forward_call(self):
        loss = losses.SoftmaxCrossEntropyLoss()

        try:
            loss.backward()
        except Exception as error:
            self.assertIsInstance(error,RuntimeError)
            self.assertIn("forward",str(error))
        else:
            self.fail(
                "SoftmaxCrossEntropyLoss.backward() "
                "should require forward() first"
            )

    def test_logits_gradient_matches_finite_difference(self):
        loss = losses.SoftmaxCrossEntropyLoss()
        logits = np.array([
            [0.2,-0.3,0.7],
            [1.1,0.4,-0.2],
        ])
        labels = np.array([2,0])

        loss.forward(logits,labels)
        analytic = loss.backward()

        numerical = np.zeros_like(logits)
        episilon = 1e-6
        batch_size = logits.shape[0]

        for sample_index in range(batch_size):
            for class_index in range(logits.shape[1]):
                plus_logits = logits.copy()
                minus_logits = logits.copy()

                plus_logits[sample_index][class_index] += episilon
                minus_logits[sample_index][class_index] -= episilon

                plus_loss = loss.forward(plus_logits,labels)
                minus_loss = loss.forward(minus_logits,labels)

                numerical[sample_index][class_index] = (
                    (plus_loss - minus_loss)/(2*episilon)
                )
        np.testing.assert_allclose(analytic,numerical,rtol = 1e-6,atol = 1e-8)



if(__name__ == "__main__"):
    unittest.main()
