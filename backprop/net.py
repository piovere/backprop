from backprop.layer import Layer


class Net():
    def __init__(self, ninputs, noutputs):
        self._inputs = ninputs
        self._outputs = noutputs
