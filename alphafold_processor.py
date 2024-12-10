import os
import json
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Button, filedialog

def process_json_files(folder_path):
    # Process all JSON files in the folder
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        
        if file_name.endswith(".json"):
            # Load JSON data
            with open(file_path, "r") as f:
                data = json.load(f)
            
            # Generate Confidence Plot (pLDDT)
            if "atom_plddts" in data:
                plddt_scores = data["atom_plddts"]
                plt.figure(figsize=(12, 4))
                plt.plot(plddt_scores, color='blue', label='pLDDT')
                plt.title(f"AlphaFold Confidence Plot (pLDDT) - {file_name}", fontsize=14)
                plt.xlabel("Atom Index", fontsize=12)
                plt.ylabel("Confidence (pLDDT)", fontsize=12)
                plt.axhline(y=90, color='green', linestyle='--', label='High Confidence (>90)')
                plt.axhline(y=70, color='orange', linestyle='--', label='Medium Confidence (70-90)')
                plt.axhline(y=50, color='red', linestyle='--', label='Low Confidence (<70)')
                plt.legend()
                plt.grid(alpha=0.5)
                plt.savefig(os.path.join(folder_path, f"{file_name}_plddt_plot.png"))
                plt.close()

            # Generate PAE Heatmap
            if "pae" in data:
                pae_matrix = np.array(data["pae"])
                plt.figure(figsize=(8, 8))
                plt.imshow(pae_matrix, cmap="Greens", origin="lower")
                plt.colorbar(label="Expected Position Error (Ångströms)", orientation="horizontal")
                plt.title(f"Predicted Aligned Error (PAE) - {file_name}", fontsize=16)
                plt.xlabel("Scored Residue", fontsize=12)
                plt.ylabel("Aligned Residue", fontsize=12)
                plt.savefig(os.path.join(folder_path, f"{file_name}_pae_heatmap.png"))
                plt.close()

            # Extract PTM and iPTM Scores
            if "iptm" in data or "ptm" in data:
                iptm = data.get("iptm", "Not found")
                ptm = data.get("ptm", "Not found")
                chain_iptm = data.get("chain_iptm", "Not found")
                chain_ptm = data.get("chain_ptm", "Not found")
                chain_pair_iptm = data.get("chain_pair_iptm", "Not found")
                
                # Save scores to a text file
                with open(os.path.join(folder_path, f"{file_name}_scores.txt"), "w") as score_file:
                    score_file.write(f"Global iPTM: {iptm}\n")
                    score_file.write(f"Global PTM: {ptm}\n")
                    score_file.write(f"Per-chain iPTM: {chain_iptm}\n")
                    score_file.write(f"Per-chain PTM: {chain_ptm}\n")
                    score_file.write(f"Pairwise chain iPTM: {chain_pair_iptm}\n")

    print("Processing complete. Outputs saved to:", folder_path)

# Create the GUI application
def create_gui():
    def select_folder():
        folder_path = filedialog.askdirectory(title="Select Folder Containing JSON Files")
        if folder_path:
            label.config(text=f"Processing files in: {folder_path}")
            process_json_files(folder_path)
            label.config(text="Processing complete! Outputs saved to the folder.")

    # Create the main GUI window
    root = Tk()
    root.title("AlphaFold JSON Processor")
    root.geometry("500x250")  # Increased height to accommodate footer text

    # Add GUI elements
    Label(root, text="Select a folder containing JSON files for processing", font=("Arial", 12)).pack(pady=10)
    Button(root, text="Select Folder", command=select_folder, font=("Arial", 12), bg="blue", fg="white").pack(pady=10)
    label = Label(root, text="", font=("Arial", 10))
    label.pack(pady=10)

    # Add footer text
    footer = Label(root, text="B.J.20241210 @ WashU Berkland Lab  MIT-OCW", font=("Arial", 10, "italic"), fg="gray")
    footer.pack(side="bottom", pady=10)

    # Run the GUI loop
    root.mainloop()

# Run the application
create_gui()
