from __future__ import print_function
import numpy as np
import math


class Sequential(object):
    def __init__(self, layers, loss):
        """
        Sequential model

        Implements a sequence of layers

        Parameters
        ----------
        layers : list of layer objects
        loss : loss object
        """

        self.layers = layers
        self.loss = loss
        self.loss1 = []
        self.loss2 = []

    def forward(self, x, target=None):
        """
        Forward pass through all layers
        
        if target is not none, then also do loss layer

        Parameters
        ----------
        x : np.array
            The input data of size number of training samples x number of features
        target : np.array
            The target data of size number of training samples x number of features (one-hot)

        Returns
        -------
        np.array
            The output of the model
        """
        soft = np.array(x.shape)
        for i in range(len(self.layers)):
            soft = self.layers[i].forward(x)
            x = soft

        if target is None:
            return soft
        else:
            return self.loss.forward(soft, target)

    def backward(self):
        """
        Compute "backward" computation of fully connected layer

        Returns
        -------
        np.array
            The gradient at the input

        """

        loss_grad = self.loss.backward()

        for i in range(len(self.layers)-1, -1, -1):
            loss_grad = self.layers[i].backward(loss_grad)

        return loss_grad

    def update_param(self, lr):
        """
        Update the parameters with learning rate lr

        Parameters
        ----------
        lr : floating point
            The learning rate
        """
        for i in range(len(self.layers)):
            self.layers[i].update_param(lr)

    def fit(self, x, y, x_test, y_test, epochs=1, lr=0.1, batch_size=128):
        """
        Fit parameters of all layers using batches

        Parameters
        ----------
        x : numpy matrix
            Training data (number of samples x number of features)
        y : numpy matrix
            Training labels (number of samples x number of features) (one-hot)
        epochs: integer
            Number of epochs to run (1 epoch = 1 pass through entire data)
        lr: float
            Learning rate
        batch_size: integer
            Number of data samples per batch of gradient descent
        """

        mini = np.floor(x.shape[0]/batch_size)
        left= x.shape[0]-(mini*batch_size)

        if np.mod(x.shape[0],batch_size)!=0:
            for j in range(epochs):
                loss2 = 0.0
                for i in range(0, np.int64(x.shape[0]-left), batch_size):

                    x_train_mini = x[i:i + batch_size]
                # print('1st',x_train_mini[0])
                    y_train_mini = y[i:i + batch_size]

                    loss2 += self.forward(x_train_mini, y_train_mini)

                    self.backward()
                    self.update_param(lr)

                for j in range(np.int64(x.shape[0]-left), x.shape[0], np.int64(left)):
                    x_train_min = x[j:j + np.int64(left)]
                    # print(x_train_min[0])
                    y_train_min = y[j:j + np.int64(left)]

                    cross_loss = self.forward(x_train_min, y_train_min)
                    loss2 += cross_loss

                    self.backward()
                    self.update_param(lr)

                self.loss1.append(loss2/float((x.shape[0]/batch_size)))
                x_test1= x_test.flatten(400,)
                self.loss2.append(self.forward(x_test,y_test))

        else:
            for j in range(epochs):
                loss2 = 0.0
                for i in range(0, np.int64(x.shape[0]), batch_size):
                    x_train_mini = x[i:i + batch_size]
                    y_train_mini = y[i:i + batch_size]

                    loss2+= self.forward(x_train_mini, y_train_mini)

                    self.backward()
                    self.update_param(lr)
                self.loss1.append(loss2 / float((x.shape[0] / batch_size)))

        return self.loss1,self.loss2

    def sigmoid(self, z):
        return [1 / (1 + math.exp(-e)) for e in z]

    def predict(self, x):
        """
        Return class prediction with input x

        Parameters
        ----------
        x : numpy matrix
            Testing data data (number of samples x number of features)

        Returns
        -------
        np.array
            The output of the model (integer class predictions)
        """

        pred1 = self.forward(x)
        out = np.ones(pred1.shape)
        for i in range(len(pred1)):
            out[i] = self.sigmoid(pred1[i])

        pred = np.zeros_like(out)
        pred[np.arange(len(pred1)), out.argmax(1)] = 1
        pred2= pred.argmax(1)
        return pred2
