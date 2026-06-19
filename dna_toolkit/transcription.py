# transcription.py
# This module converts a DNA sequence into its corresponding RNA sequence.

def dna_to_rna(sequence):
    """
    Converts a DNA sequence to RNA by replacing every 'T' with 'U'.
    """
    # Step 1: Standardize to uppercase
    sequence = sequence.upper()

    # Step 2: Replace all occurrences of 'T' with 'U'
    rna_sequence = sequence.replace("T", "U")

    return rna_sequence