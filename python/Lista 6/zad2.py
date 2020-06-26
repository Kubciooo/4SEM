import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1.0/(1+np.exp(-x))

def sigmoid_derivative(x):
    return x * (1.0 - x)
    

def euclid_squared(a, b):
    return sum((x_a - x_b) ** 2 for x_a, x_b in zip(a, b))
def mse(x,y):
    #błąd średniokwadratowy 
    return 1/len(x) * np.sum([euclid_squared(x[n],y[n]) for n in range(len(x))])


def ReLu(x):
    return x * (x > 0)

def ReLu_derivative(x):
    return 1. * (x > 0)

def tanh(x):
    return np.tanh(x)

def tanh_derivative(x):
    return 1.0 - np.tanh(x)**2

class NeuralNetwork:
    def __init__(self, x, y, func, func_derivative,eta=0.001):
        self.input              = x
        self.y                  = y
        self.weights1           = np.random.rand(10,self.input.shape[1])*2 - 1
        self.weights2           = np.random.rand(1,10) * 2 - 1
        self.output             = np.zeros(self.y.shape)
        self.eta                = eta
        self.func               = func
        self.func_derivative    = func_derivative
        self.bias              = np.random.rand(1)

    def feedforward(self):
        self.layer1 = self.func(np.dot(self.input, self.weights1.T)+self.bias)
        self.output = self.func(np.dot(self.layer1, self.weights2.T))


    def backprop(self):
        delta2 = (self.y - self.output) * self.func_derivative(self.output)
        d_weights2 = self.eta * np.dot(delta2.T, self.layer1)
        delta1 = self.func_derivative(self.layer1) * np.dot(delta2, self.weights2)
        d_weights1 = self.eta * np.dot(delta1.T, self.input)
        self.weights1 += d_weights1
        self.weights2 += d_weights2
        for d in delta2:
            self.bias -= d*self.eta

    def predict(self, predict_x):
        self.layer1 = self.func(np.dot(predict_x, self.weights1.T)+self.bias)
        self.output = self.func(np.dot(self.layer1, self.weights2.T))
        return self.output




def wykonaj_iteracje(siec1,dane, count = 5000000):
    for i in range(count):
        siec1.feedforward()
        siec1.backprop()
        if i % 1000 == 0: 
            plt.cla()
            plt.title(f"iteracja {i}  błąd: {mse(siec1.output, siec1.y)}")
            plt.xlabel("x")
            plt.scatter(dane,siec1.predict(dane))
            plt.scatter(siec1.input, siec1.y)
            plt.pause(.0000001)


######################TUTAJ WPISYWAĆ DANE! ##########################
np.random.seed(23)
# x = x=np.linspace(-50,50,26)
x = np.linspace(0,2,21)
x = np.reshape(x,(x.shape[0],1))
# y = x**2
y = np.sin((3*np.pi/2) * x)
# testing_x = np.linspace(-50,50,101)
testing_x = np.linspace(0,2,161)
testing_x = np.reshape(testing_x, (testing_x.shape[0],1))

######################################################################
a = np.min(y)
b = np.max(y)
siec1 = NeuralNetwork(x,y,ReLu,ReLu_derivative,eta=0.0000005)
if a >= 0 and b <= 1:
    siec1 = NeuralNetwork(x,y,sigmoid,sigmoid_derivative)
elif a >= -1 and b <=1:
    siec1 = NeuralNetwork(x,y,tanh,tanh_derivative)

wykonaj_iteracje(siec1,testing_x)
plt.title(f"po wszystkich iteracjach")
plt.xlabel("x")
plt.scatter(testing_x,siec1.predict(testing_x))
plt.scatter(siec1.input, siec1.y)
plt.show()