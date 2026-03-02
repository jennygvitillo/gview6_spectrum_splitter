#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Simple script to separate UV-Vis spectrum files from GaussView 6 into two parts:

1. PEAKS section -> filename_hyst.txt (all data from Peak information section)
2. SPECTRA section -> filename_spectrum.txt (all data from Spectra section)

Data is copied removing the # character at the beginning of each line.
Script created with DeepSeek, 2026.
"""

import os
import glob


def separate_file(input_filename, output_folder=None):
    """
    Separate a file into two parts: peaks and continuous spectrum
    """
    print(f"\nProcessing: {os.path.basename(input_filename)}")

    # Read the entire file
    with open(input_filename, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()

    # Variables to collect the two sections
    peaks_section = []
    spectra_section = []

    # Flags to track which section we're in
    in_peaks = False
    in_spectra = False

    for line in lines:
        original_line = line  # Keep original line for control

        # Detect start of peaks section
        if '# Peak information' in line:
            in_peaks = True
            in_spectra = False
            # Don't add the header line to data
            continue

        # Detect start of spectra section
        if '# Spectra' in line:
            in_spectra = True
            in_peaks = False
            # Don't add the header line to data
            continue

        # Detect end of a section (empty line)
        if line.strip() == '':
            if in_peaks:
                in_peaks = False
            if in_spectra:
                in_spectra = False

        # Add the line to the current section, removing the # at the beginning
        if in_peaks or in_spectra:
            # Remove the # character at the beginning of the line (if present)
            if line.startswith('#'):
                line_without_hash = line[1:]  # Removes only the first character
            else:
                line_without_hash = line

            if in_peaks:
                peaks_section.append(line_without_hash)
            elif in_spectra:
                spectra_section.append(line_without_hash)

    # Determine output folder
    if output_folder is None:
        output_folder = os.path.dirname(input_filename)
    else:
        os.makedirs(output_folder, exist_ok=True)

    # Output file names
    base = os.path.splitext(os.path.basename(input_filename))[0]
    peaks_file = os.path.join(output_folder, f"{base}_hyst.txt")
    spectra_file = os.path.join(output_folder, f"{base}_spectrum.txt")

    # Save peaks section
    if peaks_section:
        with open(peaks_file, 'w') as f:
            f.writelines(peaks_section)
        print(f"  Created: {os.path.basename(peaks_file)} ({len(peaks_section)} lines)")
    else:
        print(f"  Warning: no peaks section found")

    # Save spectra section
    if spectra_section:
        with open(spectra_file, 'w') as f:
            f.writelines(spectra_section)
        print(f"  Created: {os.path.basename(spectra_file)} ({len(spectra_section)} lines)")
    else:
        print(f"  Warning: no spectra section found")

    return len(peaks_section) > 0, len(spectra_section) > 0


def main():
    print("=" * 60)
    print("UV-VIS SPECTRA FILE SEPARATOR FROM GAUSSVIEW 6")
    print("=" * 60)
    print("This script separates each file into two parts:")
    print("  - [name]_hyst.txt      (Peak information section)")
    print("  - [name]_spectrum.txt  (Spectra section)")
    print("=" * 60)
    print("NOTE: The # character at the beginning of each line is removed")
    print("=" * 60)

    # Ask for the folder
    default_folder = os.getcwd()
    print(f"\nDefault folder: {default_folder}")
    input_folder = input("Enter the path to the folder with .txt files (Enter to use default): ").strip()

    if input_folder and os.path.isdir(input_folder):
        folder = input_folder
    else:
        folder = default_folder
        if input_folder:
            print(f"Folder not found, using default folder.")

    print(f"\nSearching for .txt files in: {folder}")

    # Find all .txt files
    txt_files = glob.glob(os.path.join(folder, "*.txt"))

    if not txt_files:
        print("No .txt files found.")
        return

    print(f"\nFound {len(txt_files)} files:")
    for i, f in enumerate(txt_files, 1):
        print(f"  {i}. {os.path.basename(f)}")

    # Ask which files to process
    print("\nOptions:")
    print("  a - Process ALL files")
    print("  n - Process only some files (enter numbers, e.g. 1,3,5-8)")
    print("  q - Quit")

    choice = input("\nChoose: ").strip().lower()

    if choice == 'q':
        return
    elif choice == 'a':
        files_to_process = txt_files
    elif choice == 'n':
        try:
            indices = input("Enter file numbers: ").strip()
            numbers = []
            for part in indices.split(','):
                part = part.strip()
                if '-' in part:
                    start, end = map(int, part.split('-'))
                    numbers.extend(range(start, end + 1))
                elif part:
                    numbers.append(int(part))

            files_to_process = [txt_files[i - 1] for i in numbers if 1 <= i <= len(txt_files)]
            print(f"Selected {len(files_to_process)} files")
        except:
            print("Invalid input, processing all files.")
            files_to_process = txt_files
    else:
        print("Invalid choice, processing all files.")
        files_to_process = txt_files

    # Ask where to save
    print("\nWhere to save the generated files?")
    print("  s - Same folder as original files")
    print("  o - Other folder")
    save_choice = input("Choose (default=s): ").strip().lower()

    output_folder = None
    if save_choice == 'o':
        output_folder = input("Enter the path to the output folder: ").strip()

    # Process the files
    print("\n" + "=" * 60)
    peaks_count = 0
    spectra_count = 0

    for file in files_to_process:
        has_peaks, has_spectra = separate_file(file, output_folder)
        if has_peaks:
            peaks_count += 1
        if has_spectra:
            spectra_count += 1

    print("\n" + "=" * 60)
    print("OPERATION COMPLETED!")
    print(f"Files processed: {len(files_to_process)}")
    print(f"_hyst.txt files created: {peaks_count}")
    print(f"_spectrum.txt files created: {spectra_count}")
    print("=" * 60)


if __name__ == "__main__":
    main()

