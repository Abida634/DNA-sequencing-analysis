# validator.py
# This module checks whether a given sequence is a valid DNA sequence.

def is_valid_dna(sequence):
    """
    Check if the sequence contains only valid DNA bases: A, T, G, C
    Returns True if valid, False otherwise.
    """
    # Step 1: Convert the sequence to uppercase
    # This makes sure 'a', 'A' are treated the same way
    sequence = sequence.upper()

    # Step 2: Define the set of allowed characters
    valid_bases = {"A", "T", "G", "C"}

    # Step 3: Check every character in the sequence
    for base in sequence:
        if base not in valid_bases:
            return False  # Found an invalid character

    # Step 4: If we reach here, all characters were valid
    return True


def clean_sequence(sequence):
    """
    Removes whitespace and newlines, and converts to uppercase.
    Useful for cleaning sequences pasted by the user or read from files.
    """
    sequence = sequence.strip()        # remove leading/trailing spaces
    sequence = sequence.replace("\n", "")  # remove newlines
    sequence = sequence.replace(" ", "")   # remove internal spaces
    sequence = sequence.upper()        # convert to uppercase
    return sequence