# reverse_complement.py
# This module generates the reverse complement of a DNA sequence.

def get_complement(sequence):
    """
    Returns the complement of a DNA sequence (without reversing it).
    A<->T and G<->C
    """
    # Step 1: Standardize to uppercase
    sequence = sequence.upper()

    # Step 2: Create a mapping (dictionary) of each base to its complement
    complement_map = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }

    # Step 3: Build the complement string one base at a time
    complement_sequence = ""  # start with an empty string
    for base in sequence:
        complement_sequence += complement_map[base]  # add the complementary base

    return complement_sequence


def get_reverse_complement(sequence):
    """
    Returns the reverse complement of a DNA sequence.
    This is the complement, read in reverse order.
    """
    # Step 1: Get the complement first (using the function above)
    complement_sequence = get_complement(sequence)

    # Step 2: Reverse the complement sequence
    # [::-1] is Python's slicing trick to reverse a string
    reverse_complement_sequence = complement_sequence[::-1]

    return reverse_complement_sequence