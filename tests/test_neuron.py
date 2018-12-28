import pytest
from backprop.neuron import Neuron
import numpy as np


@pytest.mark.parametrize("input",[
    (1),
    (2),
    (15)
])
def test_neuron_accepts_correct_number_of_inputs(input):
    n = Neuron(input)
    x = np.random.random(input)
    yp = n.predict(x)

    assert yp.shape == ()
    assert type(yp) == type(np.sqrt(0.5))


@pytest.mark.parametrize("test_inp,out",[
    (np.ones(4), 5.0),
    (np.zeros(4), 1.0),
])
def test_neuron_multiplication(test_inp, out):
    n = Neuron(4)
    n._weights = np.ones(4)

    assert n.predict(test_inp) == out


def test_neuron_can_calculate_error():
    n = Neuron(5)
    n._weights = np.ones(5)
    n._bias = 1.0

    x = np.ones(5)
    y = 6.0
    
    assert n.error(x, y) == 0.0
