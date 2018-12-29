import numpy as np


class Neuron():
    def __init__(self, ninputs):
        self._weights = np.random.random(ninputs)
        self._bias = 1.0
    
    def predict(self, x):
        o = self._weights.dot(x) + self._bias
        return self.transfer(o)
    
    def transfer(self, x):
        # return np.exp(x) / (np.exp(x) + 1)
        return x
    
    def error(self, x, y):
        return y - self.predict(x)

    def update(self, x, y):
        e = self.error(x, y)
