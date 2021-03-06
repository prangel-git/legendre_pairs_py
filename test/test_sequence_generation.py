from context import sequence_generation
from dft_utils import psd

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
