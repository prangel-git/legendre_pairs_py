def list_of_lists_to_set_of_tuples(list_of_lists):
    return set([tuple(l) for l in list_of_lists])
