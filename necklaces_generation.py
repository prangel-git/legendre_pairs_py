from vector_utils import rotate_n


def find_necklace(sequence):
    potential_necklace = sequence.copy()
    for k in range(len(sequence)):
        rotated_sequence = rotate_n(sequence, k)
        if potential_necklace > rotated_sequence:
            potential_necklace = rotated_sequence
    return potential_necklace
