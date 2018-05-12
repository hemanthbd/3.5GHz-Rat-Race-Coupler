from layers.maxpool import MaxPoolLayer
import unittest
import numpy as np

from test.util import numerical_gradient, fake_data


class TestMaxPool(unittest.TestCase):
    def setUp(self):
        self.layer = MaxPoolLayer()
        self.x = fake_data((1,3,4,4))

    def test_forward(self):
        out = self.layer.forward(self.x)

        should_be = np.array([[[[  5.,   7.],
                                [ 13.,  15.]],
                               [[ 21.,  23.],
                                [ 29.,  31.]],
                               [[ 37.,  39.],
                                [ 45.,  47.]]]])

        self.assertTrue(np.allclose(out, should_be))

    def test_bigger(self):
        self.x = fake_data((2,4,8,8))
        out = self.layer.forward(self.x)
        print("Forward")
        from test1.max_pool_big import mp_result

        self.assertTrue(np.allclose(mp_result, out))

    def test_backward(self):
        out = self.layer.forward(self.x)
        y = fake_data((1,3,2,2))
        x_grad = self.layer.backward(y)

        should_be = np.array([[[[  0.,   0.,   0.,   0.],
                                [  0.,   0.,   0.,   1.],
                                [  0.,   0.,   0.,   0.],
                                [  0.,   2.,   0.,   3.]],
                            [[  0.,   0.,   0.,   0.],
                                [  0.,   4.,   0.,   5.],
                                [  0.,   0.,   0.,   0.],
                                [  0.,   6.,   0.,   7.]],
                            [[  0.,   0.,   0.,   0.],
                                [  0.,   8.,   0.,   9.],
                                [  0.,   0.,   0.,   0.],
                                [  0.,  10.,   0.,  11.]]]])

        self.assertTrue(np.allclose(should_be, x_grad))

    def test_backward2(self):

        nm_x_grad = numerical_gradient(self.layer, self.x, self.x)


        self.layer.forward(self.x)
        y = np.ones((1,3,2,2))
        x_grad = self.layer.backward(y)

        print("x",x_grad)
        print("expected",nm_x_grad)
        self.assertTrue(np.allclose(nm_x_grad, x_grad))

    def test_backward3(self):
        self.x = fake_data((2,3,5,5))
        nm_x_grad = numerical_gradient(self.layer, self.x, self.x)

        self.layer.forward(self.x)
        y = np.ones((2,3,2,2))
        x_grad = self.layer.backward(y)

        self.assertTrue(np.allclose(nm_x_grad, x_grad))

    def test_backward4(self):
        x = np.array([[[[0,0,0,0],
                      [0,0,1,1],
                      [2,0,0,3],
                      [2,0,3,0]]]]).astype('float64')
        
        nm_x_grad = numerical_gradient(self.layer, x, x)

        out = self.layer.forward(x)
        y = np.ones((1,1,2,2))
        x_grad = self.layer.backward(y)

        self.assertTrue(np.allclose(nm_x_grad, x_grad))

if __name__ == '__main__':
    unittest.main()
