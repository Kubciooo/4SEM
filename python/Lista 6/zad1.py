import numpy as np
import matplotlib as plt

# dlaczego ostatnia kolumna to same 1? 
# Ponieważ robimy trik - dodajemy jeden wymiar z wsp. 1 
# wtedy dostaniemy nie tylko gradient, ale też przesunięcie
# innymi słowy to jest bias z zadań 2 i 3. 

def sigmoid(x):
    return 1.0/(1+np.exp(-x))

def sigmoid_derivative(x):
    return x * (1.0 - x)


def ReLu(x):
    return x * (x > 0)

def ReLu_derivative(x):
    return 1. * (x > 0)

np.random.seed(17)

class NeuralNetwork:
    def __init__(self, x, y, func, func_derivative, func2, func2_derivative):
        self.input              = x
        self.y                  = y
        self.weights1           = np.random.rand(4,self.input.shape[1])
        self.weights2           = np.random.rand(1,4)
        self.output             = np.zeros(self.y.shape)
        self.eta                = 0.01
        self.func               = func
        self.func_derivative    = func_derivative
        self.func2              = func2
        self.func2_derivative   = func2_derivative
    def feedforward(self):
        self.layer1 = self.func(np.dot(self.input, self.weights1.T))
        self.output = self.func2(np.dot(self.layer1, self.weights2.T))


    def backprop(self):
        delta2 = (self.y - self.output) * self.func2_derivative(self.output)
        d_weights2 = self.eta * np.dot(delta2.T, self.layer1)
        delta1 = self.func_derivative(self.layer1) * np.dot(delta2, self.weights2)
        d_weights1 = self.eta * np.dot(delta1.T, self.input)
        self.weights1 += d_weights1
        self.weights2 += d_weights2




def tworz_sieci(X,y):
    siec1 = NeuralNetwork(X,y,sigmoid,sigmoid_derivative,sigmoid, sigmoid_derivative)
    siec2 = NeuralNetwork(X,y,ReLu,ReLu_derivative, ReLu, ReLu_derivative)
    siec3 = NeuralNetwork(X,y,sigmoid,sigmoid_derivative, ReLu, ReLu_derivative)
    siec4 = NeuralNetwork(X, y, ReLu, ReLu_derivative, sigmoid, sigmoid_derivative)
    return siec1, siec2, siec3, siec4

def wykonaj_iteracje(siec1, siec2,siec3, siec4, count = 5000):
    for _ in range(count):
        siec1.feedforward()
        siec1.backprop()
        siec2.feedforward()
        siec2.backprop()
        siec3.feedforward()
        siec3.backprop()
        siec4.feedforward()
        siec4.backprop()

X = np.array([
    [0,0,1],
    [0,1,1],
    [1,0,1],
    [1,1,1]
    ])
y = np.array([[0], [1], [1], [0]])
siec1, siec2, siec3, siec4 = tworz_sieci(X,y)
wykonaj_iteracje(siec1,siec2, siec3, siec4)
np.set_printoptions(precision=3,suppress=True)
print("XOR:")
print("Poprawne:")
print(y.T)
print("Sigmoid: ")
print([round(x,3) for x in siec1.output.T[0]])
print("ReLU:")
print(siec2.output.T)
print("Sigmoid + ReLu:")
print([round(x,3) for x in siec3.output.T[0]])
print("ReLu + Sigmoid:")
print([round(x,3) for x in siec4.output.T[0]])



y = np.array([[0],[0],[0],[1]])
siec1, siec2, siec3, siec4 = tworz_sieci(X,y)
wykonaj_iteracje(siec1,siec2, siec3, siec4)
print("AND:")
print("Poprawne:")
print(y.T)
print("Sigmoid: ")
print([round(x,3) for x in siec1.output.T[0]])
print("ReLU:")
print(siec2.output.T)
print("Sigmoid + ReLu:")
print([round(x,3) for x in siec3.output.T[0]])
print("ReLu + Sigmoid:")
print([round(x,3) for x in siec4.output.T[0]])


y = np.array([[0],[1],[1],[1]])
siec1, siec2, siec3, siec4 = tworz_sieci(X,y)
wykonaj_iteracje(siec1,siec2, siec3, siec4)
print("OR:")
print("Poprawne:")
print(y.T)
print("Sigmoid: ")
print([round(x,3) for x in siec1.output.T[0]])
print("ReLU:")
print(siec2.output.T)
print("Sigmoid + ReLu:")
print([round(x,3) for x in siec3.output.T[0]])
print("ReLu + Sigmoid:")
print([round(x,3) for x in siec4.output.T[0]])

