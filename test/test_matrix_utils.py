from context import matrix_utils


from matrix_utils import *


def test_transpose():
    matrix = [[1, 2], [3, 4]]
    matrix_t = [[1, 3], [2, 4]]
    assert matrix_t == transpose(matrix)


def test_matrix_mul():
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]
    a_times_b = [[19, 43], [22, 50]]
    assert a_times_b == matrix_mul(a, b)


def test_matrix_times_vector():
    a = [[1, 2], [3, 4]]
    x = [5, 6]
    a_times_x = [17, 39]
    assert a_times_x == matrix_times_vector(a, x)
