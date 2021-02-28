from backprop.layer import Layer, OutputLayer
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

def test_output_layer_has_error():
    ol = OutputLayer(5)
    ol._neurons[0]._weights = np.zeros(5)
    assert ol.error(1, 1) == 0
