from backprop.layer import Layer
import numpy as np
import pytest


# Initialize for reproduceability
np.random.seed(42)

@pytest.mark.parametrize("input", [
    (1),
    (2),
    (15)
])
def test_layer_has_correct_number_of_neurons(input):
    l = Layer(input, 4)
    assert len(l._neurons) == input

@pytest.mark.parametrize("input", [
    (1),
    (2),
    (15)
])
def test_layer_predicts_correct_number_of_outputs(input):
    l = Layer(input, 5)
    r = l.predict(np.arange(5))
    assert r.shape[0] == input
