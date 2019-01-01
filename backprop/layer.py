import numpy as np
from backprop.neuron import Neuron


class Layer():
    def __init__(self, nneurons, ninputs):
        self._neurons = [Neuron(ninputs) for i in range(nneurons)]
    
    def predict(self, x):
        self._last_input = x
        self._last_output = np.array([n.predict(x) for n in self._neurons])
        return self._last_output


class OutputLayer(Layer):
    def __init__(self, ninputs):
        super().__init__(1, ninputs)
    
    def error(self, y, yp):
        return y - yp
