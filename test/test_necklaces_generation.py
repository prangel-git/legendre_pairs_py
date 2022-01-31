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
