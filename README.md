Python tool for separating GaussView 6 UV-Vis output files into peaks and continuous spectrum data

This **Python** tool automatically splits GaussView 6 text files containing UV-Vis spectra into two separate files: one for the peak information and one for the continuous spectrum data, removing the # character at the beginning of each line for clean numerical data.

## Features
Automatic Section Detection: Identifies and separates "Peak information" and "Spectra" sections from GaussView output files
Clean Data Output: Removes the # character at the beginning of each line for easy import into plotting software
Batch Processing: Processes multiple .txt files in a folder automatically
Flexible Output: Save files in the same folder as originals or in a custom output directory
Preserves Data Integrity: Copies all data exactly as in the original, only removing the leading # character

## Input Requirements
GaussView 6 output files in .txt format containing UV-Vis spectra data

Files must contain the standard GaussView sections:
Peak information section
Spectra section

## Output Files
For each input file filename.txt, the script generates two files:
- filename_hyst.txt	Peak information data (without #)
- filename_spectrum.txt	Continuous spectrum data (without #)


## Italiano
Separatore di spettri UV-Vis da GaussView 6

Strumento Python per separare automaticamente i file di output di GaussView 6 contenenti spettri UV-Vis in due parti: dati dei picchi e spettro continuo, rimuovendo il carattere # all'inizio di ogni riga per ottenere dati numerici puliti.

**Caratteristiche**
Rilevamento Automatico delle Sezioni: Identifica e separa le sezioni "Peak information" e "Spectra"
Dati Puliti: Rimuove il carattere # all'inizio di ogni riga per facile importazione in software di plotting
Elaborazione in Batch: Processa automaticamente multipli file .txt in una cartella
Selezione File: Scegli quali file processare usando intervalli numerici (es. 1,3,5-8)
Output Flessibile: Salva i file nella stessa cartella o in una directory personalizzata
