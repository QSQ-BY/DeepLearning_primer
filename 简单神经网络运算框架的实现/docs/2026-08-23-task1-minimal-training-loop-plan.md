# Task 1 Minimal Training Loop Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and verify a NumPy-only neural-network library containing `Linear`, `ReLU`, `SoftmaxCrossEntropyLoss`, `Sequential`, and `SGD`, then train a small classifier end to end.

**Architecture:** Each layer owns its forward cache and explicitly implements its local backward derivative. `Sequential` passes values forward and gradients backward, while `SGD` updates stable parameter and gradient array references in place. Tests use only `unittest` and NumPy and are written before production behavior.

**Tech Stack:** Python 3.14, NumPy 2.5, Python standard-library `unittest`, ordinary `.py` modules (no notebook and no deep-learning library).

## Global Constraints

- Work from `D:\code\DeepLearning\简单神经网络运算框架的实现` when running tests and examples.
- Production code, tests, examples, and data helpers may import only Python standard-library modules and NumPy.
- Every behavior follows Red-Green-Refactor: write one test, observe the expected failure, add the minimum implementation, and rerun all tests.
- Do not implement automatic differentiation, a common layer base class, momentum, regularization, data loaders, convolution, or BatchNorm in this plan.
- Keep parameter and gradient arrays as stable objects; `backward()` overwrites gradient contents in place.

---

## File Map

- `mininn/layers.py`: `Linear` and `ReLU` implementations.
- `mininn/losses.py`: stable combined softmax and cross-entropy loss.
- `mininn/model.py`: sequential layer composition.
- `mininn/optim.py`: in-place stochastic-gradient-descent updates.
- `mininn/__init__.py`: public imports for library users.
- `tests/test_layers.py`: deterministic forward/backward and gradient tests for layers.
- `tests/test_losses.py`: deterministic and numerical tests for the loss.
- `tests/test_training.py`: model, optimizer, and full training-loop tests.
- `examples/train_toy_classifier.py`: reproducible three-class demonstration.

### Task 1: Linear forward propagation

**Files:**
- Modify: `tests/test_layers.py`
- Modify: `mininn/layers.py`

**Interfaces:**
- Produces: `Linear(in_features: int, out_features: int, rng: numpy.random.Generator | None = None)`
- Produces: `Linear.forward(x: numpy.ndarray) -> numpy.ndarray`
- Stores: `weight` with shape `(in_features, out_features)` and `bias` with shape `(out_features,)`

- [ ] **Step 1: Write a failing test for the public class**

Replace `tests/test_layers.py` with:

```python
import unittest

from mininn import layers


class TestLinear(unittest.TestCase):
    def test_linear_class_is_available(self):
        self.assertTrue(hasattr(layers, "Linear"))


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the test and verify RED**

Run from `简单神经网络运算框架的实现`:

```powershell
python -m unittest tests.test_layers.TestLinear.test_linear_class_is_available -v
```

Expected: `FAIL` because `mininn.layers` does not yet define `Linear`.

- [ ] **Step 3: Add the smallest class declaration**

Replace `mininn/layers.py` with:

```python
class Linear:
    pass
```

- [ ] **Step 4: Verify GREEN**

Run the same test. Expected: `OK`.

- [ ] **Step 5: Replace the test with constructor and known-value forward tests**

Replace `tests/test_layers.py` with:

```python
import unittest

import numpy as np

from mininn.layers import Linear


class TestLinear(unittest.TestCase):
    def test_constructor_creates_expected_parameter_shapes(self):
        layer = Linear(2, 3, rng=np.random.default_rng(7))

        self.assertEqual(layer.weight.shape, (2, 3))
        self.assertEqual(layer.bias.shape, (3,))
        self.assertEqual(layer.weight.dtype, np.float64)
        self.assertEqual(layer.bias.dtype, np.float64)

    def test_forward_computes_matrix_product_and_bias(self):
        layer = Linear(2, 2, rng=np.random.default_rng(7))
        layer.weight[...] = np.array([[1.0, 2.0], [3.0, 4.0]])
        layer.bias[...] = np.array([0.5, -0.5])
        x = np.array([[1.0, 2.0], [-1.0, 3.0]])

        actual = layer.forward(x)

        expected = np.array([[7.5, 9.5], [8.5, 9.5]])
        np.testing.assert_allclose(actual, expected)

    def test_forward_rejects_wrong_feature_count(self):
        layer = Linear(2, 3, rng=np.random.default_rng(7))

        with self.assertRaisesRegex(ValueError, "expected 2 input features"):
            layer.forward(np.ones((4, 5)))


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 6: Run the new tests and verify RED**

Run:

```powershell
python -m unittest tests.test_layers.TestLinear -v
```

Expected: errors because `Linear` does not accept constructor arguments and has no `forward()`.

- [ ] **Step 7: Implement constructor and forward propagation**

Replace `mininn/layers.py` with:

```python
import numpy as np


class Linear:
    def __init__(self, in_features, out_features, rng=None):
        if not isinstance(in_features, int) or in_features <= 0:
            raise ValueError("in_features must be a positive integer")
        if not isinstance(out_features, int) or out_features <= 0:
            raise ValueError("out_features must be a positive integer")

        if rng is None:
            rng = np.random.default_rng()

        scale = np.sqrt(2.0 / in_features)
        self.weight = rng.normal(
            loc=0.0,
            scale=scale,
            size=(in_features, out_features),
        ).astype(np.float64)
        self.bias = np.zeros(out_features, dtype=np.float64)
        self._input = None

    def forward(self, x):
        x = np.asarray(x)
        if x.ndim != 2:
            raise ValueError("Linear input must be a 2D array")
        if x.shape[1] != self.weight.shape[0]:
            raise ValueError(
                f"Linear expected {self.weight.shape[0]} input features, "
                f"but received {x.shape[1]}"
            )

        self._input = x
        return x @ self.weight + self.bias
```

- [ ] **Step 8: Verify GREEN and run the full suite**

Run:

```powershell
python -m unittest discover -s tests -v
```

Expected: all current tests pass.

- [ ] **Step 9: Commit the completed forward behavior**

```powershell
git add mininn/layers.py tests/test_layers.py
git commit -m "feat: add Linear forward propagation"
```

### Task 2: Linear backward propagation and parameter access

**Files:**
- Modify: `tests/test_layers.py`
- Modify: `mininn/layers.py`

**Interfaces:**
- Consumes: `Linear.forward(x)` from Task 1
- Produces: `Linear.backward(grad_output) -> grad_input`
- Produces: `Linear.parameters() -> list[numpy.ndarray]`
- Produces: `Linear.gradients() -> list[numpy.ndarray]`
- Stores stable arrays: `grad_weight`, `grad_bias`

- [ ] **Step 1: Add failing backward and access tests**

Add these methods to `TestLinear` in `tests/test_layers.py`:

```python
    def test_backward_computes_input_and_parameter_gradients(self):
        layer = Linear(2, 2, rng=np.random.default_rng(7))
        layer.weight[...] = np.array([[1.0, 2.0], [3.0, 4.0]])
        x = np.array([[1.0, 2.0], [-1.0, 3.0]])
        grad_output = np.array([[1.0, -1.0], [2.0, 3.0]])
        layer.forward(x)

        grad_input = layer.backward(grad_output)

        np.testing.assert_allclose(
            grad_input,
            np.array([[-1.0, -1.0], [8.0, 18.0]]),
        )
        np.testing.assert_allclose(
            layer.grad_weight,
            np.array([[-1.0, -4.0], [8.0, 7.0]]),
        )
        np.testing.assert_allclose(layer.grad_bias, np.array([3.0, 2.0]))

    def test_parameters_and_gradients_have_matching_order(self):
        layer = Linear(2, 3, rng=np.random.default_rng(7))

        parameters = layer.parameters()
        gradients = layer.gradients()

        self.assertIs(parameters[0], layer.weight)
        self.assertIs(parameters[1], layer.bias)
        self.assertIs(gradients[0], layer.grad_weight)
        self.assertIs(gradients[1], layer.grad_bias)

    def test_backward_requires_a_previous_forward_call(self):
        layer = Linear(2, 3, rng=np.random.default_rng(7))

        with self.assertRaisesRegex(RuntimeError, "forward"):
            layer.backward(np.ones((4, 3)))
```

- [ ] **Step 2: Run and verify RED**

Run:

```powershell
python -m unittest tests.test_layers.TestLinear -v
```

Expected: errors because gradient attributes and backward/access methods do not exist.

- [ ] **Step 3: Add minimum backward implementation**

In `Linear.__init__`, immediately after `self.bias`, add:

```python
        self.grad_weight = np.zeros_like(self.weight)
        self.grad_bias = np.zeros_like(self.bias)
```

Add these methods to `Linear`:

```python
    def backward(self, grad_output):
        if self._input is None:
            raise RuntimeError("Linear.backward() requires forward() first")

        grad_output = np.asarray(grad_output)
        expected_shape = (self._input.shape[0], self.weight.shape[1])
        if grad_output.shape != expected_shape:
            raise ValueError(
                f"Linear expected grad_output shape {expected_shape}, "
                f"but received {grad_output.shape}"
            )

        self.grad_weight[...] = self._input.T @ grad_output
        self.grad_bias[...] = grad_output.sum(axis=0)
        return grad_output @ self.weight.T

    def parameters(self):
        return [self.weight, self.bias]

    def gradients(self):
        return [self.grad_weight, self.grad_bias]
```

- [ ] **Step 4: Verify GREEN**

Run the full suite. Expected: all tests pass.

- [ ] **Step 5: Add a numerical-gradient test**

Add this method to `TestLinear`:

```python
    def test_weight_gradient_matches_finite_difference(self):
        layer = Linear(2, 2, rng=np.random.default_rng(7))
        x = np.array([[0.2, -0.4], [1.2, 0.7]])
        grad_output = np.array([[0.3, -0.6], [0.8, 0.5]])
        layer.forward(x)
        layer.backward(grad_output)
        analytic = layer.grad_weight.copy()
        numerical = np.zeros_like(layer.weight)
        epsilon = 1e-6

        for index in np.ndindex(layer.weight.shape):
            original = layer.weight[index]
            layer.weight[index] = original + epsilon
            plus = np.sum(layer.forward(x) * grad_output)
            layer.weight[index] = original - epsilon
            minus = np.sum(layer.forward(x) * grad_output)
            layer.weight[index] = original
            numerical[index] = (plus - minus) / (2.0 * epsilon)

        np.testing.assert_allclose(analytic, numerical, rtol=1e-6, atol=1e-8)
```

- [ ] **Step 6: Run the numerical test and verify it passes**

Run:

```powershell
python -m unittest tests.test_layers.TestLinear.test_weight_gradient_matches_finite_difference -v
```

Expected: `OK`; this test verifies existing backward behavior rather than adding a new production feature.

- [ ] **Step 7: Commit backward propagation**

```powershell
git add mininn/layers.py tests/test_layers.py
git commit -m "feat: add Linear backward propagation"
```

### Task 3: ReLU forward and backward propagation

**Files:**
- Modify: `tests/test_layers.py`
- Modify: `mininn/layers.py`

**Interfaces:**
- Produces: `ReLU.forward(x) -> numpy.ndarray`
- Produces: `ReLU.backward(grad_output) -> numpy.ndarray`
- Produces empty `parameters()` and `gradients()` lists

- [ ] **Step 1: Add failing ReLU tests**

Update the test import:

```python
from mininn.layers import Linear, ReLU
```

Add this test class before the `if __name__` block:

```python
class TestReLU(unittest.TestCase):
    def test_forward_replaces_nonpositive_values_with_zero(self):
        layer = ReLU()
        x = np.array([[-2.0, 0.0, 3.0]])

        actual = layer.forward(x)

        np.testing.assert_allclose(actual, np.array([[0.0, 0.0, 3.0]]))

    def test_backward_keeps_gradient_only_for_positive_inputs(self):
        layer = ReLU()
        layer.forward(np.array([[-2.0, 0.0, 3.0]]))

        actual = layer.backward(np.array([[4.0, 5.0, 6.0]]))

        np.testing.assert_allclose(actual, np.array([[0.0, 0.0, 6.0]]))

    def test_backward_requires_a_previous_forward_call(self):
        with self.assertRaisesRegex(RuntimeError, "forward"):
            ReLU().backward(np.ones((1, 3)))

    def test_relu_has_no_trainable_parameters(self):
        layer = ReLU()

        self.assertEqual(layer.parameters(), [])
        self.assertEqual(layer.gradients(), [])
```

- [ ] **Step 2: Run and verify RED**

Run:

```powershell
python -m unittest tests.test_layers.TestReLU -v
```

Expected: import error because `ReLU` is not defined.

- [ ] **Step 3: Implement ReLU**

Append to `mininn/layers.py`:

```python
class ReLU:
    def __init__(self):
        self._positive_mask = None

    def forward(self, x):
        x = np.asarray(x)
        self._positive_mask = x > 0
        return np.maximum(0, x)

    def backward(self, grad_output):
        if self._positive_mask is None:
            raise RuntimeError("ReLU.backward() requires forward() first")

        grad_output = np.asarray(grad_output)
        if grad_output.shape != self._positive_mask.shape:
            raise ValueError(
                f"ReLU expected grad_output shape {self._positive_mask.shape}, "
                f"but received {grad_output.shape}"
            )
        return grad_output * self._positive_mask

    def parameters(self):
        return []

    def gradients(self):
        return []
```

- [ ] **Step 4: Verify GREEN and commit**

Run all tests, then:

```powershell
git add mininn/layers.py tests/test_layers.py
git commit -m "feat: add ReLU layer"
```

### Task 4: Stable Softmax cross-entropy loss

**Files:**
- Modify: `tests/test_losses.py`
- Modify: `mininn/losses.py`

**Interfaces:**
- Produces: `SoftmaxCrossEntropyLoss.forward(logits, labels) -> float`
- Produces: `SoftmaxCrossEntropyLoss.backward() -> numpy.ndarray`

- [ ] **Step 1: Write failing known-value and validation tests**

Replace `tests/test_losses.py` with:

```python
import unittest

import numpy as np

from mininn import losses


class TestSoftmaxCrossEntropyLoss(unittest.TestCase):
    def test_loss_class_is_available(self):
        self.assertTrue(hasattr(losses, "SoftmaxCrossEntropyLoss"))


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run and verify RED**

Run:

```powershell
python -m unittest tests.test_losses -v
```

Expected: `FAIL` because the class is absent.

- [ ] **Step 3: Add the class shell, verify GREEN, then replace tests with behavior tests**

Replace `mininn/losses.py` with:

```python
class SoftmaxCrossEntropyLoss:
    pass
```

Verify the first test passes. Then replace `tests/test_losses.py` with:

```python
import unittest

import numpy as np

from mininn.losses import SoftmaxCrossEntropyLoss


class TestSoftmaxCrossEntropyLoss(unittest.TestCase):
    def test_equal_logits_have_log_class_count_loss(self):
        loss = SoftmaxCrossEntropyLoss()
        logits = np.zeros((2, 3))
        labels = np.array([0, 2])

        actual = loss.forward(logits, labels)

        self.assertAlmostEqual(actual, np.log(3.0))

    def test_forward_is_stable_for_large_logits(self):
        loss = SoftmaxCrossEntropyLoss()
        logits = np.array([[1000.0, 1001.0, 1002.0]])

        actual = loss.forward(logits, np.array([2]))

        self.assertTrue(np.isfinite(actual))

    def test_backward_returns_mean_logit_gradient(self):
        loss = SoftmaxCrossEntropyLoss()
        loss.forward(np.zeros((2, 2)), np.array([0, 1]))

        actual = loss.backward()

        expected = np.array([[-0.25, 0.25], [0.25, -0.25]])
        np.testing.assert_allclose(actual, expected)

    def test_forward_rejects_noninteger_labels(self):
        loss = SoftmaxCrossEntropyLoss()

        with self.assertRaisesRegex(ValueError, "integer"):
            loss.forward(np.zeros((2, 3)), np.array([0.0, 1.0]))

    def test_backward_requires_a_previous_forward_call(self):
        with self.assertRaisesRegex(RuntimeError, "forward"):
            SoftmaxCrossEntropyLoss().backward()


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 4: Run behavior tests and verify RED**

Expected: errors because `forward()` and `backward()` do not exist.

- [ ] **Step 5: Implement stable forward and backward propagation**

Replace `mininn/losses.py` with:

```python
import numpy as np


class SoftmaxCrossEntropyLoss:
    def __init__(self):
        self._probabilities = None
        self._labels = None

    def forward(self, logits, labels):
        logits = np.asarray(logits)
        labels = np.asarray(labels)

        if logits.ndim != 2:
            raise ValueError("logits must be a 2D array")
        if labels.ndim != 1:
            raise ValueError("labels must be a 1D array")
        if not np.issubdtype(labels.dtype, np.integer):
            raise ValueError("labels must contain integer class indices")
        if logits.shape[0] == 0:
            raise ValueError("the batch must contain at least one sample")
        if labels.shape[0] != logits.shape[0]:
            raise ValueError("logits and labels must have the same batch size")
        if np.any(labels < 0) or np.any(labels >= logits.shape[1]):
            raise ValueError("label index is outside the class range")

        shifted = logits - logits.max(axis=1, keepdims=True)
        exp_shifted = np.exp(shifted)
        sums = exp_shifted.sum(axis=1, keepdims=True)
        self._probabilities = exp_shifted / sums
        self._labels = labels.copy()

        correct_logits = shifted[np.arange(logits.shape[0]), labels]
        log_normalizers = np.log(sums[:, 0])
        return float(np.mean(log_normalizers - correct_logits))

    def backward(self):
        if self._probabilities is None or self._labels is None:
            raise RuntimeError(
                "SoftmaxCrossEntropyLoss.backward() requires forward() first"
            )

        gradient = self._probabilities.copy()
        gradient[np.arange(gradient.shape[0]), self._labels] -= 1.0
        gradient /= gradient.shape[0]
        return gradient
```

- [ ] **Step 6: Verify GREEN**

Run all tests. Expected: all pass.

- [ ] **Step 7: Add and run a finite-difference test**

Add to `TestSoftmaxCrossEntropyLoss`:

```python
    def test_logit_gradient_matches_finite_difference(self):
        loss = SoftmaxCrossEntropyLoss()
        logits = np.array([[0.2, -0.3, 0.7], [1.1, 0.4, -0.2]])
        labels = np.array([2, 0])
        loss.forward(logits, labels)
        analytic = loss.backward()
        numerical = np.zeros_like(logits)
        epsilon = 1e-6

        for index in np.ndindex(logits.shape):
            plus_logits = logits.copy()
            minus_logits = logits.copy()
            plus_logits[index] += epsilon
            minus_logits[index] -= epsilon
            plus = loss.forward(plus_logits, labels)
            minus = loss.forward(minus_logits, labels)
            numerical[index] = (plus - minus) / (2.0 * epsilon)

        np.testing.assert_allclose(analytic, numerical, rtol=1e-6, atol=1e-8)
```

Run the new test and the full suite. Expected: all pass.

- [ ] **Step 8: Commit the loss**

```powershell
git add mininn/losses.py tests/test_losses.py
git commit -m "feat: add stable softmax cross-entropy loss"
```

### Task 5: Sequential model composition

**Files:**
- Modify: `tests/test_training.py`
- Modify: `mininn/model.py`

**Interfaces:**
- Consumes: layer `forward`, `backward`, `parameters`, and `gradients` interfaces
- Produces: `Sequential(*layers)` with the same four methods

- [ ] **Step 1: Write failing composition tests**

Replace `tests/test_training.py` with:

```python
import unittest

import numpy as np

from mininn.layers import Linear, ReLU
from mininn.model import Sequential


class TestSequential(unittest.TestCase):
    def test_forward_and_backward_follow_opposite_layer_orders(self):
        rng = np.random.default_rng(7)
        first = Linear(2, 3, rng=rng)
        activation = ReLU()
        second = Linear(3, 2, rng=rng)
        model = Sequential(first, activation, second)
        x = np.array([[0.5, -1.0], [1.0, 2.0]])

        output = model.forward(x)
        grad_input = model.backward(np.ones_like(output))

        self.assertEqual(output.shape, (2, 2))
        self.assertEqual(grad_input.shape, x.shape)

    def test_parameters_and_gradients_include_only_trainable_layers(self):
        rng = np.random.default_rng(7)
        first = Linear(2, 3, rng=rng)
        second = Linear(3, 2, rng=rng)
        model = Sequential(first, ReLU(), second)

        self.assertEqual(len(model.parameters()), 4)
        self.assertEqual(len(model.gradients()), 4)
        self.assertIs(model.parameters()[0], first.weight)
        self.assertIs(model.parameters()[2], second.weight)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run and verify RED**

Expected: import error because `Sequential` is absent.

- [ ] **Step 3: Implement the minimum model container**

Replace `mininn/model.py` with:

```python
class Sequential:
    def __init__(self, *layers):
        if not layers:
            raise ValueError("Sequential requires at least one layer")
        self.layers = list(layers)

    def forward(self, x):
        output = x
        for layer in self.layers:
            output = layer.forward(output)
        return output

    def backward(self, grad_output):
        gradient = grad_output
        for layer in reversed(self.layers):
            gradient = layer.backward(gradient)
        return gradient

    def parameters(self):
        parameters = []
        for layer in self.layers:
            parameters.extend(layer.parameters())
        return parameters

    def gradients(self):
        gradients = []
        for layer in self.layers:
            gradients.extend(layer.gradients())
        return gradients
```

- [ ] **Step 4: Verify GREEN and commit**

Run all tests, then:

```powershell
git add mininn/model.py tests/test_training.py
git commit -m "feat: add Sequential model container"
```

### Task 6: SGD parameter updates

**Files:**
- Modify: `tests/test_training.py`
- Modify: `mininn/optim.py`

**Interfaces:**
- Consumes: stable parameter and gradient lists from `Sequential`
- Produces: `SGD(parameters, gradients, learning_rate)` and `step() -> None`

- [ ] **Step 1: Add a failing exact-update test**

Add this import to `tests/test_training.py`:

```python
from mininn.optim import SGD
```

Add this test class before the `if __name__` block:

```python
class TestSGD(unittest.TestCase):
    def test_step_updates_parameters_in_place(self):
        parameter = np.array([1.0, -2.0])
        gradient = np.array([0.5, -1.5])
        optimizer = SGD([parameter], [gradient], learning_rate=0.1)
        original_reference = parameter

        optimizer.step()

        self.assertIs(parameter, original_reference)
        np.testing.assert_allclose(parameter, np.array([0.95, -1.85]))

    def test_constructor_rejects_shape_mismatch(self):
        with self.assertRaisesRegex(ValueError, "shape"):
            SGD(
                [np.zeros((2, 2))],
                [np.zeros((3, 2))],
                learning_rate=0.1,
            )
```

- [ ] **Step 2: Run and verify RED**

Expected: import error because `SGD` is absent.

- [ ] **Step 3: Implement the minimum optimizer**

Replace `mininn/optim.py` with:

```python
class SGD:
    def __init__(self, parameters, gradients, learning_rate):
        self.parameters = list(parameters)
        self.gradients = list(gradients)

        if len(self.parameters) != len(self.gradients):
            raise ValueError("parameters and gradients must have equal counts")
        if learning_rate <= 0:
            raise ValueError("learning_rate must be positive")

        for parameter, gradient in zip(self.parameters, self.gradients):
            if parameter.shape != gradient.shape:
                raise ValueError("parameter and gradient shape mismatch")

        self.learning_rate = learning_rate

    def step(self):
        for parameter, gradient in zip(self.parameters, self.gradients):
            parameter -= self.learning_rate * gradient
```

- [ ] **Step 4: Verify GREEN and commit**

Run all tests, then:

```powershell
git add mininn/optim.py tests/test_training.py
git commit -m "feat: add SGD optimizer"
```

### Task 7: End-to-end training and public package API

**Files:**
- Modify: `tests/test_training.py`
- Modify: `mininn/__init__.py`
- Modify: `examples/train_toy_classifier.py`

**Interfaces:**
- Consumes: all previous components
- Produces: public imports from `mininn`
- Produces: reproducible toy-classification example

- [ ] **Step 1: Add the failing training-loop test**

Add these imports to `tests/test_training.py`:

```python
from mininn.losses import SoftmaxCrossEntropyLoss
```

Add this test class before the `if __name__` block:

```python
class TestTrainingLoop(unittest.TestCase):
    def test_three_class_training_reduces_loss_and_reaches_target_accuracy(self):
        rng = np.random.default_rng(42)
        centers = np.array([[-1.0, -1.0], [1.0, -1.0], [0.0, 1.0]])
        x = np.vstack(
            [rng.normal(center, 0.35, size=(100, 2)) for center in centers]
        )
        labels = np.repeat(np.arange(3), 100)
        model = Sequential(
            Linear(2, 16, rng=rng),
            ReLU(),
            Linear(16, 3, rng=rng),
        )
        loss_function = SoftmaxCrossEntropyLoss()
        optimizer = SGD(model.parameters(), model.gradients(), learning_rate=0.1)

        initial_loss = loss_function.forward(model.forward(x), labels)
        for _ in range(300):
            logits = model.forward(x)
            loss_function.forward(logits, labels)
            model.backward(loss_function.backward())
            optimizer.step()

        final_logits = model.forward(x)
        final_loss = loss_function.forward(final_logits, labels)
        accuracy = np.mean(np.argmax(final_logits, axis=1) == labels)

        self.assertLess(final_loss, initial_loss * 0.5)
        self.assertGreaterEqual(accuracy, 0.85)
```

- [ ] **Step 2: Run the integration test**

Run:

```powershell
python -m unittest tests.test_training.TestTrainingLoop -v
```

Expected: `OK` if the component interfaces compose correctly. If it fails, do not loosen the thresholds; diagnose the first incorrect component with its focused tests.

- [ ] **Step 3: Add the public package exports**

Replace `mininn/__init__.py` with:

```python
from .layers import Linear, ReLU
from .losses import SoftmaxCrossEntropyLoss
from .model import Sequential
from .optim import SGD

__all__ = [
    "Linear",
    "ReLU",
    "SoftmaxCrossEntropyLoss",
    "Sequential",
    "SGD",
]
```

- [ ] **Step 4: Write the demonstration program**

Replace `examples/train_toy_classifier.py` with:

```python
from pathlib import Path
import sys

import numpy as np


PROJECT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_DIR))

from mininn import Linear, ReLU, SGD, Sequential, SoftmaxCrossEntropyLoss


def make_dataset(rng):
    centers = np.array([[-1.0, -1.0], [1.0, -1.0], [0.0, 1.0]])
    features = np.vstack(
        [rng.normal(center, 0.35, size=(100, 2)) for center in centers]
    )
    labels = np.repeat(np.arange(3), 100)
    return features, labels


def main():
    rng = np.random.default_rng(42)
    features, labels = make_dataset(rng)
    model = Sequential(
        Linear(2, 16, rng=rng),
        ReLU(),
        Linear(16, 3, rng=rng),
    )
    loss_function = SoftmaxCrossEntropyLoss()
    optimizer = SGD(model.parameters(), model.gradients(), learning_rate=0.1)

    for epoch in range(301):
        logits = model.forward(features)
        loss_value = loss_function.forward(logits, labels)
        model.backward(loss_function.backward())
        optimizer.step()

        if epoch % 50 == 0:
            accuracy = np.mean(np.argmax(logits, axis=1) == labels)
            print(
                f"epoch={epoch:3d} "
                f"loss={loss_value:.6f} "
                f"accuracy={accuracy:.2%}"
            )


if __name__ == "__main__":
    main()
```

- [ ] **Step 5: Run all tests and the example**

Run:

```powershell
python -m unittest discover -s tests -v
python examples/train_toy_classifier.py
```

Expected: all tests pass; the printed loss declines and final printed accuracy is at least 85%.

- [ ] **Step 6: Check the dependency constraint**

Run:

```powershell
rg -n "torch|tensorflow|keras|jax" mininn tests examples
```

Expected: no matches.

- [ ] **Step 7: Commit the training closure**

```powershell
git add mininn/__init__.py tests/test_training.py examples/train_toy_classifier.py
git commit -m "feat: complete NumPy training loop"
```

### Task 8: Final verification and learning checkpoint

**Files:**
- Verify only: all files under `mininn/`, `tests/`, and `examples/`

**Interfaces:**
- Consumes: complete first-stage library
- Produces: reproducible verification evidence and a user explanation of one training iteration

- [ ] **Step 1: Run the full verification commands**

```powershell
python -m unittest discover -s tests -v
python examples/train_toy_classifier.py
```

Expected: clean test output, decreasing loss, and final accuracy of at least 85%.

- [ ] **Step 2: Explain the data flow without reading source**

The user should be able to explain, in order:

```text
features
-> Linear.forward
-> ReLU.forward
-> Linear.forward
-> SoftmaxCrossEntropyLoss.forward
-> SoftmaxCrossEntropyLoss.backward
-> second Linear.backward
-> ReLU.backward
-> first Linear.backward
-> SGD.step
```

- [ ] **Step 3: Record exact verification output for the later Task 1 report**

Save the test count, initial/final loss, final accuracy, Python version, and NumPy version in the later report notes. Do not add Conv2D or BatchNorm until this stage is understood and reproducible.
