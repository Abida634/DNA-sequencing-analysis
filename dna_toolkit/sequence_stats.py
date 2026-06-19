# sequence_stats.py
# This module calculates sequence length and nucleotide frequency percentages.

from dna_toolkit.counter import count_nucleotides
# We import the function we built in Module 2 so we can reuse it here


def get_sequence_length(sequence):
    """
    Returns the total number of bases in the sequence.
    """
    sequence = sequence.upper()
    return len(sequence)


def get_nucleotide_frequencies(sequence):
    """
    Returns a dictionary showing the percentage frequency
    of each base (A, T, G, C) in the sequence.
    """
    # Step 1: Standardize to uppercase
    sequence = sequence.upper()

    # Step 2: Get the total length
    total_length = len(sequence)

    # Step 3: Handle empty sequence to avoid division by zero
    if total_length == 0:
        return {"A": 0.0, "T": 0.0, "G": 0.0, "C": 0.0}

    # Step 4: Reuse our counter function from Module 2
    counts = count_nucleotides(sequence)

    # Step 5: Create a new dictionary to hold frequencies (percentages)
    frequencies = {}

    # Step 6: Loop through each base and its count, converting to percentage
    for base, count in counts.items():
        frequencies[base] = round((count / total_length) * 100, 2)

    return frequencies