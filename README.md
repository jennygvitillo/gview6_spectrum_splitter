This script automatically splits GaussView 6 text files containing UV-Vis spectra into two separate files: one for the peak information and one for the continuous spectrum data, removing the # character at the beginning of each line for clean numerical data.

Features
Automatic Section Detection: Identifies and separates "Peak information" and "Spectra" sections from GaussView output files

Clean Data Output: Removes the # character at the beginning of each line for easy import into plotting software

Batch Processing: Processes multiple .txt files in a folder automatically

Selective Processing: Choose to process all files or specific ones using number ranges (e.g., 1,3,5-8)

Flexible Output: Save files in the same folder as originals or in a custom output directory

Preserves Data Integrity: Copies all data exactly as in the original, only removing the leading # character

Input Requirements
GaussView 6 output files in .txt format containing UV-Vis spectra data

Files must contain the standard GaussView sections:

# Peak information section

# Spectra section

Output Files
For each input file filename.txt, the script generates:

File	Content
filename_hyst.txt	Peak information data (without #)
filename_spectrum.txt	Continuous spectrum data (without #)
