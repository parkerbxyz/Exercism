"""Calculate the Hamming Distance between two DNA strands."""


def distance(strand_a: str, strand_b: str) -> int:
    """Return the Hamming distance between two equal-length sequences."""
    if not len(strand_a) == len(strand_b):
        raise ValueError("Sequences must be of equal length.")
    return sum([s1 != s2 for s1, s2 in zip(strand_a, strand_b)])
