import numpy as np
import matplotlib.pyplot as plt

from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras import regularizers
from keras.callbacks import Callback


x = np.linspace(0,2,26).T
y = np.sin((3*np.pi/2) * x)
#y = x
testing_x = np.linspace(0,2,101).T
model = Sequential()
act = 'relu'
if np.min(y) >= 0 and np.max(y) <= 1: 
    act = 'sigmoid'
elif np.min(y) >= -1 and np.max(y) <= 1:
    act = 'tanh'
model.add(Dense(10, activation=act, kernel_regularizer=regularizers.l2(0.00000001), input_shape = (1,)))
model.add(Dense(10, activation=act, kernel_regularizer=regularizers.l2(0.00000001)))

model.add(Dense(1, activation=act, kernel_regularizer=regularizers.l2(0.00000001)))

model.compile(loss='mse',optimizer=Adam())

class Test1(Callback):
    def __init__(self, xy):
        self.out_log = []
        self.xy = xy

    def on_epoch_end(self, epochs, logs={}):
        if epochs % 100 == 0:
            plt.cla()
            plt.title(f"iteracja {epochs}")
            plt.ylabel("y = x**2")
            plt.xlabel("x")
            plt.scatter(self.xy,self.model.predict(self.xy))
            plt.pause(.0000001)
        
model.fit(x,y, epochs=1500000, callbacks=[Test1(testing_x)], validation_split=0.3)
plt.title("iteracja 1500000")
plt.ylabel("y = x**2")
plt.xlabel("x")
plt.scatter(x,y)
plt.show()