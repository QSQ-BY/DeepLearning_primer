import unittest
import numpy as np
from mininn import model
from mininn import layers

class TestSequential(unittest.TestCase):
    def test_sequential_class_is_available(self):
        self.assertTrue(hasattr(model,"Sequential"))

    #验证 Sequential 能接收多个网络层，并且按照传入时的顺序保存它们
    def test_constructor_preserves_layer_order(self):
        first_layer = object()
        second_layer = object()

        try:
            sequential = model.Sequential(first_layer,second_layer)
        except TypeError as error:
            self.fail(
                "Sequential should accept multiple layers: "
                f"{error}"
            )
        self.assertEqual(sequential.layers,[first_layer,second_layer])

    def test_forward_calls_layer_inorder(self):
        class AddOneLayer:
            def forward(self,x):
                return x + 1.0

        class DoubleLayer:
            def forward(self,x):
                return x*2.0

        sequential = model.Sequential(
            AddOneLayer(),
            DoubleLayer(),
        )

        forward = getattr(sequential,"forward",None)
        self.assertTrue(callable(forward))

        x = np.array([1.0,2.0])
        actual = forward(x)
        #先加一后乘2
        expected = np.array([4.0,6.0])
        np.testing.assert_allclose(actual,expected)

    def test_backward_calls_layers_in_reverse_order(self):
        class AddOneGradientLayer:
            def backward(self,gradient):
                return gradient + 1
        class DoubleGradientLayer:
            def backward(self,gradient):
                return gradient*2

        sequential = model.Sequential(
            AddOneGradientLayer(),
            DoubleGradientLayer(),
        )

        backward = getattr(sequential,"backward",None)
        self.assertTrue(callable(backward))

        grad_output = np.array([1.0,2.0])
        actual = backward(grad_output)
        #反向传播时的导数是从后向前进行计算的
        expected = np.array([3.0,5.0])
        np.testing.assert_allclose(actual,expected)

    #测试 parameters() 能否按层顺序汇总参数，并跳过无参数层
    def test_parameters_collects_trainable_layer_parameters(self):
        class ParameterLayer:
            def __init__(self,value):
                self.parameter = np.array([value])
            def parameters(self):
                return [self.parameter]

        class LayerWithoutParameters:
            def parameters(self):
                return []
        #第一层参数：[parameter_1]
        #无参数层：  []
        #第二层参数：[parameter_2]
        #汇总结果：[parameter_1, parameter_2]
        first_layer = ParameterLayer(1.0)
        second_layer = ParameterLayer(2.0)

        sequential = model.Sequential(
            first_layer,
            LayerWithoutParameters(),
            second_layer,
        )

        parameters = getattr(sequential,"parameters",None)
        self.assertTrue(callable(parameters))

        actual = parameters()

        self.assertEqual(len(actual),2)
        self.assertIs(actual[0],first_layer.parameter)
        self.assertIs(actual[1],second_layer.parameter)

    def test_gradients_collects_trainable_layer_gradients(self):
        class GradientLayer:
            def __init__(self, value):
                self.gradient = np.array([value])

            def gradients(self):
                return [self.gradient]

        class LayerWithoutGradients:
            def gradients(self):
                return []

        first_layer = GradientLayer(1.0)
        second_layer = GradientLayer(2.0)

        sequential = model.Sequential(
            first_layer,
            LayerWithoutGradients(),
            second_layer,
        )

        gradients = getattr(sequential, "gradients", None)
        self.assertTrue(callable(gradients))

        actual = gradients()

        self.assertEqual(len(actual), 2)
        self.assertIs(actual[0], first_layer.gradient)
        self.assertIs(actual[1], second_layer.gradient)

    #检测是否一个层都没有传入
    def test_constructor_rejects_empty_layer_sequence(self):
        try:
            model.Sequential()
        except ValueError as error:
            self.assertIn("at least one layer",str(error))
        else:
            self.fail("Sequential should reject empty layer sequence")

    #检测序列网络能否正常完整工作
    def test_real_layers_work_together(self):
        rng = np.random.default_rng(7)
        first_layer = layers.Linear(
            2,3,rng = rng
        )
        activation = layers.ReLU()
        second_layer = layers.Linear(
            3,2,rng = rng
        )

        sequential = model.Sequential(
            first_layer,
            activation,
            second_layer,
        )

        x = np.array([
            [0.5,-1.0],
            [1.0,2.0]
        ])
        #二维输入
        #→ Linear(2, 3)
        #→ ReLU
        #→ Linear(3, 2)
        #→ 二维输出
        #→ 反向传播
        #→ 恢复输入形状的梯度

        output = sequential.forward(x)
        grad_output = np.ones_like(output)
        grad_input = sequential.backward(grad_output)

        self.assertEqual(output.shape,(2,2))
        self.assertEqual(grad_input.shape,x.shape)

        parameters = sequential.parameters()
        gradients = sequential.gradients()

        self.assertEqual(len(parameters),4)
        self.assertEqual(len(gradients),4)

        self.assertIs(parameters[0], first_layer.weight)
        self.assertIs(gradients[0], first_layer.grad_weight)

        self.assertIs(parameters[1], first_layer.bias)
        self.assertIs(gradients[1], first_layer.grad_bias)

        self.assertIs(parameters[2], second_layer.weight)
        self.assertIs(gradients[2], second_layer.grad_weight)

        self.assertIs(parameters[3], second_layer.bias)
        self.assertIs(gradients[3], second_layer.grad_bias)



if(__name__ == "__main__"):
    unittest.main()