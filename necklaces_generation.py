from vector_utils import rotate_n


def find_necklace(sequence):
    potential_necklace = sequence.copy()
    for k in range(len(sequence)):
        rotated_sequence = rotate_n(sequence, k)
        if potential_necklace > rotated_sequence:
            potential_necklace = rotated_sequence
    return potential_necklace


def equal_necklaces(sequence_a, sequence_b):
    return find_necklace(sequence_a) == find_necklace(sequence_b)


def successor(sequence):
    len_sequence = len(sequence)
    largest_index_equal_to_zero = find_largest_index_equal_to_zero(sequence)

    if largest_index_equal_to_zero is None:
        return None

    mod_sequence = sequence[:largest_index_equal_to_zero] + [1]
    i = len_sequence // (largest_index_equal_to_zero + 1)
    j = len_sequence % (largest_index_equal_to_zero + 1)

    return repeat_ith_times_and_fill_jth_values(mod_sequence, i, j)


def find_largest_index_equal_to_zero(sequence):
    for k in range(len(sequence) - 1, -1, -1):
        if sequence[k] == 0:
            return k

    return None


def repeat_ith_times_and_fill_jth_values(sequence, k, j):
    return sequence * k + sequence[:j]


def main():  # pragma: no cover
    print("Entry point for playing around")
    sequence = [0] * 6
    while sequence is not None:
        print(sequence)
        sequence = successor(sequence)
    print(sequence)


if __name__ == "__main__":  # pragma: no cover
    main()
