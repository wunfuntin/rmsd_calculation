import os
import subprocess
from pymol import cmd

def extract_pdb_from_silent(silent_file, pdb_id, binary_path):
    """
    Extracts a specific .pdb file from a .silent file using silent_tools.
    """
    command = f"{binary_path}/silentextractspecifc {silent_file} {pdb_id}"
    subprocess.run(command, shell=True)
    return f"{pdb_id}.pdb"

def calculate_rmsd(pdb_file1, pdb_file2):
    """
    Calculates RMSD between chain A of two pdb files using PyMOL.
    """
    cmd.load(pdb_file1, "structure1")
    cmd.load(pdb_file2, "structure2")
    rmsd = cmd.align("structure1 and chain A", "structure2 and chain A")[0]
    cmd.delete("structure1")
    cmd.delete("structure2")
    return rmsd

def main():
    silent_file1 = "/rmsd_silent_test/RFD_run_1.silent"
    silent_file2 = "/rmsd_silent_test/AF2_run_1.silent"
    binary_path = "/Users/rwalker/silent_tools"

    # Assuming a fixed range for the counting integer (e.g., 1 to 100)
    for i in range(1, 101):
        pdb_id1 = f"design_{i:04d}.pdb"
        pdb_id2 = f"design_{i:04d}.pdb"

        pdb_file1 = extract_pdb_from_silent(silent_file1, pdb_id1, binary_path)
        pdb_file2 = extract_pdb_from_silent(silent_file2, pdb_id2, binary_path)

        rmsd = calculate_rmsd(pdb_file1, pdb_file2)
        print(f"RMSD between {pdb_file1} and {pdb_file2}: {rmsd}")

        # Clean up extracted files
        os.remove(pdb_file1)
        os.remove(pdb_file2)

if __name__ == "__main__":
    main()
