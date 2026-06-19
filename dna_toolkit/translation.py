# translation.py
# This module translates a DNA sequence into a protein sequence
# using the standard genetic code (codon table).

# Step 1: Define the codon table as a dictionary
# Each 3-letter DNA codon maps to a 1-letter amino acid code.
# '*' represents a STOP codon.
CODON_TABLE = {
    "TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L",
    "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "ATT": "I", "ATC": "I", "ATA": "I", "ATG": "M",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "TAT": "Y", "TAC": "Y", "TAA": "*", "TAG": "*",
    "CAT": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "AAT": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "TGT": "C", "TGC": "C", "TGA": "*", "TGG": "W",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AGT": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
}


def translate_dna(sequence):
    """
    Translates a DNA sequence into a protein sequence.
    Stops translation early if a stop codon ('*') is found.
    """
    # Step 1: Standardize to uppercase
    sequence = sequence.upper()

    # Step 2: Create an empty string to build the protein sequence
    protein_sequence = ""

    # Step 3: Loop through the sequence in steps of 3 (codon by codon)
    # range(start, stop, step) generates numbers: 0, 3, 6, 9, ...
    for i in range(0, len(sequence), 3):

        # Step 4: Extract one codon (3 letters) using slicing
        codon = sequence[i:i+3]

        # Step 5: Make sure the codon is exactly 3 letters
        # (handles cases where the sequence length isn't a multiple of 3)
        if len(codon) != 3:
            break  # stop the loop, incomplete codon at the end

        # Step 6: Look up the amino acid for this codon
        amino_acid = CODON_TABLE.get(codon, "?")
        # .get() returns "?" if the codon isn't found (e.g., contains 'N')

        # Step 7: If we hit a STOP codon, stop translating
        if amino_acid == "*":
            break

        # Step 8: Add the amino acid to our protein sequence
        protein_sequence += amino_acid

    return protein_sequence