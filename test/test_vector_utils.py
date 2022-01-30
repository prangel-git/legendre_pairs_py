from context import vector_utils

from vector_utils import *


def test_dot():
    assert dot([1, 2, 3], [4, 5, 6]) == 32


def test_rotate_right():
    assert rotate_left([1, 2, 3]) == [2, 3, 1]


def test_rotate_left():
    assert rotate_right([1, 2, 3]) == [3, 1, 2]


def test_rotate_n():
    assert rotate_n([1, 2, 3, 4], 1) == [2, 3, 4, 1]
    assert rotate_n([1, 2, 3, 4], 2) == [3, 4, 1, 2]
    assert rotate_n([1, 2, 3, 4], -1) == [4, 1, 2, 3]


def test_reverse():
    assert reverse([1, 2, 3]) == [3, 2, 1]


def test_pad_right():
    assert pad_right([1, 2, 3], 4) == [1, 2, 3, 0, 0, 0, 0]


def test_pad_left():
    assert pad_left([1, 2, 3], 4) == [0, 0, 0, 0, 1, 2, 3]


def test_pointwise_operation():
    assert pointwise_operation(lambda x, y: x + y, [1, 2, 3], [4, 5, 6]) == [5, 7, 9]


def test_convolution():
    assert convolution([1, 2, 3], [4, 5, 6]) == [4, 13, 28, 27, 18]


def test_correlation():
    assert correlation([1, 2, 3], [4, 5, 6]) == [6, 17, 32, 23, 12]


def test_circular_convolution():
    assert circular_convolution([1, 2, 3], [4, 5, 6]) == [28, 31, 31]


def test_circular_correlation():
    assert circular_correlation([1, 2, 3], [4, 5, 6]) == [32, 29, 29]


def test_distance_l2():
    assert distance_l2([1, 1], [2, 2]) == 2
