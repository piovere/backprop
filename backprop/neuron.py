import numpy as np


class Neuron():
    def __init__(self, ninputs):
        self._weights = np.random.random(ninputs)
        self._bias = 1.0
    
    def predict(self, x):
        o = self.net(x)
        return self.transfer(o)
    
    def net(self, x):
        return self._weights.dot(x) + self._bias

    def transfer(self, x):
        # return np.exp(x) / (np.exp(x) + 1)
        return x
    
    def transfer_derivative(self, x):
        # return self.transfer(x) * (1 - self.transfer(x))
        return 1
    
    def error(self, x, y):
        return y - self.predict(x)

    def update(self, x, y):
        e = self.error(x, y)
