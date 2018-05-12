import numpy as np


class MaxPoolLayer(object):
    def __init__(self, size=2):
        """
        MaxPool layer
        Ok to assume non-overlapping regions
        """
        self.locs = None  # to store max locations
        self.size = size  # size of the pooling

    def forward(self, x):
        """
        Compute "forward" computation of max pooling layer

        Parameters
        ----------
        x : np.array
            The input data of size number of training samples x number
            of input channels x number of rows x number of columns

        Returns
        -------
        np.array
            The output of the maxpooling

        Stores
        -------
        self.locs : np.array
             The locations of the maxes (needed for back propagation)
        """
        #raise NotImplementedError
        max = np.zeros((x.shape[0],x.shape[1],int(x.shape[2]/self.size),int(x.shape[3]/self.size)))

        r = x.shape[2]//self.size
        c = x.shape[3]//self.size
        self.locs = np.zeros(x.shape)

        for i in range(x.shape[0]):
            for j in range(x.shape[1]):
                for g in range (r):
                    for h in range (c):
                        idli = np.max(x[i,j,g*self.size:(g+1)*self.size,h*self.size:(h+1)*self.size])
                        sambar = x[i,j,g*self.size:(g+1)*self.size,h*self.size:(h+1)*self.size] == idli
                        max[i,j,g,h] = idli
                        sambar = sambar.reshape((self.size, self.size))
                        self.locs[i,j,g*self.size:(g+1)*self.size,h*self.size:(h+1)*self.size] = sambar

        return max



    def backward(self, y_grad):
        """
        Compute "backward" computation of maxpool layer

        Parameters
        ----------
        y_grad : np.array
            The gradient at the output

        Returns
        -------
        np.array
            The gradient at the input
        """
        #raise NotImplementedError

        x = self.locs

        r = x.shape[2] // self.size
        c = x.shape[3] // self.size


        theta = np.zeros(self.locs.shape)
        for i in range(x.shape[0]):
            for j in range(x.shape[1]):
                for g in range(r):
                    for h in range(c):
                        sambar = self.locs[i, j, g * self.size:(g + 1) * self.size, h * self.size:(h + 1) * self.size] * y_grad[
                            i, j, g, h]
                        theta[i, j, g * self.size:(g + 1) * self.size, h * self.size:(h + 1) * self.size] = sambar

        return theta

    def update_param(self, lr):
        pass