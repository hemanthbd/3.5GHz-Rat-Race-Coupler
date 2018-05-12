import numpy as np


class FlattenLayer(object):
    def __init__(self):
        """
        Flatten layer
        """
        self.orig_shape = None # to store the shape for backpropagation

    def forward(self, x):
        """
        Compute "forward" computation of flatten layer

        Parameters
        ----------
        x : np.array
            The input data of size number of training samples x number
            of input channels x number of rows x number of columns

        Returns
        -------
        np.array
            The output of the flatten operation
            size = training samples x (number of input channels * number of rows * number of columns)
            (should make a copy of the data with np.copy)

        Stores
        -------
        self.orig_shape : list
             The original shape of the data
        """

        # f = x.reshape(x.shape[0], (x.shape[1]*x.shape[2]*x.shape[3]))
        f = np.zeros((x.shape[0], (x.shape[1]*x.shape[2]*x.shape[3])))
        print(f.shape)
        for b in range(0, x.shape[0]):
            d = 0
            for c in range(0, x.shape[1]):
                for p in range(0, x.shape[2]):
                    for q in range(0, x.shape[3]):
                        f[b, d] = x[b, c, p, q]
                        d = d+1

        self.orig_shape = x.shape

        print("Done flatten")
        return f

    def backward(self, y_grad):
        """
        Compute "backward" computation of flatten layer

        Parameters
        ----------
        y_grad : np.array
            The gradient at the output

        Returns
        -------
        np.array
            The gradient at the input
        """
        x_grad = np.zeros(self.orig_shape)

        for b in range(0,self.orig_shape[0]):
            d = 0
            for c in range(0,self.orig_shape[1]):
                for p in range(0,self.orig_shape[2]):
                    for q in range(0,self.orig_shape[3]):
                        x_grad[b, c, p, q] = y_grad[b, d]
                        d = d+1

        #y_grad = y_grad.reshape(self.orig_shape[0], self.orig_shape[1], self.orig_shape[2], self.orig_shape[3])
        #print(x_grad.shape)
        return x_grad

    def update_param(self, lr):
        pass
