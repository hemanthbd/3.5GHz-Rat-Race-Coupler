from layers.dataset import cifar100
from layers.full import FullLayer
from layers.softmax import SoftMaxLayer
from layers.cross_entropy import CrossEntropyLayer
from layers.sequential import Sequential
from layers.relu import ReluLayer
from layers.conv import ConvLayer
from layers.maxpool import MaxPoolLayer
from layers.flatten import FlattenLayer

import numpy as np
import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test) = cifar100(1213076538)

layer1 = ConvLayer(3, 16, 3)
relu1 = ReluLayer()
layer2 = MaxPoolLayer(2)
layer3 = ConvLayer(16, 32, 3)
relu2 = ReluLayer()
layer4 = MaxPoolLayer(2)
layer5 = FlattenLayer()
layer6 = FullLayer(32*8*8, 4)
softmax = SoftMaxLayer()
loss = CrossEntropyLayer()


lr = 0.1
scores = []
n_epochs = 5
batch_size = 128

x_train = np.array(x_train)
y_train = np.array(y_train)
x_test = np.array(x_test)
y_test = np.array(y_test)

model = Sequential((layer1, relu1, layer2, layer3, relu2, layer4, layer5, layer6, softmax), loss)

loss2,loss3 = model.fit(x_train, y_train, x_test, y_test, n_epochs, lr, batch_size)

print("Train Loss", loss2)
print("Test Loss", loss3)
y_pred = model.predict(x_test)
print('Predictions', y_pred)
    # y_train1= y_train.argmax(1)
print('Actual', np.argmax(y_test, axis=1))
scores.append(np.mean(y_pred == np.argmax(y_test, axis=1)))

print("Neural accuracy for n_epochs=" + str(n_epochs) + " and Learning Rate=" + str(lr) + " is: " + str(np.argmax(y_test, axis=1)))


scores = np.asarray(scores)
print(scores)


fig, ax = plt.subplots()
ax.plot(range(n_epochs), loss2, 'r',label='Lr=0.1')
ax.plot(range(n_epochs) , loss3, 'g', label='Lr=0.1')
plt.xlabel('Epochs')
plt.ylabel('Value of Training & Testing Error Loss Function')
plt.title('Neural Network for CIFAR-100 for Epochs=10 ')
legend = ax.legend(loc='upper right ', shadow=True, fontsize='x-large')

# Put a nicer background color on the legend.
legend.get_frame().set_facecolor('#00FFCC')

plt.show()


