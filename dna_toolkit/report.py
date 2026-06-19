# report.py
# This module combines results from all other modules into one
# complete, formatted analysis report.

from dna_toolkit.validator import is_valid_dna, clean_sequence
from dna_toolkit.counter import count_nucleotides
from dna_toolkit.gc_content import calculate_gc_content
from dna_toolkit.reverse_complement import get_reverse_complement
from dna_toolkit.transcription import dna_to_rna
from dna_toolkit.translation import translate_dna
from dna_toolkit.sequence_stats import get_sequence_length, get_nucleotide_frequencies


def generate_report(sequence, sequence_name="Unnamed Sequence"):
    """
    Runs a full analysis on the given DNA sequence and returns
    a formatted text report (as a string).
    """
    # Step 1: Clean the input sequence first
    sequence = clean_sequence(sequence)

    # Step 2: Validate it - if invalid, return an error report immediately
    if not is_valid_dna(sequence):
        return (
            f"ERROR: The provided sequence for '{sequence_name}' is not a valid "
            f"DNA sequence. It must contain only A, T, G, and C."
        )

    # Step 3: Run every analysis module on the cleaned sequence
    length = get_sequence_length(sequence)
    counts = count_nucleotides(sequence)
    gc_content = calculate_gc_content(sequence)
    frequencies = get_nucleotide_frequencies(sequence)
    reverse_comp = get_reverse_complement(sequence)
    rna_sequence = dna_to_rna(sequence)
    protein_sequence = translate_dna(sequence)

    # Step 4: Build the report using an f-string (multi-line)
    report = f"""
=========================================
   DNA SEQUENCE ANALYSIS REPORT
=========================================
Sequence Name : {sequence_name}

--- ORIGINAL SEQUENCE ---
{sequence}

--- BASIC STATISTICS ---
Sequence Length : {length} bases
Nucleotide Counts:
    A: {counts['A']}
    T: {counts['T']}
    G: {counts['G']}
    C: {counts['C']}

Nucleotide Frequencies (%):
    A: {frequencies['A']}%
    T: {frequencies['T']}%
    G: {frequencies['G']}%
    C: {frequencies['C']}%

GC Content : {gc_content}%

--- SEQUENCE TRANSFORMATIONS ---
Reverse Complement:
{reverse_comp}

RNA Sequence (Transcription):
{rna_sequence}

Protein Sequence (Translation):
{protein_sequence}

=========================================
   END OF REPORT
=========================================
"""

    return report