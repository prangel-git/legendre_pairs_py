from context import necklaces_generation
from necklaces_generation import *


def test_find_necklace():
    sequence = [1, 0, 0, 1]
    neckalace = [0, 0, 1, 1]
    assert find_necklace(sequence) == neckalace
