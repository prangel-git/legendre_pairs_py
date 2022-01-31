import pytest

from context import necklaces_generation
from necklaces_generation import *


def test_find_necklace():
    sequence = [1, 0, 0, 1]
    neckalace = [0, 0, 1, 1]
    assert find_necklace(sequence) == neckalace


def test_equal_necklaces_true():
    assert equal_necklaces([1, 0, 1, 1], [1, 1, 1, 0])


def test_equal_necklaces_false():
    assert not equal_necklaces([1, 0, 1, 1], [1, 0, 1, 0])


@pytest.mark.parametrize(
    "seq, seq_successor",
    [
        ([0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1]),
        ([0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0]),
        ([0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 1, 1]),
        ([0, 0, 0, 0, 1, 1], [0, 0, 0, 1, 0, 0]),
        ([0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 1]),
        ([0, 0, 0, 1, 0, 1], [0, 0, 0, 1, 1, 0]),
        ([0, 0, 0, 1, 1, 0], [0, 0, 0, 1, 1, 1]),
        ([0, 0, 0, 1, 1, 1], [0, 0, 1, 0, 0, 1]),
        ([1, 1, 1, 1, 1, 1], None),
    ],
)
def test_successor(seq, seq_successor):
    assert successor(seq) == seq_successor


@pytest.mark.parametrize(
    "sequence, index",
    [
        ([0, 1, 1, 0, 1], 3),
        ([0, 1, 1, 1, 1], 0),
        ([1, 1, 1, 1, 0], 4),
        ([1, 1, 1, 1, 1], None),
    ],
)
def test_find_largest_index_equal_to_zero(sequence, index):
    assert find_largest_index_equal_to_zero(sequence) == index
