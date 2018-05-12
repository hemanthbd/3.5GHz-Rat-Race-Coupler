from layers.conv import ConvLayer
import unittest
import numpy as np

from test.util import numerical_gradient, fake_data


class TestConv(unittest.TestCase):
    def setUp(self):
        pass

    def test_forward1(self):
        layer = ConvLayer(1, 1, 3)

        x = fake_data((1, 1, 3, 3))

        layer.W = fake_data((1, 1, 3, 3))

        layer.b = fake_data(layer.b.shape)

        y = layer.forward(x)

        should_be = np.array([[[[58., 100.,  70.],
                                [132., 204., 132.],
                                [70., 100.,  58.]]]])

        self.assertTrue(np.allclose(y, should_be))

    def test_forward2(self):
        layer = ConvLayer(2, 1, 3)

        x = fake_data((1, 2, 4, 4))
        layer.W = fake_data((1, 2, 3, 3))

        layer.b = fake_data(layer.b.shape)

        y = layer.forward(x)

        should_be = np.array([[[[1196., 1796., 1916., 1264.],
                                [1881., 2793., 2946., 1923.],
                                [2313., 3405., 3558., 2307.],
                                [1424., 2072., 2156., 1380.]]]])
        
        self.assertTrue(np.allclose(y, should_be))

    def test_forward3(self):
        layer = ConvLayer(2, 2, 3)

        x = fake_data((1, 2, 4, 4))
        layer.W = fake_data((2, 2, 3, 3))
        layer.b = fake_data(layer.b.shape)

        y = layer.forward(x)

        should_be = np.array([[[[1196., 1796., 1916., 1264.],
                                [1881., 2793., 2946., 1923.],
                                [2313., 3405., 3558., 2307.],
                                [1424., 2072., 2156., 1380.]],
                               [[2709., 4173., 4509., 3065.],
                                [4582., 7006., 7483., 5056.],
                                [5878., 8914., 9391., 6304.],
                                [4089., 6177., 6477., 4333.]]]])

        self.assertTrue(np.allclose(y, should_be))

    def test_forward4(self):
        h = 5
        layer = ConvLayer(2, 5, h)

        x = fake_data((2, 2, 8, 8))

        layer.W = fake_data((5, 2, h, h))
        layer.b = fake_data(layer.b.shape)

        y = layer.forward(x)

        from test1.test4_result import t4_should_be

        self.assertTrue(np.allclose(y, t4_should_be))

    def test_backward1(self):
        layer = ConvLayer(1, 1, 3)

        x = fake_data((1, 1, 8, 8))
        layer.W = fake_data((1, 1, 3, 3))
        layer.b = fake_data(layer.b.shape)

        y = layer.forward(x)
        x_grad = layer.backward(np.ones_like(y))

        # do numerical gradients
        nm_x_grad = numerical_gradient(layer, x, x)
        nm_w_grad = numerical_gradient(layer, x, layer.W)
        nm_b_grad = numerical_gradient(layer, x, layer.b)

        # note that this does not check the gradients of the padded elements

        self.assertTrue(np.allclose(nm_x_grad, x_grad))
        self.assertTrue(np.allclose(nm_w_grad, layer.W_grad))
        self.assertTrue(np.allclose(nm_b_grad, layer.b_grad))

    def test_backward2(self):
        layer = ConvLayer(2, 1, 3)

        x = fake_data((1, 2, 4, 4))
        layer.W = fake_data((1, 2, 3, 3))
        layer.b = fake_data(layer.b.shape)
        
        y = layer.forward(x)
        x_grad = layer.backward(np.ones_like(y))

        # do numerical gradients
        nm_x_grad = numerical_gradient(layer, x, x)
        nm_w_grad = numerical_gradient(layer, x, layer.W)
        nm_b_grad = numerical_gradient(layer, x, layer.b)

        self.assertTrue(np.allclose(nm_x_grad, x_grad))
        #print("expected", nm_x_grad)
        #print(x_grad)
        self.assertTrue(np.allclose(nm_w_grad, layer.W_grad))
        #print("expected2", nm_w_grad)
        #print(layer.W_grad)
        self.assertTrue(np.allclose(nm_b_grad, layer.b_grad))
        #print("expected3", nm_b_grad)
        #print(layer.b_grad)

    def test_backward3(self):
        layer = ConvLayer(2, 2, 3)

        x = fake_data((1, 2, 4, 4))
        layer.W = fake_data((2, 2, 3, 3))
        layer.b = fake_data(layer.b.shape)
        
        y = layer.forward(x)
        x_grad = layer.backward(np.ones_like(y))

        # do numerical gradients
        nm_x_grad = numerical_gradient(layer, x, x)
        nm_w_grad = numerical_gradient(layer, x, layer.W)
        nm_b_grad = numerical_gradient(layer, x, layer.b)

        self.assertTrue(np.allclose(nm_x_grad, x_grad))
        self.assertTrue(np.allclose(nm_w_grad, layer.W_grad))
        self.assertTrue(np.allclose(nm_b_grad, layer.b_grad))

    def test_backward3_5(self):
        layer = ConvLayer(5, 3, 3)

        x = fake_data((2, 5, 3, 3))
        layer.W = fake_data(layer.W.shape)
        layer.b = fake_data(layer.b.shape)
        y = layer.forward(x)
        x_grad = layer.backward(np.ones_like(y))

        # do numerical gradients
        nm_x_grad = numerical_gradient(layer, x, x)
        nm_w_grad = numerical_gradient(layer, x, layer.W)
        nm_b_grad = numerical_gradient(layer, x, layer.b)

        self.assertTrue(np.allclose(nm_x_grad, x_grad))
        self.assertTrue(np.allclose(nm_w_grad, layer.W_grad))
        self.assertTrue(np.allclose(nm_b_grad, layer.b_grad))

    def test_backward4(self):
        h = 5
        layer = ConvLayer(2, 5, h)

        x = fake_data((2, 2, 8, 8))
        layer.W = fake_data((5, 2, h, h))
        layer.b = fake_data(layer.b.shape)

        y = layer.forward(x)
        x_grad = layer.backward(np.ones_like(y))

        nm_x_grad = numerical_gradient(layer, x, x)
        nm_w_grad = numerical_gradient(layer, x, layer.W)
        nm_b_grad = numerical_gradient(layer, x, layer.b)

        self.assertTrue(np.allclose(nm_x_grad, x_grad))
        self.assertTrue(np.allclose(nm_w_grad, layer.W_grad))
        self.assertTrue(np.allclose(nm_b_grad, layer.b_grad))

    def test_backward5(self):
        h = 5
        layer = ConvLayer(2, 5, h)

        x = fake_data((2, 2, 8, 8))
        layer.W = fake_data((5, 2, h, h))
        layer.b = fake_data(layer.b.shape)
        y = layer.forward(x)
        y_grad = fake_data(y.shape)
        x_grad = layer.backward(y_grad)

        nm_x_grad = numerical_gradient(layer, x, x, y_grad)
        nm_w_grad = numerical_gradient(layer, x, layer.W, y_grad)
        nm_b_grad = numerical_gradient(layer, x, layer.b, y_grad)

        self.assertTrue(np.allclose(nm_x_grad, x_grad))
        #print("expected",nm_x_grad)
        #print(x_grad)
        self.assertTrue(np.allclose(nm_w_grad, layer.W_grad))
        #print("expected2",nm_w_grad)
        #print(layer.W_grad)
        self.assertTrue(np.allclose(nm_b_grad, layer.b_grad))
        #print("expected3",nm_b_grad)
        #print(layer.b_grad)


if __name__ == '__main__':
    unittest.main()
