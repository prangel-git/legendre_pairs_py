from sequence_generation import seq_filtering_by_psd
from necklaces_generation import seq_bracelets_of_half_density


def main():
    n = 27
    gamma = (n + 1) // 2

    bracelets_len = 0
    for _ in seq_bracelets_of_half_density(n):
        bracelets_len += 1

    filtered_bracelets_len = 0
    for _ in seq_filtering_by_psd(seq_bracelets_of_half_density(n), gamma):
        filtered_bracelets_len += 1

    print(
        f"number of bracelents {bracelets_len} vs number of filtered {filtered_bracelets_len}"
    )


if __name__ == "__main__":
    main()
