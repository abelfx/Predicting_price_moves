# Quantitative Stock Analysis Notebook

This notebook performs quantitative analysis on historical stock data and integrates news headlines.  
It is part of the **Predicting Price Moves with News Sentiment** project.

## Overview

- Loads historical stock prices for multiple tickers (`AAPL`, `AMZN`, `GOOG`, `META`, `MSFT`, `NVDA`).
- Computes technical indicators using TA-Lib:
  - SMA, EMA, RSI, MACD, Bollinger Bands, ATR, OBV, Stochastic, ADX
- Merges stock prices with daily aggregated headlines.
- Calculates daily returns and next-day returns.
- Visualizes price charts with technical indicators and highlights headline events.

## Key Sections

1. **Load Dataset**
   - Reads CSVs for each ticker.
   - Parses `Date` column and sorts chronologically.
   - Raises error if file missing.

2. **Technical Indicators**
   - Functions to compute RSI, MACD, Bollinger Bands, ATR, OBV, Stochastic, ADX.
   - Adds indicators to each ticker’s dataframe.

3. **Merge Headlines with Prices**
   - Reads `raw_analyst_ratings.csv`.
   - Normalizes dates and aggregates headlines per day.
   - Merges with stock prices to create combined dataframe with:
     - `headlines_count`
     - `avg_headline_len`
     - `return` and `next_return`

4. **Visualization**
   - Plotly used for interactive charts.
   - Candlestick chart + technical indicators.
   - Marks headline events on stock price charts.

## Usage

1. Open notebook in Jupyter Lab or VS Code.
2. Ensure `data/` folder contains:
   - `raw_analyst_ratings.csv`
   - Stock CSVs (one per ticker)
3. Install dependencies:
```bash
pip install -r ../requirements.txt
```
4. Run cells sequentially to reproduce analysis.

Output:
- Stock dataframes with technical indicators.
- Merged dataset with headlines and stock movements.
- Interactive plots for each ticker with headline markers.


