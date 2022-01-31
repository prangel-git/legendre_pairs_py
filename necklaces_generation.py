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
    t = len_sequence // (largest_index_equal_to_zero + 1)
    j = len_sequence % (largest_index_equal_to_zero + 1)

    return repeat_tth_times_and_fill_jth_values(mod_sequence, t, j)


def fkm_algorithm(start, end):

    if len(start) != len(end):
        return

    l = len(start)

    start_necklace = find_necklace(start)
    end_necklace = find_necklace(end)

    current = min(start_necklace, end_necklace)
    real_end = max(start_necklace, end_necklace)

    yield current

    while current < real_end:
        i = find_largest_index_equal_to_zero(current) + 1
        t = l // i
        j = l % i

        mod_current = current[: i - 1] + [1]
        current = repeat_tth_times_and_fill_jth_values(mod_current, t, j)
        if j == 0:
            yield current


def find_largest_index_equal_to_zero(sequence):
    for k in range(len(sequence) - 1, -1, -1):
        if sequence[k] == 0:
            return k

    return None


def repeat_tth_times_and_fill_jth_values(sequence, t, j):
    return sequence * t + sequence[:j]


def main():  # pragma: no cover
    print("Entry point for playing around")
    sequences = [seq for seq in fkm_algorithm([0] * 6, [1] * 6)]
    for seq in sequences:
        print(seq)


if __name__ == "__main__":  # pragma: no cover
    main()