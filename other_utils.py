def list_of_lists_to_set_of_tuples(list_of_lists):
    return set([tuple(l) for l in list_of_lists])


def max_with_index(numbers):
    return max(numbers), numbers.index(max(numbers))
