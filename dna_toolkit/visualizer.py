# visualizer.py
# This module creates a bar chart showing nucleotide frequencies.

import matplotlib.pyplot as plt
# We import matplotlib's "pyplot" module and nickname it "plt"
# (this is the standard convention used by almost everyone)


def plot_nucleotide_frequencies(frequencies, save_path=None):
    """
    Creates a bar chart of nucleotide frequencies (A, T, G, C).
    If save_path is provided, saves the chart as an image file.
    Otherwise, displays the chart on screen.
    """
    # Step 1: Extract the base names (A, T, G, C) and their values
    bases = list(frequencies.keys())      # e.g., ["A", "T", "G", "C"]
    values = list(frequencies.values())   # e.g., [25.0, 25.0, 25.0, 25.0]

    # Step 2: Define a color for each bar (purely visual choice)
    colors = ["#4CAF50", "#F44336", "#2196F3", "#FF9800"]
    # Green for A, Red for T, Blue for G, Orange for C

    # Step 3: Create the bar chart
    plt.figure(figsize=(6, 4))  # sets the size of the chart (width, height in inches)
    plt.bar(bases, values, color=colors)

    # Step 4: Add labels and a title for clarity
    plt.title("Nucleotide Frequency (%)")
    plt.xlabel("Nucleotide Base")
    plt.ylabel("Frequency (%)")

    # Step 5: Add the percentage value on top of each bar
    for i, value in enumerate(values):
        plt.text(i, value + 1, f"{value}%", ha="center")

    # Step 6: Either save the chart to a file, or show it on screen
    if save_path:
        plt.savefig(save_path)  # saves the chart as an image (e.g., PNG)
        print(f"Chart saved to: {save_path}")
    else:
        plt.show()  # opens a window displaying the chart

    # Step 7: Close the figure to free up memory (good practice)
    plt.close()