# AlphaFold-JSON-Processor
A Python GUI tool to process AlphaFold JSON files, generating confidence plots (pLDDT), PAE heatmaps, and extracting PTM/iPTM scores. Simply select a folder, and it processes all JSON files, saving outputs (plots and scores) in the same directory for visualization and analysis.

# AlphaFold JSON Processor

AlphaFold JSON Processor is a Python-based GUI application that processes AlphaFold prediction JSON files. It generates:
- Confidence plots (pLDDT)
- PAE heatmaps
- Extracted PTM and iPTM scores

This software is designed to simplify the visualization and analysis of AlphaFold prediction results.

## Features

- **Confidence Plot (pLDDT)**: Generates line plots showing confidence scores for each atom.
- **PAE Heatmap**: Visualizes the Predicted Aligned Error (PAE) matrix.
- **PTM and iPTM Scores**: Extracts and saves global and per-chain scores in text format.
- **User-Friendly GUI**: Select a folder, and the tool processes all `.json` files in the directory.

## How to Install and Run

### Prerequisites

Ensure you have the following installed:
- Python 3.7 or later
- Required Python libraries:
  - `numpy`
  - `matplotlib`
  - `tkinter` (included with most Python installations)

### Installation

1. Clone the repository from GitHub:
   ```bash
   git clone https://github.com/<your-username>/alphafold-json-processor.git
   cd alphafold-json-processor
2. Install the dependencies:
    pip install numpy matplotlib

### Usage
1. Navigate to the script's location: cd /path/to/alphafold-json-processor
2. Run the script:python alphafold_processor.py
3. A GUI window will open. Follow these steps:
  - Click "Select Folder" to choose a directory containing AlphaFold JSON files.
  - The tool will process all .json files in the selected folder.
  - Outputs will be saved in the same folder, including:
    - Confidence plots (*_plddt_plot.png)
    - PAE heatmaps (*_pae_heatmap.png)
    - PTM and iPTM scores (*_scores.txt)
4. The footer in the GUI displays the developer information.

### Output Files
For each JSON file, the following outputs are generated:
- Confidence Plot: <filename>_plddt_plot.png
- PAE Heatmap: <filename>_pae_heatmap.png
- PTM and iPTM Scores: <filename>_scores.txt

### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Developer
This software was developed by B.J. at WashU Berkland Lab on 2024-12-10.

```plaintext
MIT License

Copyright (c) 2024 B.J. WashU Berkland Lab

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
