from legendre_pairs import *
from sequence_generation import *
from necklaces_generation import *
from dft_utils import *
from vector_utils import *


def print_dft_matrix(n):
    x = [1] * n

    dft_matrix_5 = dft_matrix(5)

    for row in dft_matrix_5:
        print(row)


def find_bracelets_of_half_density_and_filtering(n):
    gamma = (n + 1) // 2

    bracelets = [seq for seq in seq_bracelets_of_half_density(n)]

    filtered_bracelets = [seq for seq in seq_filtering_by_psd(bracelets, gamma)]

    print(
        f"number of bracelents {len(bracelets)} vs number of filtered {len(filtered_bracelets)}"
    )


def find_legendre_pairs_by_brute_force(n):
    compatible_sequences = brute_force_search_of_compatible_autocorrelations(n)
    for a, b in compatible_sequences:
        correlation_a = circular_correlation(a, a)
        correlation_b = circular_correlation(b, b)
        correlation_sum = pointwise_operation(
            lambda x, y: x + y, correlation_a, correlation_b
        )
        psd_a = psd(a)
        psd_b = psd(b)
        psd_sum = pointwise_operation(lambda x, y: round(x + y), psd_a, psd_b)

        print(f"sequence a {a}, sequence b {b}, psd sum {psd_sum}")


def generate_necklaces_and_check_if_they_are_bracelets(n):
    sequences = [seq for seq in fkm_algorithm([0] * n, [1] * n)]
    count = 0

    for seq in sequences:
        print(
            f"seq {seq} density {sum(seq)} count {count} is bracelet {seq == find_bracelet(seq)}"
        )
        count += 1

    count = 0
    bracelet = set()
    for seq in sequences:
        seq_bracelet = tuple(find_bracelet(seq))
        if seq_bracelet not in bracelet:
            print(f"seq_bracelet {seq_bracelet} count {count}")
            count += 1
            bracelet.add(seq_bracelet)
    print(f"total necklaces {len(sequences)} total bracelets {count}")


def count_necklaces_and_charm_bracelets_with_half_density(n):
    num_necklaces = 0
    num_bracelets = 0
    num_charm_bracelets = 0

    for sequence in seq_necklaces_of_half_density(n):
        num_necklaces += 1
        if is_charm_bracelet(sequence):
            num_charm_bracelets += 1

        if find_bracelet_from_necklace(sequence) == sequence:
            num_bracelets += 1

    print(
        f"total necklaces {num_necklaces}, total bracelets {num_bracelets}, total charm bracelets {num_charm_bracelets}"
    )

    return


def generate_charm_bracelets_with_half_density(n):
    count = 1
    for seq in filter_by_charm_bracelet(seq_necklaces_of_half_density(n)):
        print(f"Charm bracelet {count}: {seq}")
        count += 1
    count_necklaces_and_charm_bracelets_with_half_density(n)


def main():
    n = 15
    generate_charm_bracelets_with_half_density(n)


if __name__ == "__main__":
    main()
