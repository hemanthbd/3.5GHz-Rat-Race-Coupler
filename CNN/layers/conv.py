import numpy as np
import scipy.signal


class ConvLayer(object):
    def __init__(self, n_i, n_o, h):
        """
        Convolutional layer

        Parameters
        ----------
        n_i : integer
            The number of input channels
        n_o : integer
            The number of output channels
        h : integer
            The size of the filter
        """
        # glorot initialization

        self.W = np.random.normal(0, np.sqrt(2.0 / (n_i + n_o)), (h, h, n_i, n_o)).T.astype('float64')
        # self.b = np.random.rand(n_o,).astype('float64')

        self.x = None
        # self.W = np.random.normal((n_o, n_i, h, h)).astype('float64')
        self.b = np.zeros((1, n_o)).astype('float64')

        self.n_i = n_i
        self.n_o = n_o

        self.W_grad = None
        self.b_grad = None

    def forward(self, x):
        """
        Compute "forward" computation of convolutional layer

        Parameters
        ----------
        x : np.array
            The input data of size number of training samples x number
            of input channels x number of rows x number of columns

        Returns
        -------
        np.array
            The output of the convolutiona

        Stores
        -------
        self.x : np.array
             The input data (need to store for backwards pass)
        """
        # print(x)
        if self.W.shape[2] % 2 != 0:
            p = (self.W.shape[2] - 1) / 2

        sig = np.zeros((x.shape[0], self.W.shape[0], x.shape[2], x.shape[3]))

        for t in range(0, x.shape[0]):
            for n in range(0, self.W.shape[0]):
                for c in range(0, x.shape[1]):

                        x1 = x[t, c, :, :]

                        x2 = np.zeros((x.shape[2] + 2 * int(p), x.shape[3] + 2 * int(p)))
                        x2[:, :] = np.pad(x1[:, :], (int(p), int(p)), 'constant', constant_values=(0))

                        sig[t, n, :, :] += scipy.signal.correlate(x2[:, :], self.W[n, c, :, :], mode='valid')

        for t in range(0, x.shape[0]):
            for n in range(0, self.W.shape[0]):
                sig[t, n, :, :] += self.b[0, n]

        self.x = x
        #print("Done convolution")
        #print(sig)
        return sig

    def backward(self, y_grad):
        """
        Compute "backward" computation of convolutional layer

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
        self.w_grad : np.array
             The gradient with respect to W (same dimensions as self.W
        """
        self.b_grad = np.zeros(self.b.shape)

        # bi= np.array(self.b_grad.shape).reshape(1,self.b.shape[1])

        for n in range(y_grad.shape[1]):
            self.b_grad[0, n] = np.sum(y_grad[:, n, :, :])

        if self.W.shape[2] % 2 != 0:
            p = (self.W.shape[2] - 1) / 2

        self.W_grad = np.zeros(self.W.shape)
        x_grad = np.zeros(self.x.shape)

        for t in range(0, y_grad.shape[0]):
            for n in range(0, y_grad.shape[1]):
                for c in range(0, self.x.shape[1]):

                        x1 = self.x[t, c, :, :]
                        #y2 = y_grad[t, n, :, :]

                        x2 = np.zeros((self.x.shape[2] + 2 * int(p), self.x.shape[3] + 2 * int(p)))
                        x2[:, :] = np.pad(x1[:, :], (int(p), int(p)), 'constant', constant_values=0)

                        #y2 = np.zeros((y_grad.shape[2] + 2 * int(p), y_grad.shape[3] + 2 * int(p)))
                        #y2[:, :] = np.pad(y_grad[:, :], (int(p), int(p)), 'constant', constant_values=0)

                        self.W_grad[n, c, :, :] += scipy.signal.correlate(x2[:, :], y_grad[t, n, :, :], mode='valid')
                        x_grad[t, c, :, :] += scipy.signal.convolve2d(y_grad[t, n, :, :],
                                                                      self.W[n, c, :, :], mode='same')

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
        print(self.W_grad)
        self.b = self.b - lr*self.b_grad
