from context import legendre_pairs
from context import sequence_generation

from legendre_pairs import *
from sequence_generation import seq_n_choose_k


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


def test_seq_filtering_by_psd():
    n = 11
    gamma = 6
    filtered_sequences = seq_filtering_by_psd(seq_n_choose_k(n, (n + 1) // 2), gamma)

    is_not_empty_iterator = False

    for seq in filtered_sequences:
        is_not_empty_iterator = True
        assert round(max(psd(seq)[1:])) <= gamma

    assert is_not_empty_iterator


def test_seq_potential_sequences_max_psd():
    n = 11
    gamma = 6

    for seq_a, (seq_b, max_psd, max_psd_idx) in zip(
        seq_filtering_by_psd(seq_n_choose_k(n, (n + 1) // 2), gamma),
        seq_potential_sequences_max_psd(n),
    ):
        assert seq_a == seq_b
