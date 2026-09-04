import unittest
import numpy as np
from mininn import model
from mininn import layers
from mininn import optim
from mininn import losses
import mininn
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

class TestSGD(unittest.TestCase):
    def test_sgd_class_is_available(self):
        self.assertTrue(hasattr(optim,"SGD"))

    #检测类是否能接收必要的变量
    def test_constructor_accepts_parameters_gradients_and_learning_rate(self):
        parameters = np.array([1.0,-2.0])
        gradients = np.array([0.5,-1.5])
        try:
            optim.SGD([parameters],[gradients],learning_rate = 0.1,)
        except TypeError as error:
            self.fail("SGD should accept parameters,gradients and learning_rate: "f"{error}")

    #检测是否含有step方法
    def test_step_method_is_available(self):
        parameter = np.array([1.0,-2.0])
        gradient = np.array([0.5,-1.5])
        optimizer = optim.SGD([parameter],[gradient],learning_rate = 0.1)
        step = getattr(optimizer,"step",None)
        self.assertTrue(callable(step))

    #检测step函数是否是原地修改变量
    def test_step_updates_parameters_in_place(self):
        parameter = np.array([1.0,-2.0])
        gradient = np.array([0.5,-1.5])
        optimizer = optim.SGD([parameter],[gradient],learning_rate = 0.1)
        original_parameter = parameter
        optimizer.step()
        #assertIs 用于保证优化器修改的是原数组，而不是创建新数组
        self.assertIs(parameter,original_parameter)
        np.testing.assert_allclose(parameter,np.array([0.95,-1.85]))

    #检测传入的参数和梯度数量是否相等
    def test_constructor_rejects_parameter_gradient_count_mismatch(self):
        parameters = [
            np.zeros(2),
            np.zeros(3),
        ]
        gradients = [np.zeros(2)]
        try:
            optim.SGD(parameters,gradients,learning_rate = 0.1)
        except ValueError as error:
            self.assertIn("equal counts",str(error))
        else:
            self.fail(
                "SGD should reject different parameter and gradient counts"
            )

    def test_constructor_rejects_parameter_gradient_shape_mismatch(self):
        parameter = np.zeros((2,2))
        gradient = np.zeros((3,2))
        try:
            optim.SGD([parameter],[gradient],learning_rate = 0.1)
        except ValueError as error:
            self.assertIn("shape",str(error))
        else:
            self.fail(
                "SGD should reject parameter and gradient shape mismatch"
            )

    def test_constructor_rejects_nonpositive_learning_rate(self):
        parameter = np.zeros(2)
        gradient = np.zeros(2)
        for learning_rate in [0.0,-0.1]:
            #相当于分别测试0.0和-0.1，避免在第一次断言失败之后程序就直接停止
            #使用它后各组输入可以分别执行和报告
            with self.subTest(learning_rate = learning_rate):
                try:
                    optim.SGD([parameter],[gradient],learning_rate)
                except ValueError as error:
                    self.assertIn("positive",str(error))
                else:
                    self.fail(
                        "SGD should reject a nonpositive learning rate"
                    )

class TestTrainingLoop(unittest.TestCase):
    def test_three_class_training_reduces_loss_and_reaches_target_accuracy(self):
        rng = np.random.default_rng(7)
        centers = np.array([
            [-1.0,-1.0],
            [1.0,-1.0],
            [0.0,1.0],
        ])

        #创建初始化训练数据
        #对三个类别中心进行轻微扰动，每个类别生成100份数据最后拼接起来
        #类别0数据：(100, 2)
        #类别1数据：(100, 2)
        #类别2数据：(100, 2)
        x = np.vstack([
            rng.normal(center,0.35,size = (100,2))
            for center in centers
        ])

        #标签数据[0, 0, ..., 0, 1, 1, ..., 1, 2, 2, ..., 2]
        labels = np.repeat(np.arange(3),100)#labels.shape == (300,)

        #创建神经网络，两个线性层中间用ReLU()激活函数进行连接
        #x (300, 2)
        #    │
        #    ▼
        #Linear(2, 16)
        #    │ (300, 16)
        #    ▼
        #ReLU
        #    │ (300, 16)
        #    ▼
        #Linear(16, 3)
        #    │
        #    ▼
        #logits (300, 3)
        network = model.Sequential(
            layers.Linear(2,16,rng = rng),
            layers.ReLU(),
            layers.Linear(16,3,rng = rng),
        )

        #损失函数的创建，使用softmax交叉熵损失函数
        loss_function = losses.SoftmaxCrossEntropyLoss()

        #创建优化器
        optimizer = optim.SGD(
            network.parameters(),
            network.gradients(),
            learning_rate = 0.1,
        )

        #记录训练前的损失
        initial_loss = loss_function.forward(
            network.forward(x),
            labels,
        )

        #完整训练闭环
        #第一步：网络前向传播
        #logits = network.forward(x)
        #形状变化：
        #(300, 2)
        #→ (300, 16)
        #→ (300, 16)
        #→ (300, 3)
        #同时各层会缓存反向传播需要的信息：
        #- 第一个 Linear 缓存原始输入；
        #- ReLU 缓存正数位置；
        #- 第二个 Linear 缓存隐藏层输出。
        #第二步：损失前向传播
        #loss_function.forward(logits, labels)
        #虽然这里没有保存返回的损失值，但这个调用不能省略，因为它还会缓存：
        #- Softmax概率；
        #- 正确标签。
        #这些数据是下一行 backward() 必须使用的。
        #第三步：反向传播
        #network.backward(loss_function.backward())
        #先执行：
        #loss_function.backward()
        #得到：
        #dL/dlogits，形状为 (300, 3)
        #然后将梯度传给网络：
        #network.backward(...)
        #完整传播过程为：
        #损失函数
        #dL/dlogits: (300, 3)
        #        │
        #        ▼
        #第二个 Linear.backward()
        #产生 dW2、db2
        #返回梯度: (300, 16)
        #        │
        #        ▼
        #ReLU.backward()
        #返回梯度: (300, 16)
        #        │
        #        ▼
        #第一个 Linear.backward()
        #产生 dW1、db1
        #返回梯度: (300, 2)
        #最后返回的 (300, 2) 输入梯度没有继续使用，因为输入数据 x 不是需要训练的参数。
        #这个框架也不需要单独调用 zero_grad()，因为每次 Linear.backward() 都会覆盖梯度数组，而不是累加梯度。
        #第四步：更新参数
        #optimizer.step()
        #使用刚刚计算出的四组梯度更新：
        #W1、b1、W2、b2
        for _ in range(300):
            logits = network.forward(x)
            loss_function.forward(logits,labels)
            network.backward(loss_function.backward())
            optimizer.step()

        #计算训练后的结果
        final_logits = network.forward(x)
        final_loss = loss_function.forward(
            final_logits,
            labels,
        )

        #计算准确率
        #从每个样本的三个类别分数中选出最大值所在的类别
        #300个样本每一行取得最大值，然后与标签进行比较最后取平均值计算准确率
        accuracy = np.mean(
            np.argmax(final_logits,axis = 1) == labels
        )

        self.assertLess(final_loss,initial_loss * 0.5)
        self.assertGreaterEqual(accuracy,0.85)

class TestPublicAPI(unittest.TestCase):
    def test_package_exports_training_components(self):
        expected_names = [
            "Linear",#线性层
            "ReLU",#ReLU激活函数
            "Conv2D",#卷积层
            "SoftmaxCrossEntropyLoss",#交叉熵损失函数
            "Sequential",#全连接层
            "SGD",#随机梯度下降优化器
            "Flatten",#卷积展平层
        ]
        for name in expected_names:
            with self.subTest(name = name):
                #如果断言时报则会报出错误信息f"mininn should export {name}"
                self.assertTrue(hasattr(mininn,name),f"mininn should export {name}")
                self.assertIn(name,mininn.__all__,f"{name} should be listed in mininn.__all__")

#测试小型CNN网络
class TestToyCNN(unittest.TestCase):
    #测试前向传播的输出形状正确
    def test_forward_return_two_class_logits(self):
        rng = np.random.default_rng(7)
        network = model.Sequential(
            layers.Conv2D(in_channels = 1,out_channels = 2
                        ,kernel_size = 3,padding = 1,rng = rng),
            layers.ReLU(),
            layers.Flatten(),
            layers.Linear(2*8*8,2,rng = rng),
        )
        #(3, 1, 8, 8)
        #→ Conv2D
        #(3, 2, 8, 8)
        #→ Flatten
        #(3, 128)
        #→ Linear
        #(3, 2)
        x = np.zeros((3,1,8,8),dtype = np.float64)
        logits = network.forward(x)
        self.assertEqual(logits.shape, (3, 2))

    ##测试反向传播的输出形状正确
    def test_backward_returns_nchw_input_gradient(self):
        rng = np.random.default_rng(7)
        network = model.Sequential(
            layers.Conv2D(in_channels = 1,out_channels = 2
                        ,kernel_size = 3,padding = 1,rng = rng),
            layers.ReLU(),
            layers.Flatten(),
            layers.Linear(2*8*8,2,rng = rng),
        )
        x = np.ones((3,1,8,8),dtype = np.float64)
        logits = network.forward(x)
        #(3, 2)
        #→ Linear.backward
        #(3, 128)
        #→ Flatten.backward
        #(3, 2, 8, 8)
        #→ ReLU.backward
        #(3, 2, 8, 8)
        #→ Conv2D.backward
        #(3, 1, 8, 8)
        grad_output = np.ones_like(logits)
        grad_input = network.backward(grad_output)
        self.assertEqual(grad_input.shape, x.shape)
if(__name__ == "__main__"):
    unittest.main()
