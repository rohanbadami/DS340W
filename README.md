
Group 56: Ayushman Choudhury and Rohan Badami
This repository contains one runnable notebook: reproduce_and_novelty.ipynb.
It reproduces and extends results using processed datasets derived from the FNSPID dataset.

DATA

Raw data source: https://www.kaggle.com/datasets/blacksnail789521/time-imm

The processed dataset is not stored in this repository.
We made it so it is provided separately as a GitHub Release asset named processed.zip.

When the notebook is run, it automatically:
	•	downloads processed.zip from the GitHub Releases section
	•	extracts it into the folder: data/processed/
	•	reads ticker-level files from:
data/processed//time_series.csv
data/processed//text.csv

No manual download is required by the TAs 
