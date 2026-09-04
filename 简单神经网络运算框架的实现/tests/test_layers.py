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

class TestConv2D(unittest.TestCase):
    def test_conv2d_class_is_available(self):
        self.assertTrue(hasattr(layers,"Conv2D"))
    #检查构造函数有没有包含所需的参数
    def test_constructor_declares_expected_arguments(self):
        #获取类的参数名
        parameters = inspect.signature(layers.Conv2D).parameters
        expected_names = [
            "in_channels","out_channels",
            "kernel_size","stride","padding","rng"
        ]
        self.assertEqual(list(parameters),expected_names)

    #检查参数的默认值
    def test_constructor_uses_expected_optional_defaults(self):
        parameters = inspect.signature(layers.Conv2D).parameters
        self.assertEqual(parameters["stride"].default,1)
        self.assertEqual(parameters["padding"].default,0)
        self.assertIsNone(parameters["rng"].default)

    #检查构造函数是否创建了预期形状的参数
    def test_constructor_creates_expected_parameter_shape(self):
        layer = layers.Conv2D(in_channels = 2,out_channels = 3,kernel_size = 4,rng = np.random.default_rng(7))
        #检查是否创建了参数
        self.assertTrue(hasattr(layer,"weight"))
        self.assertTrue(hasattr(layer,"bias"))
        self.assertTrue(hasattr(layer,"grad_weight"))
        self.assertTrue(hasattr(layer,"grad_bias"))
        #检查参数的形状是否正确
        #权重的形状含义是(输出通道数，输入通道数，卷积核高度，卷积核宽度)
        self.assertEqual(layer.weight.shape,(3,2,4,4))
        #偏置参数，对每一组输出加上一个偏置参数，故形状是3
        self.assertEqual(layer.bias.shape,(3,))
        #梯度的形状应该与原本参数的形状一致
        self.assertEqual(layer.grad_weight.shape, layer.weight.shape)
        self.assertEqual(layer.grad_bias.shape, layer.bias.shape)
        #参数的类型应该为浮点类型
        self.assertEqual(layer.weight.dtype, np.float64)
        self.assertEqual(layer.bias.dtype, np.float64)
        self.assertEqual(layer.grad_weight.dtype, np.float64)
        self.assertEqual(layer.grad_bias.dtype, np.float64)

        #检测初始化是否符合预期
        fan_in = 2*4*4#He初始化，输入通道数 × 卷积核高度 × 卷积核宽度
        scale = np.sqrt(2.0 / fan_in)
        expected_weight = np.random.default_rng(7).normal(
            loc = 0.0,scale = scale,size = (3,2,4,4),
        ).astype(np.float64)
        np.testing.assert_allclose(layer.weight,expected_weight)
        #除了权重以外的所有参数初始化都应该为0
        np.testing.assert_array_equal(layer.bias,np.zeros(3))
        np.testing.assert_array_equal(
            layer.grad_weight,
            np.zeros((3, 2, 4, 4)),
        )
        np.testing.assert_array_equal(
            layer.grad_bias,
            np.zeros(3),
        )

    def test_parameters_and_gradients_have_matching_order(self):
        layer = layers.Conv2D(
            in_channels= 2,out_channels = 3,
            kernel_size = 4,rng = np.random.default_rng(7),
        )

        #检查类中是否含有参数和梯度
        parameters = getattr(layer,"parameters",None)
        gradients = getattr(layer,"gradients",None)

        self.assertTrue(callable(parameters))
        self.assertTrue(callable(gradients))

        parameter_list = parameters()
        gradient_list = gradients()

        #参数和梯度都应该为两个，权重和偏置
        self.assertEqual(len(parameter_list),2)
        self.assertEqual(len(gradient_list),2)

        self.assertIs(parameter_list[0], layer.weight)
        self.assertIs(parameter_list[1], layer.bias)
        self.assertIs(gradient_list[0], layer.grad_weight)
        self.assertIs(gradient_list[1], layer.grad_bias)

#检测输入、输出通道数、卷积核大小和步长是否大于0
    def test_constructor_rejects_nonpositive_out_channels(self):
        for out_channels in [0,-1]:
            with self.subTest(out_channels = out_channels):
                try:
                    layers.Conv2D(in_channels=2,out_channels=out_channels,kernel_size=3)
                except ValueError as error:
                    self.assertIn("out_channels",str(error))
                else:
                    self.fail(
                        "Conv2D should reject nonpositive out_channels"
                    )
    def test_constructor_rejects_nonpositive_in_channels(self):
        for in_channels in [0, -1]:
            with self.subTest(in_channels=in_channels):
                try:
                    layers.Conv2D(
                        in_channels=in_channels,
                        out_channels=3,
                        kernel_size=3,
                    )
                except Exception as error:
                    self.assertIsInstance(error, ValueError)
                    self.assertIn("in_channels", str(error))
                else:
                    self.fail(
                        "Conv2D should reject nonpositive in_channels"
                    )
    def test_constructor_rejects_nonpositive_kernel_size(self):
        for kernel_size in [0, -1]:
            with self.subTest(kernel_size=kernel_size):
                try:
                    layers.Conv2D(
                        in_channels=2,
                        out_channels=3,
                        kernel_size=kernel_size,
                    )
                except Exception as error:
                    self.assertIsInstance(error, ValueError)
                    self.assertIn("kernel_size", str(error))
                else:
                    self.fail(
                        "Conv2D should reject nonpositive kernel_size"
                    )
    def test_constructor_rejects_nonpositive_stride(self):
        for stride in [0, -1]:
            with self.subTest(stride=stride):
                try:
                    layers.Conv2D(
                        in_channels=2,
                        out_channels=3,
                        kernel_size=3,
                        stride=stride,
                    )
                except ValueError as error:
                    self.assertIn("stride", str(error))
                else:
                    self.fail(
                        "Conv2D should reject nonpositive stride"
                    )
    #检测填充是否非负
    def test_constructor_rejects_negative_padding(self):
        for padding in [-1, -2]:
            with self.subTest(padding=padding):
                try:
                    layers.Conv2D(
                        in_channels=2,
                        out_channels=3,
                        kernel_size=3,
                        padding=padding,
                    )
                except ValueError as error:
                    self.assertIn("padding", str(error))
                else:
                    self.fail(
                        "Conv2D should reject negative padding"
                    )

    #检测参数是否会拒绝非整数
    def test_constructor_rejects_noninteger_configuration(self):
        valid_configuration = {
            "in_channels":2,
            "out_channels":3,
            "kernel_size":3,
            "stride":1,"padding":0,
        }

        parameter_names = [
            "in_channels","out_channels","kernel_size","stride","padding"
        ]

        for parameter_name in parameter_names:
            for invalid_value in [1.5,True]:
                with self.subTest(
                    parameter_name = parameter_name,
                    invalid_value = invalid_value,
                ):
                    configuration = valid_configuration.copy()
                    configuration[parameter_name] = invalid_value
                    try:
                        #使用二重解包，相当于 key = value
                        #使用一重解包则只有键
                        layers.Conv2D(**configuration)
                    except Exception as error:
                        self.assertIsInstance(error,ValueError)
                        self.assertIn(parameter_name,str(error))
                    else:
                        self.fail(
                            "Conv2D should reject noninteger "
                            f"{parameter_name}"
                        )

    #检测前向传播是否会拒绝非4维的输入
    def test_forward_rejects_non_4d_input(self):
        layer = layers.Conv2D(
            in_channels = 2,out_channels = 3,kernel_size = 3,
        )
        #检测forward是否存在
        forward = getattr(layer,"forward",None)
        self.assertTrue(callable(forward))

        #检查forward是否拒绝非合法的输入
        #构造非合法的输入
        invalid_inputs = [
            np.ones((2,5,5)),
            np.ones((1,2,3,4,5)),
        ]
        for x in invalid_inputs:
            with self.subTest(input_shape = x.shape):
                try:
                    layer.forward(x)
                except Exception as error:
                    self.assertIsInstance(error,ValueError)
                    self.assertIn("4D",str(error))
                else:
                    self.fail(
                        "Conv2D.forward() should reject non-4D input"
                    )

    #检测前向传播传入的通道数是否正确
    def test_forward_rejects_wrong_input_channel_count(self):
        layer = layers.Conv2D(
            in_channels = 2,
            out_channels = 3,
            kernel_size = 3,
        )
        x = np.ones((1,3,5,5))
        #层要求的输入通道数：2
        #实际输入形状：(1, 3, 5, 5)
        #实际通道数：3
        try:
            layer.forward(x)
        except ValueError as error:
            self.assertIn("expected 2 input channels",str(error))
        else:
            self.fail(
                "Conv2D.forward() should reject "
                "the wrong input channel count"
            )

    #检查卷积核的大小是否要大于输入的长宽(扩展后)
    def test_forward_rejects_kernel_larger_than_padded_input(self):
        layer = layers.Conv2D(
            in_channels = 2,
            out_channels = 3,
            kernel_size = 5,
            padding = 1
        )
        padding = 1
        invalid_inputs = [
            np.ones((1,2,2,6)),
            np.ones((1,2,6,2))
        ]

        for x in invalid_inputs:
            with self.subTest(padded_input_height = x.shape[2]+2*padding,
                            padded_input_width = x.shape[3]+2*padding):
                try:
                    layer.forward(x)
                except ValueError as error:
                    self.assertIn("kernel_size",str(error))
                else:
                    self.fail(
                        "Conv2D.forward() should reject a kernel "
                        "larger than the padded input"
                    )

    #检测卷积前向传播输出的形状是否正确
    def test_forward_returns_expected_output_shape_with_flooring(self):
        layer = layers.Conv2D(
            in_channels=2,
            out_channels=3,
            kernel_size=3,
            stride=2,
            padding=1,
        )
        x= np.ones((2,2,6,7))
        output = layer.forward(x)
        self.assertIsInstance(output,np.ndarray)#检测output是否为numpy数组
        #H_out = floor((H + 2P - K) / S) + 1
        #W_out = floor((W + 2P - K) / S) + 1
        #H：输入高度
        #W：输入宽度
        #P：padding，扩展的圈数
        #K：kernel_size，卷积核大小
        #S：stride，步长
        #剩余空间不足一次完整移动时，不能把卷积核的一部分放到输入外面
        #所以要进行向下取整
        self.assertEqual(output.shape, (2, 3, 3, 4))

    # 检查单样本、单通道卷积的具体计算结果
    def test_forward_computes_single_channel_known_values(self):
        layer = layers.Conv2D(
            in_channels=1,
            out_channels=1,
            kernel_size=2,
        )

        # 手动固定参数，避免随机初始化影响结果
        #选中 layer.weight/layer.bias 中的全部元素，然后把右边的数据写进去
        layer.weight[...] = np.ones((1, 1, 2, 2))
        layer.bias[...] = np.array([0.5])

        x = np.array(
            [
                [
                    [
                        [1.0, 2.0, 3.0],
                        [4.0, 5.0, 6.0],
                        [7.0, 8.0, 9.0],
                    ]
                ]
            ]
        )

        actual = layer.forward(x)

        expected = np.array(
            [
                [
                    [
                        [12.5, 16.5],
                        [24.5, 28.5],
                    ]
                ]
            ]
        )

        np.testing.assert_allclose(actual, expected)

    #检查多通道多样本的卷积计算结果
    def test_forward_computes_multiple_batches_and_channels_and_adds_bias_once(self):
        layer = layers.Conv2D(
            in_channels = 2,
            out_channels = 2,
            kernel_size = 1
        )
        #输出通道，输入通道，卷积核大小
        layer.weight[0,:,0,0] = [1.0,10.0]
        layer.weight[1,:,0,0] = [-1.0,2.0]
        layer.bias[...] = np.array([1.0,-1.0])
        x = np.array([
            [  # 第 0 个样本
                [
                    [1.0, 2.0],
                    [3.0, 4.0],
                ],  # 输入通道 0
                [
                    [10.0, 20.0],
                    [30.0, 40.0],
                ],  # 输入通道 1
            ],
            [  # 第 1 个样本
                [
                    [5.0, 6.0],
                    [7.0, 8.0],
                ],  # 输入通道 0
                [
                    [50.0, 60.0],
                    [70.0, 80.0],
                ],  # 输入通道 1
            ],
        ])
        expected = np.array([
            [  # 第 0 个样本
                [
                    [102.0, 203.0],
                    [304.0, 405.0],
                ],  # 输出通道 0
                [
                    [18.0, 37.0],
                    [56.0, 75.0],
                ],  # 输出通道 1
            ],
            [  # 第 1 个样本
                [
                    [506.0, 607.0],
                    [708.0, 809.0],
                ],  # 输出通道 0
                [
                    [94.0, 113.0],
                    [132.0, 151.0],
                ],  # 输出通道 1
            ],
        ])
        actual = layer.forward(x)
        self.assertEqual(actual.shape,(2,2,2,2))#NCHW
        np.testing.assert_allclose(actual,expected)

    #检查卷积窗口在移动的时候是否为stride步长
    def test_forward_uses_stride_to_select_input_windows(self):
        layer = layers.Conv2D(
            in_channels=1,
            out_channels=1,
            kernel_size=2,
            stride=2,
        )
        layer.weight[...] = 1.0
        layer.bias[...] = 0.0
        x = np.array([
            [
                [
                    [1.0,  2.0,  3.0,  4.0],
                    [5.0,  6.0,  7.0,  8.0],
                    [9.0, 10.0, 11.0, 12.0],
                    [13.0, 14.0, 15.0, 16.0],
                ]
            ]
        ])
        actual = layer.forward(x)
        expected = np.array([
            [
                [
                    [14.0, 22.0],
                    [46.0, 54.0],
                ]
            ]
        ])
        self.assertEqual(actual.shape, (1, 1, 2, 2))
        np.testing.assert_allclose(actual, expected)

    #测试填充是否生效
    def test_forward_uses_zero_padding_around_spatial_dimensions(self):
        layer = layers.Conv2D(
            in_channels=1,
            out_channels=1,
            kernel_size=2,
            padding=1,
        )

        layer.weight[...] = 1.0
        layer.bias[...] = 0.0

        x = np.array([
            [
                [
                    [1.0, 2.0],
                    [3.0, 4.0],
                ]
            ]
        ])

        actual = layer.forward(x)

        expected = np.array([
            [
                [
                    [1.0, 3.0, 2.0],
                    [4.0, 10.0, 6.0],
                    [3.0, 7.0, 4.0],
                ]
            ]
        ])

        self.assertEqual(actual.shape, (1, 1, 3, 3))
        np.testing.assert_allclose(actual, expected)

    def test_backward_requires_a_previous_forward_call(self):
        layer = layers.Conv2D(
            in_channels = 1,
            out_channels = 1,
            kernel_size = 1,
        )
        backward = getattr(layer,"backward",None)
        self.assertTrue(callable(backward))

        try :
            backward(np.ones((1,1,1,1)))
        except RuntimeError as error:
            self.assertIn("forward",str(error))
        else:
            self.fail(
                "Conv2D.backward() should require forward() first"
            )

    def test_backward_rejects_wrong_gradient_shape(self):
        layer = layers.Conv2D(
            in_channels = 1,
            out_channels = 2,
            kernel_size = 2,
        )
        x = np.ones((2,1,3,3))#NCHW
        output = layer.forward(x)

        #正确的输出形状应为(2,2,2,2)
        self.assertEqual(output.shape,(2,2,2,2))
        #故意把最后一维度写成一维构造错误形状
        wrong_grad_output = np.ones((2,2,2,1))

        try:
            layer.backward(wrong_grad_output)
        except Exception as error:
            self.assertIsInstance(error,ValueError)
            self.assertIn(
                "expected grad_output shape",
                str(error),
            )
        else:
            self.fail(
                "Conv2D.backward() should reject "
                "the wrong gradient shape"
            )

    #测试反向传播正确计算偏置的梯度
    #grad_bias[oc]=Σ grad_output[n, oc, oh, ow]
    def test_backward_computes_bias_gradient(self):
        layer = layers.Conv2D(
            in_channels=1,
            out_channels=2,
            kernel_size=1,
        )
        #偏置的梯度与参数x无关，只与输入有关
        x = np.zeros((2,1,2,2))
        layer.forward(x)
        grad_output = np.array([
            [
                [
                    [1.0, 2.0],
                    [3.0, 4.0],
                ],
                [
                    [10.0, 20.0],
                    [30.0, 40.0],
                ],
            ],
            [
                [
                    [5.0, 6.0],
                    [7.0, 8.0],
                ],
                [
                    [50.0, 60.0],
                    [70.0, 80.0],
                ],
            ],
        ])
        layer.backward(grad_output)
        expected = np.array([
            36.0,
            360.0,
        ])#每个通道的输出计算结果相加起来
        np.testing.assert_allclose(layer.grad_bias, expected)
        #Linear：一个输出特征一个偏置
        #Conv2D：一个输出通道一个偏置

    #测试反向传播正确计算卷积核/权重的梯度
    #grad_weight[oc, ic, kh, kw]=Σ input_window[ic, kh, kw] × grad_output[n, oc, oh, ow]
    def test_backward_computes_weight_gradient(self):
        layer = layers.Conv2D(
            in_channels = 1,
            out_channels = 1,
            kernel_size = 2,
        )
        layer.weight[...] = 1.0
        layer.bias[...] = 0.0

        x = np.array([
            [
                [
                    [1.0,2.0,3.0],
                    [4.0,5.0,6.0],
                    [7.0,8.0,9.0],
                ]
            ]
        ])
        layer.forward(x)
        grad_output = np.array([
            [
                [
                    [1.0, 2.0],
                    [3.0, 4.0],
                ]
            ]
        ])
        layer.backward(grad_output)
        #四个前向窗口分别是：
        #窗口0：      窗口1：
        #1 2          2 3
        #4 5          5 6
        #窗口2：      窗口3：
        #4 5          5 6
        #7 8          8 9
        #他们对应的上游梯度分别是：1,2,3,4
        #例如卷积核左上角的梯度：
        #1×1 + 2×2 + 4×3 + 5×4
        #= 1 + 4 + 12 + 20
        #= 37
        #卷积核右下角：
        #5×1 + 6×2 + 8×3 + 9×4
        #= 5 + 12 + 24 + 36
        #= 77
        expected = np.array([
            [
                [
                    [37.0, 47.0],
                    [67.0, 77.0],
                ]
            ]
        ])
        np.testing.assert_allclose(layer.grad_weight, expected)

    #测试反向传播正确计算输入梯度
    def test_backward_accumulates_overlapping_input_gradients(self):
        layer = layers.Conv2D(
            in_channels = 1,
            out_channels = 1,
            kernel_size = 2,
        )
        layer.weight[...] = np.array([
            [
                [
                    [1.0,2.0],
                    [3.0,4.0],
                ]
            ]
        ])
        layer.bias[...] = 0.0
        x = np.zeros((1,1,3,3))#NCHW
        layer.forward(x)
        grad_output = np.ones((1,1,2,2))
        expected = np.array([
            [
                [
                    [1.0, 3.0, 2.0],
                    [4.0, 10.0, 6.0],
                    [3.0, 7.0, 4.0],
                ]
            ]
        ])
        actual = layer.backward(grad_output)
        self.assertIsInstance(actual, np.ndarray)
        self.assertEqual(actual.shape, x.shape)
        np.testing.assert_allclose(actual, expected)
        #第一次放置：      第二次向右放置：
        #1 2 0             0 1 2
        #3 4 0             0 3 4
        #0 0 0             0 0 0
        #
        #第三次向下放置：  第四次右下放置：
        #0 0 0             0 0 0
        #1 2 0             0 1 2
        #3 4 0             0 3 4
        #四个矩阵相加得到：
        #1  3  2
        #4 10  6
        #3  7  4
        #偏置梯度：   上游梯度
        #权重梯度：   输入窗口 × 上游梯度
        #输入梯度：   卷积核 × 上游梯度

    def test_backward_removes_padding_from_input_gradient(self):
        layer = layers.Conv2D(
            in_channels = 1,
            out_channels = 1,
            kernel_size = 2,
            padding = 1,
        )
        layer.weight[...] = np.array([
            [
                [
                    [1.0,2.0],
                    [3.0,4.0],
                ]
            ]
        ])
        layer.bias[...] = 0.0

        x = np.zeros((1,1,2,2))
        output = layer.forward(x)
        self.assertEqual(output.shape,(1,1,3,3))

        grad_output = np.ones_like(output)
        actual = layer.backward(grad_output)

        expected = np.array([
            [
                [
                    [10.0, 10.0],
                    [10.0, 10.0],
                ]
            ]
        ])
        self.assertEqual(actual.shape, x.shape)
        np.testing.assert_allclose(actual, expected)

class TestFlatten(unittest.TestCase):
    def test_Flatten_class_is_available(self):
        self.assertTrue(hasattr(layers,"Flatten"))

    def test_forward_flattens_each_sample(self):
        layer = layers.Flatten()
        #检测前向传播是否存在
        forward = getattr(layer,"forward",None)
        self.assertTrue(callable(forward))

        x = np.arange(16,dtype = np.float64).reshape(2,2,2,2)#NCHW
        actual = forward(x)
        #第一维不变，即两个样本保留，后面进行展平，变为2*8
        expected = np.array([
            [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0],
            [8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0],
        ])
        self.assertEqual(actual.shape,expected.shape)
        np.testing.assert_array_equal(actual,expected)

    def test_backward_requires_a_previous_forward_call(self):
        #检测反向传播是否存在
        layer = layers.Flatten()
        backward = getattr(layer,"backward",None)
        self.assertTrue(callable(backward))

        try:
            layer.backward(np.ones((2,8)))
        except RuntimeError as error:
            self.assertIn("forward",str(error))
        else:
            self.fail("Flatten.backward() should require a previous forward call")

    def test_backward_rejects_wrong_gradient_shape(self):
        layer = layers.Flatten()
        layer.forward(np.zeros((2,2,2,2)))
        #故意构造错误的参数，形状为(2,7)，应该为(2,8)
        wrong_grad_output = np.ones((2,7))

        try:
            layer.backward(wrong_grad_output)
        except Exception as error:
            self.assertIsInstance(error,ValueError)
            self.assertIn("expected grad_output shape",str(error))
        else:
            self.fail("Flatten.backward() should reject the wrong gradient shape")

    #把上游梯度恢复成原来x的形状
    def test_backward_restores_original_shape_and_values(self):
        layer = layers.Flatten()
        x = np.zeros((2, 2, 2, 2))
        layer.forward(x)

        grad_output = np.arange(
            16, dtype=np.float64
        ).reshape(2, 8)

        actual = layer.backward(grad_output)
        expected = grad_output.reshape(x.shape)

        self.assertIsInstance(actual, np.ndarray)
        self.assertEqual(actual.shape, x.shape)
        np.testing.assert_array_equal(actual, expected)

    def test_has_no_trainable_parameters(self):
        layer = layers.Flatten()

        parameters = getattr(layer, "parameters", None)
        gradients = getattr(layer, "gradients", None)

        self.assertTrue(callable(parameters))
        self.assertTrue(callable(gradients))
        self.assertEqual(parameters(), [])
        self.assertEqual(gradients(), [])



if(__name__ == "__main__"):
    unittest.main()
