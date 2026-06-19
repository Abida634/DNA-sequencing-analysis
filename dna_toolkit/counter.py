# counter.py
# This module counts how many times each nucleotide (A, T, G, C) appears.

def count_nucleotides(sequence):
    """
    Takes a DNA sequence (string) and returns a dictionary
    showing the count of each base: A, T, G, C
    """
    # Step 1: Make sure the sequence is uppercase for consistency
    sequence = sequence.upper()

    # Step 2: Create a dictionary to store counts, starting at zero
    counts = {"A": 0, "T": 0, "G": 0, "C": 0}

    # Step 3: Loop through each character in the sequence
    for base in sequence:
        # Step 4: If the character is one of A, T, G, C, increase its count by 1
        if base in counts:
            counts[base] += 1

    # Step 5: Return the final dictionary of counts
    return counts