import numpy as np


class Neuron():
    def __init__(self, ninputs):
        self._weights = np.random.random(ninputs)
    
    def predict(self, x):
        o = self._weights.dot(x)
        return self.transfer(o)
    
    def transfer(self, x):
        return np.exp(x) / (np.exp(x) + 1)
