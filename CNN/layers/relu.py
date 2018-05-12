import numpy as np


class ReluLayer(object):
    def __init__(self):
        """
        Rectified Linear Unit
        """
        self.y = None

    def forward(self, x):
        """
        Implement forward pass of Relu

        y = x if x > 0
        y = 0 otherwise

        Parameters
        ----------
        x : np.array
            The input data of size number of training samples x number of features

        Returns
        -------
        np.array
            The output of the layer

        Stores
        -------
        self.y : np.array
             The output data (need to store for backwards pass)

        """
        self.y = np.ones(x.shape)

        self.y = np.array(x)

        self.y[self.y < 0] = 0

        print("Done relu")

        return self.y

    def backward(self, y_grad):
        """
        Implement backward pass of Relu

        Parameters
        ----------
        y_grad : np.array
            The gradient at the output

        Returns
        -------
        np.array
            The gradient at the input
        """

        j = np.array(self.y)

        j[j > 0] = 1
        j[j == 0] = 0.0

        x_grad = j*y_grad

        return x_grad

    def update_param(self, lr):
        pass  # no parameters to update
