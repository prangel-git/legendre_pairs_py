from context import equivalent_sequences
from equivalent_sequences import *


def test_find_sequences_with_same_correlation():
    n = 11
    correlation_to_sequences = find_sequences_with_same_correlation(n)

    for correlation, sequences in correlation_to_sequences.items():
        for sequence in sequences:
            assert tuple(circular_correlation(sequence, sequence)) == correlation
