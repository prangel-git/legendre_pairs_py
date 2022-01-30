from context import sequence_generation
from dft_utils import psd
from equivalent_sequences import find_rotation_and_reversal_orbit

from sequence_generation import *


def test_seq_binary():
    expected = set([(0, 0), (0, 1), (1, 0), (1, 1)])
    generated = set([tuple(l) for l in seq_binary(2)])
    assert generated == expected


def test_seq_binary_invalid():
    assert [seq for seq in seq_binary(0)] == []
    assert [seq for seq in seq_binary(-1)] == []


def test_seq_n_choose_k():
    expected = set(
        [
            (1, 1, 0, 0),
            (1, 0, 1, 0),
            (1, 0, 0, 1),
            (0, 1, 1, 0),
            (0, 1, 0, 1),
            (0, 0, 1, 1),
        ]
    )
    generated = set([tuple(l) for l in seq_n_choose_k(4, 2)])
    assert generated == expected


def test_seq_n_choose_k_invalid():
    assert [seq for seq in seq_n_choose_k(5, 6)] == []


def test_seq_module_rotations_and_reversal():
    n = 11
    sequences = [tuple(seq) for seq in seq_bracelets(seq_binary(n))]
    seq_to_orbit = {
        seq: find_rotation_and_reversal_orbit(list(seq)) for seq in sequences
    }

    for seq_a in sequences:
        for seq_b in sequences:
            if seq_a != seq_b:
                assert seq_to_orbit[seq_a] != seq_to_orbit[seq_b]


def test_seq_filtering_by_psd():
    n = 11
    gamma = 6
    filtered_sequences = seq_filtering_by_psd(
        seq_bracelets(seq_n_choose_k(n, (n + 1) // 2)), gamma
    )

    is_not_empty_iterator = False

    for seq in filtered_sequences:
        is_not_empty_iterator = True
        assert round(max(psd(seq)[1:])) <= gamma

    assert is_not_empty_iterator
