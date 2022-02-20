from dft_utils import psd, psd_k, dft_matrix
from integer_utils import relative_primes
from necklaces_generation import seq_necklaces_of_half_density, filter_by_charm_bracelet
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


def seq_potential_necklace_max_psd(n):
    eps = 1e-2

    dft_matrix_n = dft_matrix(n)

    gamma = (n + 1) // 2
    offset = (n + 1) / 4
    for seq in seq_necklaces_of_half_density(n):
        is_psd_bounded_by_gamma = True
        max_offset_psd = 0
        max_idx = 0
        for idx in relative_primes(len(seq)):
            current_psd = abs_square(dot(dft_matrix_n[idx], seq))
            if current_psd - eps > gamma:
                is_psd_bounded_by_gamma = False
                break

            current_psd_offset = current_psd - offset
            if abs(current_psd_offset) > max_offset_psd:
                max_offset_psd = current_psd_offset
                max_idx = idx

        if is_psd_bounded_by_gamma:
            decimated_seq = [seq[(k * max_idx) % len(seq)] for k in range(len(seq))]

            yield (decimated_seq, max_offset_psd)


def find_potential_legendre_pairs_by_offset(n):
    eps = 1e-2
    observed_triples = []
    for new_seq, new_max in seq_potential_necklace_max_psd(n):
        observed_triples.append((new_seq, new_max))
        for obs_seq, obs_max in observed_triples:
            if abs(obs_max + new_max) < eps:
                yield new_seq


def brute_force_by_offset(n):
    correlation_to_sequence = dict()
    compatible_sequences = []
    expected_addition = [n - 1] + [(n - 1) // 2 - 1] * (n - 1)
    gamma = (n + 1) // 2
    for sequence in find_potential_legendre_pairs_by_offset(n):

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
            yield compatible_sequence


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
            yield compatible_sequence


def main():  # pragma: no cover
    print("Entry point for playing around")
    n = 23

    is_offset = False

    generator = (
        brute_force_by_offset(n)
        if is_offset
        else brute_force_search_of_compatible_autocorrelations(n)
    )

    count = 0
    for seq_a, seq_b in generator:
        # print(f"legendre pairs {count}: {seq_a}, {seq_b}")
        count += 1

    print("is offset", is_offset)
    print(f"number of pairs found {count}")


if __name__ == "__main__":  # pragma: no cover
    main()
