# file_handler.py
# This module handles saving results to files and reading DNA from FASTA files.

import os
# 'os' is a built-in Python library for interacting with the file system
# (e.g., creating folders, checking if files exist)


def save_results_to_file(results_text, output_path):
    """
    Saves a block of text (our analysis results) to a file.
    Creates the output folder if it doesn't already exist.
    """
    # Step 1: Get the folder portion of the output path
    folder = os.path.dirname(output_path)

    # Step 2: If the folder doesn't exist, create it
    if folder and not os.path.exists(folder):
        os.makedirs(folder)

    # Step 3: Open the file in "write" mode and save the text
    with open(output_path, "w") as file:
        file.write(results_text)

    print(f"Results saved to: {output_path}")


def read_fasta_file(file_path):
    """
    Reads a FASTA file and returns the DNA sequence as a single string,
    with all line breaks removed (joins multi-line sequences into one).
    """
    sequence_lines = []  # will hold each line of the sequence (excluding the header)

    # Step 1: Open the file in "read" mode
    with open(file_path, "r") as file:
        # Step 2: Loop through each line in the file
        for line in file:
            line = line.strip()  # remove newline characters and extra spaces

            # Step 3: Skip the header line (starts with '>')
            if line.startswith(">"):
                continue  # skip to the next line, don't add this to our sequence

            # Step 4: Add the sequence line to our list
            sequence_lines.append(line)

    # Step 5: Join all the lines together into one continuous sequence
    full_sequence = "".join(sequence_lines)

    return full_sequence