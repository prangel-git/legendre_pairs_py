from vector_utils import circular_correlation
from sequence_generation import seq_binary


def find_sequences_with_same_correlation(n):
    correlation_to_sequences = dict()
    for sequence in seq_binary(n):
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
