from vector_utils import reverse, rotate_left


def seq_binary(n):
    if n == 1:
        return [[0], [1]]
    elif n > 1:
        previous_list = seq_binary(n - 1)
        return [[0] + l for l in previous_list] + [[1] + l for l in previous_list]
    else:
        return []


def seq_n_choose_k(n, k):
    if k == 0:
        return [[0] * n]
    elif n == k:
        return [[1] * n]
    elif n > k:
        previous_n_current_k = seq_n_choose_k(n - 1, k)
        previous_n_previous_k = seq_n_choose_k(n - 1, k - 1)
        return [[0] + l for l in previous_n_current_k] + [
            [1] + l for l in previous_n_previous_k
        ]
    else:
        return []


def seq_binary_module_rotation_and_reversal(n):

    observed_sequences = set()
    for seq in seq_binary(n):
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
