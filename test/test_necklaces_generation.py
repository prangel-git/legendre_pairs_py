import pytest

from context import necklaces_generation
from necklaces_generation import *

from equivalent_sequences import find_rotation_and_reversal_orbit


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


def test_fkm_algorithm():
    start = [0] * 6
    end = [1] * 6
    generated_necklaces = [seq for seq in fkm_algorithm(start, end)]
    necklaces = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 1],
        [0, 0, 0, 1, 0, 1],
        [0, 0, 0, 1, 1, 1],
        [0, 0, 1, 0, 0, 1],
        [0, 0, 1, 0, 1, 1],
        [0, 0, 1, 1, 0, 1],
        [0, 0, 1, 1, 1, 1],
        [0, 1, 0, 1, 0, 1],
        [0, 1, 0, 1, 1, 1],
        [0, 1, 1, 0, 1, 1],
        [0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
    ]
    assert generated_necklaces == necklaces


def test_fkm_algorithm_returns_none():
    assert [seq for seq in fkm_algorithm([0, 0, 1], [0, 0])] == []


def test_seq_necklaces_of_half_density():
    expected_necklaces = [
        [0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 1, 0, 1, 1],
        [0, 0, 0, 1, 1, 0, 1],
        [0, 0, 1, 0, 0, 1, 1],
        [0, 0, 1, 0, 1, 0, 1],
    ]

    necklaces = [seq for seq in seq_necklaces_of_half_density(7)]
    assert expected_necklaces == necklaces


def test_find_bracelet():
    expected_bracelet = [0, 0, 1, 0, 1, 1, 1]
    assert find_bracelet([1, 1, 0, 1, 0, 0, 1]) == expected_bracelet


def test_find_bracelet_from_necklace():
    expected_bracelet = [0, 0, 1, 0, 1, 1, 1]
    assert find_bracelet_from_necklace([0, 0, 1, 1, 1, 0, 1]) == expected_bracelet


def test_seq_bracelets_of_half_density():
    expected_necklaces = [
        [0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 1, 0, 1, 1],
        [0, 0, 1, 0, 0, 1, 1],
        [0, 0, 1, 0, 1, 0, 1],
    ]

    bracelets = [seq for seq in seq_bracelets_of_half_density(7)]
    assert expected_necklaces == bracelets


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
