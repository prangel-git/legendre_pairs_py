from dft_utils import psd

from vector_utils import circular_correlation, correlation, pointwise_operation
from sequence_generation import seq_binary, seq_n_choose_k


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


def find_sequences_with_same_correlation(n):
    correlation_to_sequences = dict()
    for sequence in seq_n_choose_k(n, n // 2):
        correlation_a = tuple(circular_correlation(sequence, sequence))
        if correlation_a not in correlation_to_sequences.keys():
            correlation_to_sequences[correlation_a] = [sequence]
        else:
            correlation_to_sequences[correlation_a] = correlation_to_sequences[
                correlation_a
            ] + [sequence]
    return correlation_to_sequences


def main():
    corr_to_seqs = find_sequences_with_same_correlation(11)

    total_sequences = 0
    for corr in corr_to_seqs.keys():
        num_sequences = len(corr_to_seqs[corr])
        total_sequences += num_sequences
        print(f"sequence {corr} equivalences {num_sequences}")
        """
        for seq in corr_to_seqs[corr]:
            print(seq)
            """

    print(f"Total equivalence classes {len(corr_to_seqs)}")
    print(f"Total sequences {total_sequences}")


if __name__ == "__main__":
    main()
