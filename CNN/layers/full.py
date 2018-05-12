import numpy as np


class FullLayer(object):
    def __init__(self, n_i, n_o):
        """
        Fully connected layer

        Parameters
        ----------

        n_i : integer
            The number of inputs
        n_o : integer
            The number of outputs
        """
        self.x = None
        self.W_grad = None
        self.b_grad = None

        # need to initialize self.W and self.b

        self.W = np.random.normal(0, np.sqrt(2.0/(n_i+n_o)), (n_i, n_o)).T.astype('float64')

        # self.b = np.random.rand(n_o,).astype('float64')
        self.b = np.zeros(n_o, ).astype('float64')

    def forward(self, x):
        """
        Compute "forward" computation of fully connected layer

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
        self.x : np.array
             The input data (need to store for backwards pass)
        """

        f = x.dot(self.W.transpose()) + self.b

        self.x = x
        print("Done full")
        return f

    def backward(self, y_grad):
        """
        Compute "backward" computation of fully connected layer

        Parameters
        ----------
        y_grad : np.array
            The gradient at the output

        Returns
        -------
        np.array
            The gradient at the input

        Stores
        -------
        self.b_grad : np.array
             The gradient with respect to b (same dimensions as self.b)
        self.W_grad : np.array
             The gradient with respect to W (same dimensions as self.W
        """

        x_grad = np.dot(y_grad, self.W)

        self.W_grad = np.zeros(self.W.shape)
        for i in range(len(self.x)):
            q = np.dot(y_grad[i].reshape(1, y_grad.shape[1]).T, self.x[i].reshape(1, self.x.shape[1]))
            self.W_grad = q+ self.W_grad

        self.b_grad = np.zeros(self.b.shape)
        for i in range(len(y_grad)):
            self.b_grad = np.add(y_grad[i], self.b_grad)

        return x_grad

    def update_param(self, lr):
        """
        Update the parameters with learning rate lr

        Parameters
        ----------
        lr : floating point
            The learning rate

        Stores
        -------
        self.W : np.array
             The updated value for self.W
        self.b : np.array
             The updated value for self.b
        """

        self.W = self.W - lr*self.W_grad

        self.b = self.b - lr*self.b_grad
