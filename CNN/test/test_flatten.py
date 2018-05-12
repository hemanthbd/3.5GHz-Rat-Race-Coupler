from layers.flatten import FlattenLayer
import unittest
import numpy as np

from test.util import numerical_gradient, fake_data


class TestConv(unittest.TestCase):
    def setUp(self):
        pass

    def test_forward1(self):
        layer = FlattenLayer()

        x = fake_data((1,2,3,3))
        y = layer.forward(x)

        self.assertTrue(y.shape == (1, 18))

    def test_backward1(self):
        layer = FlattenLayer()

        x = fake_data((1, 2, 3, 3))

        y = layer.forward(x)

        x_grad = layer.backward(np.ones_like(y))

        # do numerical gradients
        nm_x_grad = numerical_gradient(layer, x, x)
        print(x_grad)
        print(nm_x_grad)
        self.assertTrue(np.allclose(nm_x_grad, x_grad))


if __name__ == '__main__':
    unittest.main()
