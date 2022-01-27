import pytest

from context import integer_utils
from integer_utils import *


def test_prime_generator():
    primes_smaller_than_100 = [
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
        83,
        89,
        97,
    ]
    generated_primes = []
    for prime in primes():
        if prime < 100:
            generated_primes.append(prime)
        else:
            break

    assert generated_primes == primes_smaller_than_100


def test_cycles_generator():
    numbers = [1, 2, 1]
    expected_cycle = [1, 2, 1, 1, 2, 1]
    generated_cycle = []
    for num in cycle(numbers):
        if len(generated_cycle) < 6:
            generated_cycle.append(num)
        else:
            break
    assert generated_cycle == expected_cycle


def test_gcd():
    a = 15
    b = 35
    g, x, y = gcd_extended(a, b)

    expected_gcd = 5
    expected_x = -2
    expected_y = 1

    assert expected_gcd == g
    assert expected_x == x
    assert expected_y == y


@pytest.mark.parametrize(
    "a, n, expected_answer",
    [
        (0, 21, 0),
        (1, 21, 1),
        (2, 21, -1),
        (3, 21, 0),
        (4, 21, 1),
        (5, 21, 1),
        (6, 21, 0),
        (7, 21, 0),
        (8, 21, -1),
        (9, 21, 0),
        (10, 21, -1),
        (11, 21, -1),
        (12, 21, 0),
        (13, 21, -1),
        (14, 21, 0),
        (15, 21, 0),
        (16, 21, 1),
        (17, 21, 1),
        (18, 21, 0),
        (19, 21, -1),
        (20, 21, 1),
    ],
)
def test_jacobi(a, n, expected_answer):
    answer = jacobi(a, n)
    assert answer == expected_answer


@pytest.mark.parametrize(
    "input, expected_answer", [(1, 2), (2, 6), (3, 30), (4, 210), (5, 2310)]
)
def test_primorial(input, expected_answer):
    answer = primorial(input)
    assert answer == expected_answer


@pytest.mark.parametrize(
    "input, expected_answer", [(6, [1, 5]), (30, [1, 7, 11, 13, 17, 19, 23, 29])]
)
def test_relative_primes(input, expected_answer):
    answer = relative_primes(input)
    assert answer == expected_answer


@pytest.mark.parametrize(
    "input, expected_answer", [(6, {2: 1, 3: 1}), (30, {2: 1, 3: 1, 5: 1}), (8, {2: 3})]
)
def test_prime_factorization(input, expected_answer):
    answer = prime_factorization(input)
    assert answer == expected_answer


@pytest.mark.parametrize("input, expected_answer", [(3, 2), (7, 6), (10, 4)])
def test_totient(input, expected_answer):
    answer = totient(input)
    assert answer == expected_answer
