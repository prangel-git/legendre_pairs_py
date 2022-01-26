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


def test_find_sequences_with_same_correlation():
    n = 11
    correlation_to_sequences = find_sequences_with_same_correlation(n)

    for correlation, sequences in correlation_to_sequences.items():
        for sequence in sequences:
            assert tuple(circular_correlation(sequence, sequence)) == correlation
