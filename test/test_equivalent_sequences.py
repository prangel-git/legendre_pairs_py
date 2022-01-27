from context import equivalent_sequences
from equivalent_sequences import *


def test_find_sequences_with_same_correlation():
    n = 11
    correlation_to_sequences = find_sequences_with_same_correlation(n)

    for correlation, sequences in correlation_to_sequences.items():
        for sequence in sequences:
            assert tuple(circular_correlation(sequence, sequence)) == correlation


def test_find_rotation_and_reversal_orbit():
    sequence = [1, 2, 3]
    orbit_of_sequence = set(
        [(1, 2, 3), (3, 1, 2), (2, 3, 1), (3, 2, 1), (1, 3, 2), (2, 1, 3)]
    )
    assert find_rotation_and_reversal_orbit(sequence) == orbit_of_sequence
