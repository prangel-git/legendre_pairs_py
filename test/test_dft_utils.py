from context import dft_utils

from vector_utils import circular_correlation, distance_l2

from dft_utils import *

eps = 1e-10


def test_roots_of_unity_k_n():
    answer = roots_of_unity_k_n(1, 2)
    expected = [1, -1]
    assert distance_l2(answer, expected) < eps


def test_dft_k():
    num_elements = 10
    answer = dft_k([1] * num_elements, 0)
    assert num_elements == answer


def test_dft():
    x = [1, 1, 1]
    manual_dft_x = [dft_k(x, k) for k in range(len(x))]
    dft_x = dft(x)
    assert distance_l2(dft_x, manual_dft_x) < eps


def test_psd():
    x = [1, 1, 1]
    manual_psd_x = [psd_k(x, k) for k in range(len(x))]
    psd_x = psd(x)
    assert distance_l2(psd_x, manual_psd_x) < eps


def test_psd_is_dft_of_autocorrelation():
    x = [1, 1, 1]
    dft_autocorrelation_x = dft(circular_correlation(x, x))
    psd_x = psd(x)
    assert distance_l2(psd_x, dft_autocorrelation_x) < eps
