import numpy as np


class CrossEntropyLayer(object):
    def __init__(self):
        """
        Constructor
        """
        self.x = None
        self.t = None

    def forward(self, x, t):
        """
        Implements forward pass of cross entropy

        l(x,t) = 1/N * sum(log(x) * t)

        where
        x = input (number of samples x feature dimension)
        t = target with one hot encoding (number of samples x feature dimension)
        N = number of samples (constant)

        Parameters
        ----------
        x : np.array
            The input data of size number of training samples x feature dimension
        t : np.array
            The target data (one-hot) of size number of training samples x feature dimension

        Returns
        -------
        np.array
            The output of the loss

        Stores
        -------
        self.x : np.array
             The input data (need to store for backwards pass)
        self.t : np.array
             The target data (need to store for backwards pass)
        """
        l = 0.0

        for i in range(len(x)):
            for j in range(t.shape[1]):
                l += t[i, j]*np.log(x[i, j] + 1e-9)

        l = -1.0*l/len(x)

        self.x = np.array(x)
        self.t = np.array(t)
        print(l)
        print("Done crossentropy")
        return l

    def backward(self, y_grad=None):
        """
        Compute "backward" computation of softmax loss layer

        Returns
        -------
        np.array
            The gradient at the input

        """
        x_grad = np.ones(self.x.shape)
        for i in range(len(self.x)):
            for j in range(self.t.shape[1]):
                x_grad[i, j] = -1.0*(self.t[i, j] / (self.x[i, j]))/len(self.x)

        return x_grad
