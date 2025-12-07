Group 56: Ayushman Choudhury and Rohan Badami

FOR THE TA TO REPRODUCE THE CODE: 

step 1) git clone https://github.com/rohanbadami/DS340W.git
step 2) cd DS340W
step 3) pip install pandas requests jupyter
step 4) jupyter notebook
open the notebook, select kernel -> restart and run all cells. all cells should run now 

OUR RESULTS: 

•	We tested 10 stocks with daily prices and one news headline per day.
    
•	We used FinBERT to score each headline for positive or negative tone. 
•	We built models to predict next-day volatility using: 
    1.	price data only and 
    2.	price data plus sentiment. 
•	Both models gave almost the same accuracy.
•	The sentiment features did not improve predictions in a meaningful way. 
•	In short: price history explains volatility better than news tone in this dataset. 
•	Sentiment matters a little, but not enough to change results.

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

