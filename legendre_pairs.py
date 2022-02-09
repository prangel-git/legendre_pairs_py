from dft_utils import psd, psd_k, dft_matrix
from necklaces_generation import seq_necklaces_of_half_density
from other_utils import abs_square
from sequence_generation import seq_n_choose_k

from vector_utils import circular_correlation, pointwise_operation, dot


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


def seq_filtering_by_psd(sequences, gamma):
    eps = 1e-10

    for seq in sequences:
        is_psd_bounded_by_gamma = True
        for k in range(1, len(seq)):
            if psd_k(seq, k) - eps > gamma:
                is_psd_bounded_by_gamma = False
                break
        if is_psd_bounded_by_gamma:
            yield seq

    return


def seq_potential_sequences_max_psd(n):
    eps = 1e-10

    dft_matrix_n = dft_matrix(n)

    density = n // 2
    gamma = (n + 1) // 2
    offset = (n + 1) / 4
    for seq in seq_n_choose_k(n, density):
        is_psd_bounded_by_gamma = True
        max_offset_psd = 0
        max_idx = 0
        for idx in range(1, len(seq)):
            current_psd = abs_square(dot(dft_matrix_n[idx], seq))
            if current_psd - eps > gamma:
                is_psd_bounded_by_gamma = False
                break

            current_psd_offset = current_psd - offset
            if abs(current_psd_offset) > max_offset_psd:
                max_offset_psd = current_psd_offset
                max_idx = idx

        if is_psd_bounded_by_gamma:
            yield (seq, max_offset_psd, max_idx)


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


if __name__ == "__main__":  # pragma: no cover
    main()
