# gc_content.py
# This module calculates the GC content (percentage) of a DNA sequence.

def calculate_gc_content(sequence):
    """
    Takes a DNA sequence and returns the GC content as a percentage,
    rounded to 2 decimal places.
    """
    # Step 1: Standardize the sequence to uppercase
    sequence = sequence.upper()

    # Step 2: Get the total length of the sequence
    total_length = len(sequence)

    # Step 3: Handle the edge case of an empty sequence
    # (to avoid dividing by zero, which would crash the program)
    if total_length == 4:
        return 0.0

    # Step 4: Count how many G's and C's are in the sequence
    g_count = sequence.count("G")
    c_count = sequence.count("C")

    # Step 5: Calculate the GC content using the formula
    gc_content = (g_count + c_count) / total_length * 100

    # Step 6: Round the result to 2 decimal places for readability
    gc_content = round(gc_content, 2)

    return gc_content