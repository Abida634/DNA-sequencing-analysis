# 🧬 DNA Sequence Analysis Toolkit

A beginner-friendly, command-line bioinformatics tool built in Python for analyzing DNA sequences. This project demonstrates core concepts in molecular biology (GC content, transcription, translation, reverse complement) combined with practical Python programming skills (file handling, data visualization, modular design).

---

## 📋 Features

- ✅ DNA sequence validation
- 🔢 Nucleotide counting (A, T, G, C)
- 📊 GC content calculation
- 🔄 Reverse complement generation
- 🧪 DNA → RNA conversion (transcription)
- 🧬 DNA → Protein translation (using the standard genetic code)
- 📏 Sequence length calculation
- 📈 Nucleotide frequency analysis and bar chart visualization
- 📁 FASTA file reading
- 💾 Save results and full reports to text files

---

## 🛠️ Technologies Used

- **Python 3.8+**
- **Matplotlib** — for data visualization

---

## 📂 Project Structure
dna-toolkit/

│

├── dna_toolkit/              # Core package with all analysis modules

│   ├── init.py

│   ├── validator.py           # Sequence validation & cleaning

│   ├── counter.py             # Nucleotide counting

│   ├── gc_content.py          # GC content calculation

│   ├── reverse_complement.py  # Reverse complement generation

│   ├── transcription.py       # DNA to RNA conversion

│   ├── translation.py         # DNA to Protein translation

│   ├── sequence_stats.py       # Length & frequency calculations

│   ├── visualizer.py           # Matplotlib chart generation

│   ├── file_handler.py         # File save/read (incl. FASTA)

│   └── report.py               # Full analysis report generator

│

├── data/

│   └── sample.fasta           # Sample DNA sequence (Beta-Globin fragment)

│

├── output/                    # Generated reports & charts saved here

│   └── .gitkeep

│

├── main.py                    # Run this file to start the program

├── README.md

├── requirements.txt

└── .gitignore

---

## ⚙️ Installation

1. **Clone this repository:**
```bash
   git clone https://github.com/YOUR_USERNAME/dna-toolkit.git
   cd dna-toolkit
```

2. **(Recommended) Create a virtual environment:**
```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
```

3. **Install dependencies:**
```bash
   pip install -r requirements.txt
```

---

## ▶️ How to Run

```bash
python main.py
```

You'll be presented with a menu:
1. Choose to type a sequence manually or load from `data/sample.fasta`
2. Once validated, choose from analysis options (counts, GC content, reverse complement, RNA, protein translation, charts, or a full report)
3. Reports and charts are saved automatically to the `output/` folder

---

## 🧪 Example Usage
Enter your DNA sequence: ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG
Sequence accepted! Length: 40 bases
What would you like to do?

Show nucleotide counts
Calculate GC content
Get reverse complement
Convert to RNA
Translate to protein
Show nucleotide frequency graph
Generate full report (and save to file)
Exit

---

## 🐛 Debugging Common Errors

| Error Message | Likely Cause | Solution |
|---|---|---|
| `ModuleNotFoundError: No module named 'matplotlib'` | Matplotlib not installed | Run `pip install -r requirements.txt` |
| `FileNotFoundError` | Wrong FASTA file path | Check the file path is correct relative to where you run `main.py` |
| `ERROR: This is not a valid DNA sequence` | Sequence contains letters other than A, T, G, C | Check for typos, spaces, or other characters (e.g., 'N', numbers) |
| Program shows blank/empty results | Empty sequence input | Make sure you typed/pasted a sequence before pressing Enter |
| `IndentationError` | Inconsistent spacing in code | Make sure you use 4 spaces (not tabs) consistently for indentation |

---

## 🚀 Future Improvements

- Support for multi-sequence FASTA files
- Reverse translation (protein → possible DNA sequences)
- Open Reading Frame (ORF) finder across all 6 reading frames
- GUI version using Tkinter or a web app using Streamlit/Flask
- Support for ambiguous bases (N, R, Y, etc.) per IUPAC codes
- Unit tests using pytest
- Command-line arguments (e.g., `python main.py --file data/sample.fasta`)
- Codon usage frequency analysis
- Integration with NCBI databases via Biopython/Entrez

---

## 👤 Author

**[Abida rehman]**
B.Sc. Biochemistry | Aspiring Bioinformatician
[www.linkedin.com/in/abida-rehman-a08b92283] |  | [rehmanabida634@gmail.com]

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).