import numpy as np


class SoftMaxLayer(object):
    def __init__(self):
        """
        Constructor
        """
        self.y = None

    def forward(self, x):
        """
        Implement forward pass of softmax

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
             The output of the layer (needed for backpropagation)
        """

        self.y = np.array(x.shape)

        max1 = np.max(x, axis=-1, keepdims=True)
        e = np.exp(x - max1)
        sum1 = np.sum(e, axis=-1, keepdims=True)

        self.y = e / sum1
        print("Done softmax")
        return self.y

    def backward(self, y_grad):
        """
        Compute "backward" computation of softmax

        Parameters
        ----------
        y_grad : np.array
            The gradient at the output

        Returns
        -------
        np.array
            The gradient at the input

        """

        x_grad = np.zeros(y_grad.shape)

        for i in range(len(self.y)):
            x = np.diag(self.y[i])

            j = x - np.outer(self.y[i].T, self.y[i])

            x_grad[i] = np.dot(y_grad[i], j).reshape(1, self.y.shape[1])

        return x_grad

    def update_param(self, lr):
        pass  # no learning for softmax layer
