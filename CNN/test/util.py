import numpy as np
from itertools import product


def numerical_gradient(layer, x, param, y_grad=None):
    # for now just do one param
    original = layer.forward(x)
    h = 0.001

    # init grad
    grad = np.zeros_like(param)

    # loop through all indices of all dimensions
    ranges = [list(range(i)) for i in param.shape]
    for inds in product(*ranges):
        param[inds] += h
        new_value = layer.forward(x)
        #print("new",new_value)
        param[inds] -= h
        diff = (new_value - original) / h
        if y_grad is not None:
            grad[inds] = np.sum(diff * y_grad)
        else:
            grad[inds] = np.sum(diff)

    return grad


def fake_data(size):
    """
    get fake data that is like 0,1,2,3,4, etc
    """
    return np.arange(np.product(size)).reshape(size).astype('float64')