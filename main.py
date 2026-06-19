# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# main.py
# This is the main program - the entry point for the DNA Sequence Analysis Toolkit.

from dna_toolkit.validator import is_valid_dna, clean_sequence
from dna_toolkit.counter import count_nucleotides
from dna_toolkit.gc_content import calculate_gc_content
from dna_toolkit.reverse_complement import get_reverse_complement
from dna_toolkit.transcription import dna_to_rna
from dna_toolkit.translation import translate_dna
from dna_toolkit.sequence_stats import get_sequence_length, get_nucleotide_frequencies
from dna_toolkit.visualizer import plot_nucleotide_frequencies
from dna_toolkit.file_handler import save_results_to_file, read_fasta_file
from dna_toolkit.report import generate_report


def get_sequence_from_user():
    """
    Asks the user how they want to provide a DNA sequence:
    either by typing it directly, or by loading a FASTA file.
    """
    print("\nHow would you like to provide the DNA sequence?")
    print("1. Type/paste the sequence directly")
    print("2. Load from a FASTA file")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        sequence = input("Enter your DNA sequence: ")
        return clean_sequence(sequence)

    elif choice == "2":
        file_path = input("Enter the path to your FASTA file (e.g., data/sample.fasta): ")
        try:
            sequence = read_fasta_file(file_path)
            return clean_sequence(sequence)
        except FileNotFoundError:
            print(f"ERROR: File not found at '{file_path}'. Please check the path.")
            return None

    else:
        print("Invalid choice. Please enter 1 or 2.")
        return None


def show_menu():
    """
    Displays the main menu of available analyses.
    """
    print("\n========== DNA SEQUENCE ANALYSIS TOOLKIT ==========")
    print("1. Validate Sequence")
    print("2. Count Nucleotides")
    print("3. Calculate GC Content")
    print("4. Generate Reverse Complement")
    print("5. Convert DNA to RNA")
    print("6. Translate DNA to Protein")
    print("7. Show Sequence Length")
    print("8. Show Nucleotide Frequencies")
    print("9. Display Frequency Graph")
    print("10. Generate Full Report (and save to file)")
    print("0. Exit")
    print("=====================================================")


def main():
    """
    The main program loop. Keeps showing the menu until the user exits.
    """
    print("Welcome to the DNA Sequence Analysis Toolkit!")

    # Step 1: Get the sequence from the user (once, at the start)
    sequence = get_sequence_from_user()

    # Step 2: If something went wrong getting the sequence, stop the program
    if sequence is None:
        print("Could not get a valid sequence. Exiting program.")
        return  # exits the main() function immediately

    # Step 3: Validate the sequence before doing anything else
    if not is_valid_dna(sequence):
        print("ERROR: This is not a valid DNA sequence (only A, T, G, C allowed).")
        return

    print(f"\nSequence loaded successfully! Length: {len(sequence)} bases.")

    # Step 4: Loop forever, showing the menu, until user chooses to exit
    while True:
        show_menu()
        choice = input("Enter your choice (0-10): ")

        if choice == "1":
            print("\nThis sequence is VALID DNA (contains only A, T, G, C).")

        elif choice == "2":
            counts = count_nucleotides(sequence)
            print(f"\nNucleotide Counts: {counts}")

        elif choice == "3":
            gc = calculate_gc_content(sequence)
            print(f"\nGC Content: {gc}%")

        elif choice == "4":
            rev_comp = get_reverse_complement(sequence)
            print(f"\nReverse Complement:\n{rev_comp}")

        elif choice == "5":
            rna = dna_to_rna(sequence)
            print(f"\nRNA Sequence:\n{rna}")

        elif choice == "6":
            protein = translate_dna(sequence)
            print(f"\nProtein Sequence:\n{protein}")

        elif choice == "7":
            length = get_sequence_length(sequence)
            print(f"\nSequence Length: {length} bases")

        elif choice == "8":
            freqs = get_nucleotide_frequencies(sequence)
            print(f"\nNucleotide Frequencies: {freqs}")

        elif choice == "9":
            freqs = get_nucleotide_frequencies(sequence)
            save_choice = input("Save chart to file? (y/n): ")
            if save_choice.lower() == "y":
                plot_nucleotide_frequencies(freqs, save_path="output/frequency_chart.png")
            else:
                plot_nucleotide_frequencies(freqs)

        elif choice == "10":
            name = input("Enter a name for this sequence (or press Enter to skip): ")
            if name.strip() == "":
                name = "Unnamed Sequence"
            report = generate_report(sequence, sequence_name=name)
            print(report)
            save_results_to_file(report, "output/analysis_report.txt")

        elif choice == "0":
            print("\nThank you for using the DNA Sequence Analysis Toolkit. Goodbye!")
            break  # exits the while loop, ending the program

        else:
            print("\nInvalid choice. Please enter a number between 0 and 10.")


# Step 5: This special block ensures main() only runs when this file
# is run directly (not when imported by another file)
if __name__ == "__main__":
    main()
