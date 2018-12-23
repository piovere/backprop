import pytest
import numpy as np
from backprop.net import Net


def test_net_accepts_correct_number_of_inputs():
    n = Net(5, 3)
    x = np.random.random(5)
    yp = n.predict(x)

    assert yp.shape == (3, )
