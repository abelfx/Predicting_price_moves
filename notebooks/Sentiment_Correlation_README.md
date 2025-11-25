# Sentiment Correlation Analysis Notebook

This notebook analyzes the relationship between news sentiment and stock price movements for multiple tickers. It is part of the **Predicting Price Moves with News Sentiment** project.

## Overview

- Loads processed news and stock data for selected tickers (AMZN, GOOG, NVDA, MSFT).
- Performs sentiment analysis on headlines using TextBlob.
- Aggregates daily sentiment scores for each ticker.
- Calculates daily returns for each stock.
- Merges sentiment scores with daily returns.
- Computes Pearson correlation between average daily sentiment and daily returns.
- Visualizes sentiment vs. return for each ticker.
- Summarizes findings and insights for actionable strategies.

## Key Sections

1. **Data Loading**
   - Loads news and stock data from processed CSVs.
   - Ensures date alignment for accurate merging.
2. **Sentiment Analysis**
   - Assigns sentiment scores to headlines.
   - Aggregates daily sentiment per ticker.
3. **Return Calculation**
   - Computes daily percentage change in closing prices.
4. **Correlation Analysis**
   - Merges sentiment and returns by date.
   - Calculates Pearson correlation coefficient.
5. **Visualization**
   - Scatter plots of sentiment vs. return for each ticker.
6. **Findings & Insights**
   - Summarizes results and recommendations.

## Usage

1. Open notebook in Jupyter Lab or VS Code.
2. Ensure processed data is available in `data/processed/`.
3. Install dependencies:

```bash
pip install -r ../requirements.txt
```

4. Run cells sequentially to reproduce analysis.
5. Review findings for actionable insights.
