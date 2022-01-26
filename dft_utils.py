from __future__ import annotations

from cmath import exp, pi

from vector_utils import dot
from matrix_utils import matrix_times_vector


def roots_of_unity_k_n(k: complex, n: complex) -> list(complex):
    return [exp(2j * pi * k * m / n) for m in range(n)]


def dft_k(x, k):
    return dot(x, roots_of_unity_k_n(k, len(x)))


def psd_k(x, k):
    x_hat_k = dft_k(x, k)
    return x_hat_k.conjugate() * x_hat_k


def dft_matrix(n):
    w_n = roots_of_unity_k_n(1, n)
    return [[w_n[(j * k) % n] for j in range(n)] for k in range(n)]


def dft(x):
    transform_matrix = dft_matrix(len(x))
    return matrix_times_vector(transform_matrix, x)


def psd(x):
    x_hat = dft(x)
    return [
        x_hat_i.real * x_hat_i.real + x_hat_i.imag * x_hat_i.imag for x_hat_i in x_hat
    ]


def main():
    x = [1] * 5

    dft_matrix_5 = dft_matrix(5)

    for row in dft_matrix_5:
        print(row)


if __name__ == "__main__":
    main()
