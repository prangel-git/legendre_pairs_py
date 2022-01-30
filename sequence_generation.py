from vector_utils import reverse, rotate_right
from dft_utils import psd_k, psd


def seq_binary(n):
    if n == 1:
        yield [0]
        yield [1]
    elif n > 1:
        for l in seq_binary(n - 1):
            yield [0] + l
            yield [1] + l

    return


def seq_n_choose_k(n, k):
    if k == 0:
        yield [0] * n
    elif n == k:
        yield [1] * n
    elif n > k:
        for previous_n_current_k in seq_n_choose_k(n - 1, k):
            yield [0] + previous_n_current_k

        for previous_n_previous_k in seq_n_choose_k(n - 1, k - 1):
            yield [1] + previous_n_previous_k

    return


def seq_bracelets(sequences):

    observed_sequences = set()
    for seq in sequences:
        if tuple(seq) not in observed_sequences:
            seen_seq = seq.copy()
            for k in range(len(seen_seq)):
                seen_seq = rotate_right(seen_seq)
                observed_sequences.add(tuple(seen_seq))
                observed_sequences.add(tuple(reverse(seen_seq)))

            yield seq

    return


def seq_filtering_by_psd(sequences, gamma):
    eps = 1e-10
    # filter(lambda x: all([psd_k(x, k) - eps > gamma for k in range(1, len(x))]), sequences)
    for seq in sequences:
        is_psd_bounded_by_gamma = True
        for k in range(1, len(seq)):
            if psd_k(seq, k) - eps > gamma:
                is_psd_bounded_by_gamma = False
                break
        if is_psd_bounded_by_gamma:
            yield seq

    return


def main():  # pragma: no cover
    print("Entry point for playing around")


if __name__ == "__main__":  # pragma: no cover
    main()
