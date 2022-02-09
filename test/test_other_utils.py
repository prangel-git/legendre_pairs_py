from context import other_utils
from other_utils import *


def test_list_of_lists_to_set_of_tuples():
    list_of_lists = [[1, 2, 3], [4, 5], [6]]
    set_of_tuples = set([(1, 2, 3), (4, 5), (6,)])
    assert list_of_lists_to_set_of_tuples(list_of_lists) == set_of_tuples


def test_max_with_index():
    numbers = [5, 2, 7, 1, 4, 7]
    assert max_with_index(numbers) == (7, 2)


def test_abs_square():
    a = 2 + 3j
    assert abs_square(a) == 13
