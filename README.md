Group 56: Ayushman Choudhury and Rohan Badami

FOR THE TA TO REPRODUCE THE CODE: 

step 1) git clone https://github.com/rohanbadami/DS340W.git
step 2) cd DS340W
step 3) pip install pandas requests jupyter
step 4) jupyter notebook
open the notebook, select kernel -> restart and run all cells. all cells should run now 

OUR RESULTS: 

•	FinBERT sentiment is internally consistent and produces sensible per-ticker profiles.
•	However, under this modeling setup (absolute daily returns with tree models), sentiment and novelty features do not provide meaningful incremental predictive power beyond price-based features.
•	Both the placebo experiment and rolling backtest suggest that any performance gains from sentiment are tiny and not robust, which is the main substantive result.

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

No manual download is required by the TAs.

