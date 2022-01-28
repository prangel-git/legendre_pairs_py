from context import legendre_pairs

from legendre_pairs import *


def test_are_compatible_autocorrelation():
    a = [1, 1, 1, -1, 1, -1, -1]
    b = [1, -1, -1, 1, -1, 1, 1]
    assert are_compatible_autocorrelation(a, b)


def test_not_are_compatible_autocorrelation():
    a = [1, 1, 1, -1, 1, -1, -1]
    b = [-1, 1, -1, 1, -1, 1, 1]
    assert not are_compatible_autocorrelation(a, b)


def test_are_compatible_psd():
    a = [1, 1, 1, 0, 1, 0, 0]
    b = [1, 0, 0, 1, 0, 1, 1]
    assert are_compatible_psd(a, b)


def test_not_are_compatible_psd():
    a = [1, 1, 1, -1, 1, -1, -1]
    b = [0, 1, 0, 1, 0, 1, 1]
    assert not are_compatible_psd(a, b)


def test_brute_force_search_of_compatible_autocorrelations():
    n = 11
    compatible_autocorrelation = brute_force_search_of_compatible_autocorrelations(n)
    assert compatible_autocorrelation

    for seq_a, seq_b in compatible_autocorrelation:
        assert are_compatible_psd(seq_a, seq_b)
