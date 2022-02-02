from dft_utils import psd
from necklaces_generation import seq_necklaces_of_half_density
from sequence_generation import seq_filtering_by_psd

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

    correlation_to_sequence = dict()
    compatible_sequences = []
    expected_addition = [n - 1] + [(n - 1) // 2 - 1] * (n - 1)
    gamma = (n + 1) // 2
    for sequence in seq_filtering_by_psd(seq_necklaces_of_half_density(n), gamma):

        correlation = tuple(circular_correlation(sequence, sequence))

        if correlation in correlation_to_sequence.keys():
            continue

        correlation_to_sequence[correlation] = sequence

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
        psd_a = psd(a)
        psd_b = psd(b)
        psd_sum = pointwise_operation(lambda x, y: round(x + y), psd_a, psd_b)

        print(f"sequence a {a}, sequence b {b}, psd sum {psd_sum}")


if __name__ == "__main__":  # pragma: no cover
    main()
