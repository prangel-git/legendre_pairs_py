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

    number_of_repetitions = len_sequence // (largest_index_equal_to_zero + 1)
    length_last_part = len_sequence % (largest_index_equal_to_zero + 1)

    return (
        sequence[:largest_index_equal_to_zero] + [1]
    ) * number_of_repetitions + sequence[:length_last_part]


def find_largest_index_equal_to_zero(sequence):
    for k in range(len(sequence) - 1, -1, -1):
        if sequence[k] == 0:
            return k

    return None


def main():  # pragma: no cover
    print("Entry point for playing around")


if __name__ == "__main__":  # pragma: no cover
    main()
