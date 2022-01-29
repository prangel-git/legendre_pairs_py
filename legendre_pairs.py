from dft_utils import psd
from sequence_generation import (
    seq_bracelets,
    seq_binary,
    seq_n_choose_k,
)

from vector_utils import circular_correlation, pointwise_operation


def are_compatible_autocorrelation(a, b):
    correlation_a = circular_correlation(a, a)
    correlation_b = circular_correlation(b, b)
    result = pointwise_operation(lambda x, y: x + y, correlation_a, correlation_b)
    return all([result[1] == result[i] for i in range(1, len(result))])


def are_compatible_psd(a, b):
    psd_a = psd(a)
    psd_b = psd(b)
    result = pointwise_operation(lambda x, y: x + y, psd_a, psd_b)
    are_almost_equal = lambda x, y: abs(x - y) < 1e-10
    return all([are_almost_equal(result[1], result[i]) for i in range(1, len(result))])


def brute_force_search_of_compatible_autocorrelations(n):

    correlation_to_sequence = {
        tuple(circular_correlation(seq, seq)): seq
        for seq in seq_bracelets(seq_n_choose_k(n, n // 2))
    }

    compatible_sequences = []
    expected_addition = [n - 1] + [(n - 1) // 2 - 1] * (n - 1)
    for correlation in correlation_to_sequence.keys():
        expected_correlation = tuple(
            pointwise_operation(lambda x, y: x - y, expected_addition, correlation)
        )
        if expected_correlation in correlation_to_sequence.keys():
            compatible_sequence = (
                list(correlation_to_sequence[correlation]),
                list(correlation_to_sequence[expected_correlation]),
            )
            compatible_sequences.append(compatible_sequence)

    return compatible_sequences


def main():  # pragma: no cover
    print("Entry point for playing around")
    n = 21
    compatible_sequences = brute_force_search_of_compatible_autocorrelations(n)
    for a, b in compatible_sequences:
        correlation_a = circular_correlation(a, a)
        correlation_b = circular_correlation(b, b)
        correlation_sum = pointwise_operation(
            lambda x, y: x + y, correlation_a, correlation_b
        )
        print(f"sequence a {a}, sequence b {b}, correlation sum {correlation_sum}")


if __name__ == "__main__":  # pragma: no cover
    main()
