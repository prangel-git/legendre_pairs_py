from vector_utils import reverse, rotate_left


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


def seq_module_rotation_and_reversal(sequences):

    observed_sequences = set()
    for seq in sequences:
        if tuple(seq) not in observed_sequences:
            seen_seq = seq.copy()
            for k in range(len(seen_seq)):
                seen_seq = rotate_left(seen_seq)
                observed_sequences.add(tuple(seen_seq))
                observed_sequences.add(tuple(reverse(seen_seq)))

            yield seq

    return


def main():  # pragma: no cover
    print("Entry point for playing around")


if __name__ == "__main__":  # pragma: no cover
    main()
