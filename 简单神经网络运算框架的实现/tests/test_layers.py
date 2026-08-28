import unittest#python标准测试库
import inspect#用于获取函数、类和对象需要传入的参数名
import numpy as np#无需多言,yyds
from mininn import layers

class TestLinearModel(unittest.TestCase):
    #检测Linear类是否已经存在
    def test_linear_class_is_available(self):
        #hasattr(layers, "Linear")它询问 Python：
        #layers 模块中是否存在一个叫作 Linear 的成员？
        #如果有就返回True,否则返回False
        #assertTrue函数要求括号里的内容必须是True，如果是False就会报错
        self.assertTrue(hasattr(layers,"Linear"))

    #测试构造函数是否长成了我们希望的样子
    def test_constructor_declares_expected_arguments(self):
        #inspect函数用于获取函数、类和对象的结构,检查是否有对应的接口
        #parameters相当于一个集合里面包含了所有的参数名
        parameters = inspect.signature(layers.Linear).parameters
        #三个断言用于检查类是否有我们需要的接口
        self.assertIn("in_features",parameters)#输入的特征数量
        self.assertIn("out_features",parameters)#输出的特征数量
        self.assertIn("rng",parameters)#可选的numpy随机数生成器

    def test_constructor_creates_expected_parameter_shapes(self):
        rng = np.random.default_rng(7)#7为随机种子
        layer = layers.Linear(2,3,rng = rng)#输入变量是2，输出变量是3

        #这里创建的是：
        #Linear(in_features=2, out_features=3)
        #所以未来矩阵形状应该是：
        #输入 x：            (batch_size, 2)
        #权重 weight：       (2, 3)
        #输出：              (batch_size, 3)
        #偏置 bias：         (3,)

        #矩阵乘法过程：
        #(batch_size, 2)(2, 3) = (batch_size, 3)
        #偏置 (3,) 会通过 NumPy 广播，加到每个样本的三个输出上。
        #前两个 hasattr() 可以确保当前测试得到清晰的断言失败，
        #而不是直接访问不存在的属性产生错误。
        self.assertTrue(hasattr(layer,"weight"))
        self.assertTrue(hasattr(layer,"bias"))
        self.assertEqual(layer.weight.shape,(2,3))
        self.assertEqual(layer.bias.shape,(3,))

    #检查随机数生成器是否为我们成功生成了一个随机的权重矩阵，全0的偏置矩阵
    def test_constructor_uses_rng_for_reproducible_weights(self):
        #创建第一个 Linear(2, 3)，并提供种子为 7 的随机数生成器。
        first = layers.Linear(2,3,rng = np.random.default_rng(7))
        #创建第二个独立的生成器，但种子仍然是 7。
        second = layers.Linear(2,3,rng = np.random.default_rng(7))
        #检查两个权重矩阵的对应元素近似相等
        np.testing.assert_allclose(first.weight,second.weight)
        self.assertFalse(np.all(first.weight == 0.0))
        #检查偏置矩阵的元素全为0
        np.testing.assert_allclose(first.bias,np.zeros(3))

    #测试构造函数在省略 rng 时，会自动创建默认随机数生成器
    def test_constructor_creates_default_rng_when_omitted(self):
        try:
            layer = layers.Linear(2,3,rng = None)
        #如果 try 中发生 AttributeError，就捕获它，并把错误对象保存到变量 error。
        except AttributeError as error:
            #self.fail() 会主动让当前测试失败。
            self.fail(
                f"Linear Model should create a default rng when rng is None:{error}"
            )
        #创建成功后检查权重
        self.assertFalse(np.all(layer.weight == 0.0))
        np.testing.assert_allclose(layer.bias,np.zeros(3))

    #检测前向传播是否能进行正确的计算
    def test_forward_computes_matrix_product_and_bias(self):
        layer = layers.Linear(2,2,rng = np.random.default_rng(7),)
        layer.weight[::] = np.array([
            [1.0,2.0],
            [-1.0,3.0],
        ])
        layer.bias[::] = np.array([
            0.5,-0.5
        ])
        x = np.array([
            [1.0, 2.0],
            [-1.0, 3.0],
        ])
        #getattr会在方法不存在时返回 None，随后 callable(forward) 返回 False
        forward = getattr(layer,"forward",None)
        self.assertTrue(callable(forward))
        actual = forward(x)
        expected = np.array([
            [-0.5,7.5],
            [-3.5,6.5],
        ])
        np.testing.assert_allclose(actual,expected)

    #查 Linear.forward() 面对错误输入时，能否尽早给出清楚的错误信息
    def test_forward_rejects_wrong_feature_count(self):
        #forward() 的结果	                    测试结果
        #抛出 ValueError，且信息包含指定文字	     测试通过
        #抛出 ValueError，但信息不包含指定文字	 assertIn() 失败
        #没有抛出任何异常	                    self.fail() 失败
        #抛出其他异常，如 TypeError	            测试显示 ERROR
        layer = layers.Linear(2,3,rng = np.random.default_rng(7))
        #故意创建错误的输入
        wrong_x = np.ones((4,5))
        try:
            layer.forward(wrong_x)
        #在forward函数已经抛出了ValueError的时候触发
        except ValueError as error:
            self.assertIn(
                "expected 2 input features",
                str(error),
            )
        else:
            self.fail(
                "Linear.forward() should reject the wrong feature count"
            )

    #检查向前传播是否拒绝了非二维输入
    def test_forward_rejects_non_2d_input(self):
        layer = layers.Linear(2,3,rng = np.random.default_rng(7))
        wrong_x = np.ones(2)
        try:
            layer.forward(wrong_x)
        except (ValueError,IndexError) as error:
            #异常类型：ValueError
            #异常信息：说明输入必须是 2D array
            self.assertIsInstance(error,ValueError)
            self.assertIn(
                "2D array",str(error)
            )
        else:
            self.fail("Linear.forward() should reject non-2D input")

    #测试反向传播是否能正确计算输入和参数的梯度
    def test_backward_computes_input_and_parameter_gradients(self):
        layer = layers.Linear(2,2,rng = np.random.default_rng(7))
        layer.weight[::] = np.array([
            [1.0,2.0],
            [3.0,4.0],
        ])
        x = np.array([
            [1.0,2.0],
            [-1.0,3.0],
        ])
        #表示损失函数对于Y的梯度，这里直接认为规定
        grad_output = np.array([
            [1.0,-1.0],
            [2.0,3.0],
        ])
        layer.forward(x)

        #表示损失函数对x的梯度，认为计算然后机型比较
        #grad_input = grad_ouput @ W.T（数学推导得出）
        grad_input = layer.backward(grad_output)
        np.testing.assert_allclose(grad_input,
            np.array([
                [-1.0,-1.0],
                [8.0,18.0]
            ]))

        #grad_weight = X.T @ grad_output
        np.testing.assert_allclose(
            layer.grad_weight,
            np.array([
                [-1.0, -4.0],
                [8.0, 7.0],
            ]))

        #grad_bias = sum(grad_output(axis = 0))
        np.testing.assert_allclose(
            layer.grad_bias,
            np.array([3.0, 2.0]),
        )

    #验证反向传播之前是否有向前传播
    def test_backward_requires_a_previous_forward_call(self):
        layer = layers.Linear(2,3,rng = np.random.default_rng(7))
        #实际行为	                               测试结果
        #抛出 RuntimeError("...forward...")	        OK
        #抛出 RuntimeError，但信息没有 "forward"	 FAIL
        #没有抛出异常	进入 else，                  FAIL
        #抛出 AttributeError 等其他异常	             未被捕获，ERROR
        try:
            layer.backward(np.ones((4,3)))
        except RuntimeError as error:
            self.assertIn("forward",str(error))
        else:
            self.fail("Linear.backward should requires forward first")

    #验证Linear能否把可训练参数以及对应的梯度以正确的顺序传递给优化器
    def test_parameters_and_gradients_have_matching_order(self):
        layer = layers.Linear(2,3,rng = np.random.default_rng(7))
        #期望接口:
        #parameters() → [weight, bias]
        #gradients()  → [grad_weight, grad_bias]
        #parameters容器和gradient容器里的参数和梯度一一对应
        parameters = layer.parameters()
        gradients = layer.gradients()

        self.assertIs(parameters[0],layer.weight)
        self.assertIs(parameters[1],layer.bias)
        self.assertIs(gradients[0],layer.grad_weight)
        self.assertIs(gradients[1],layer.grad_bias)

    def test_backward_rejects_wrong_gradient_shape(self):
        layer = layers.Linear(2,3,rng = np.random.default_rng(7))
        layer.forward(np.ones((4,2)))
        #y = X @ w，所以正确的输出形状应该是(4,3),这里故意传入错误的形状(4,2)
        wrong_grad_output = np.ones((4,2))

        try:
            layer.backward(wrong_grad_output)
        except ValueError as error:
            self.assertIn(
                "expected grad_output shape",
                str(error),
            )
        else:
            self.fail("Linear.backward() should reject the wrong gradient shape")

    #通过“轻微改变权重，观察结果怎么变化”，独立检查 grad_weight 是否正确
    def test_weight_gradient_matches_finite_difference(self):
        layer = layers.Linear(2,2,np.random.default_rng(7))
        x = np.array([
            [0.2,-0.4],
            [1.2,0.7],
        ])
        grad_output = np.array([
            [0.3,-0.6],
            [0.8,0.5],
        ])
    #先正常进行正向传播与反向传播并记录下来权重梯度
        layer.forward(x)
        layer.backward(grad_output)
        analytic = layer.grad_weight.copy()

        numerical = np.zeros_like(layer.weight)
        epsilon = 1e-6
        #依次估算每个权重的偏导数
        for index in np.ndindex(layer.weight.shape):
            original = layer.weight[index]

            layer.weight[index] = original + epsilon
            plus = np.sum(layer.forward(x)*grad_output)

            layer.weight[index] = original - epsilon
            minus = np.sum(layer.forward(x)*grad_output)

            layer.weight[index] = original
            numerical[index] = ((plus - minus)/(2*epsilon))

        np.testing.assert_allclose(analytic,numerical,rtol = 1e-6,atol = 1e-8)

class TestReLU(unittest.TestCase):
    def test_relu_class_is_available(self):
        self.assertTrue(hasattr(layers,"ReLU"))

    #检测ReLU模型是否能成功把非正值置为0
    def test_forward_replaces_nonpositive_values_with_zero(self):
        layer = layers.ReLU()
        forward = getattr(layer,"forward",None)
        self.assertTrue(callable(forward))

        x = np.array([
            [-2.0,0.0,3.0],
        ])
        actual = forward(x)
        expected = np.array([
            [0.0,0.0,3.0],
        ])
        np.testing.assert_allclose(actual,expected)

    #测试 ReLU 反向传播只保留前向输入为正的位置的梯度
    def test_backward_keeps_gradient_only_for_positive_inputs(self):
        layer = layers.ReLU()
        layer.forward(np.array([
            [-2.0,0.0,3.0],
        ]))

        backward = getattr(layer,"backward",None)
        self.assertTrue(callable(backward))

        grad_output = np.array([
            [4.0,5.0,6.0],
        ])
        actual = backward(grad_output)
        #前两个输入是非正数，因此只保留最后一个位置的梯度
        expected = np.array([
            [0.0,0.0,6.0]
        ])
        np.testing.assert_allclose(actual,expected)

    def test_backward_requires_a_previous_forward_call(self):
        layer = layers.ReLU()
        try:
            layer.backward(np.ones((1,3)))
        except RuntimeError as error:
            self.assertIn("forward",str(error))
        else:
            self.fail("ReLU.backward() should require forward() first")

    def test_backward_rejects_wrong_gradient_shape(self):
        layer = layers.ReLU()
        layer.forward(np.ones((2,3)))
        wrong_grad_output = np.ones(3)
        try:
            layer.backward(wrong_grad_output)
        except ValueError as error:
            self.assertIn("expected grad_output shape",str(error))
        else:
            self.fail("ReLU.backward() should reject wrong grad_output shape")

    #检测 ReLU 是否提供空的参数与梯度接口
    def test_relu_has_no_trainable_parameters(self):
        layer = layers.ReLU()

        parameters = getattr(layer,"parameters",None)
        gradients = getattr(layer,"gradients",None)

        self.assertTrue(callable(parameters))
        self.assertTrue(callable(gradients))
        self.assertEqual(parameters(),[])
        self.assertEqual(gradients(),[])

if(__name__ == "__main__"):
    unittest.main()
