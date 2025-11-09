import polars as pl
import pandas as pd
import yfinance as yf
from pathlib import Path

news_path = "/Users/rohanbadami/Downloads/filtered_4tickers_only.parquet"
output_dir = Path("/Users/rohanbadami/Downloads/news_with_prices_all")
output_dir.mkdir(exist_ok=True)

print("Loading news parquet...")
news = pl.read_parquet(news_path)
tickers = ["AAPL", "MSFT", "AMZN", "GOOGL"]
all_merged = []  # store per ticker merged dfs 

for t in tickers:

    df = news.filter(pl.col("Stock_symbol") == t)
    df = df.with_columns(pl.col("Date").dt.date().alias("news_date"))
    df_pd = df.to_pandas()

    if df_pd.empty:
        print(f"No news data for {t}, skipping.")
        continue

    # appropriate date range for each stock 
    min_date = df_pd["news_date"].min()
    max_date = df_pd["news_date"].max()
    print(f" News covers from {min_date} → {max_date}")

    start_date = pd.to_datetime(min_date).strftime("%Y-%m-%d")
    end_date = (pd.to_datetime(max_date) + pd.Timedelta(days=3)).strftime("%Y-%m-%d")

    # fetching yfinance data 
    print(f" Fetching {t} price data...")
    try:
        data = yf.download(t, start=start_date, end=end_date, progress=False)
    except Exception as e:
        print(f"Failed to fetch {t}: {e}")
        continue

    if data.empty:
        print(f"No price data returned for {t}, skipping.")
        continue

    # flattening multiindex columns from yfinance
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = [col[0] for col in data.columns]

    data.reset_index(inplace=True)
    data["date_price"] = pd.to_datetime(data["Date"]).dt.date
    data["price_symbol"] = t

    # merge keys are of same type 
    df_pd["news_date"] = pd.to_datetime(df_pd["news_date"]).dt.date
    data["date_price"] = pd.to_datetime(data["date_price"]).dt.date

    # merging news from fnspid with yfinance price data
    merged = pd.merge(
        df_pd,
        data[["price_symbol", "date_price", "Open", "High", "Low", "Close", "Volume"]],
        left_on=["Stock_symbol", "news_date"],
        right_on=["price_symbol", "date_price"],
        how="left"
    )

    # forward Fill Missing Prices (for weekends etc.) | Parent paper does exponential decay imputation!
    merged = merged.sort_values(["Stock_symbol", "Date"])
    merged[["Open", "High", "Low", "Close", "Volume"]] = (
        merged[["Open", "High", "Low", "Close", "Volume"]].ffill()
    )

    merged["is_exact_match"] = merged["news_date"] == merged["date_price"]

    merged = merged.drop_duplicates(subset=["Stock_symbol", "Article_title", "Date"], keep="first")

    out_csv = output_dir / f"news_with_prices_{t}.csv"
    merged.to_csv(out_csv, index=False)
    print(f"Saved merged dataset for {t} → {out_csv}")

    all_merged.append(merged)

if all_merged:
    combined = pd.concat(all_merged, ignore_index=True)
    combined = combined.sort_values(["Stock_symbol", "Date"])
    combined_out = output_dir / "news_with_prices_ALL.csv"

    combined = combined.drop_duplicates(subset=["Stock_symbol", "Article_title", "Date"], keep="first")

    combined.to_csv(combined_out, index=False)
    print(f"\nUnified dataset saved → {combined_out}")
    print(f"Total rows: {len(combined):,}")
    print("Preview:")
    print(combined[["Stock_symbol", "Date", "news_date", "date_price", "Open", "Close", "is_exact_match"]].head(10))
else:
    print("No datasets were merged. Please check yfinance or parquet file paths.")
