import numpy as np
from backprop.neuron import Neuron


class Layer():
    def __init__(self, nneurons, ninputs):
        self._neurons = [Neuron(ninputs) for i in range(nneurons)]
    
    def predict(self, x):
        return np.array([n.predict(x) for n in self._neurons])
