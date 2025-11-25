# Predicting Price Moves with News Sentiment

## Overview

Dive into real-world financial news and discover how headlines shape stock swings. This project analyzes financial news sentiment, computes technical indicators, and investigates correlations between news sentiment and daily stock returns to inform predictive analytics.

## Business Context

Nova Financial Solutions aims to enhance its financial forecasting capabilities using advanced data analysis. The primary goal is to leverage news sentiment to predict stock price movements. This involves:

- **Sentiment Analysis:** Quantifying tone in headlines using NLP to understand emotional context around stocks.
- **Correlation Analysis:** Measuring the relationship between news sentiment and stock price changes to inform investment strategies.

The project integrates **Data Engineering (DE)**, **Financial Analytics (FA)**, and **Machine Learning Engineering (MLE)** to improve predictive insights.

## Dataset Overview

We use the **Financial News and Stock Price Integration Dataset (FNSPID)**, which combines quantitative stock price data with qualitative news headlines.

| Column    | Description                                                        |
| --------- | ------------------------------------------------------------------ |
| headline  | Title of the news article, often indicating key financial actions. |
| url       | Direct link to the full article.                                   |
| publisher | Author or source of the news.                                      |
| date      | Publication date & time (UTC-4).                                   |
| stock     | Stock ticker symbol (e.g., AAPL for Apple).                        |

## Project Structure

```
├── .vscode/
│ └── settings.json
├── .github/
│ └── workflows/
│ └── unittests.yml
├── .gitignore
├── requirements.txt
├── README.md
├── src/
│ ├── init.py
├── notebooks/
│ ├── init.py
│ └── eda_and_sentiment.ipynb
│ └── quant_analysis.ipynb
├── tests/
│ ├── init.py
└── scripts/
├── init.py
```

- Descriptive statistics: headline length, publisher frequency, publication trends.

## Task Summary

- **Task 1 – EDA:**
  - Descriptive statistics: headline length, publisher frequency, publication trends.
  - Topic modeling and sentiment scoring for headlines.
- **Task 2 – Quantitative Analysis:**
  - Stock data preparation and alignment.
  - Technical indicators (SMA, EMA, RSI, MACD, Bollinger Bands, ATR, OBV, Stochastic, ADX) for all tickers.
  - Merges stock prices with headline events and calculates daily returns.
  - Visualization of indicators against historical stock prices.
- **Task 3 – Sentiment Correlation:**

  - Sentiment analysis on headlines for AMZN, GOOG, NVDA, MSFT.
  - Aggregates daily sentiment and computes correlation with daily returns.
  - Visualizes and summarizes findings for actionable investment strategies.
  - Text analysis: keyword extraction, topic modeling.
  - Time series analysis: publication spikes and patterns.


## Key EDA Activities

- Counted articles per publisher to identify most active sources.
- Measured headline lengths and identified outliers.
- Extracted prominent keywords and phrases to highlight major financial events.
- Examined publishing trends by time of day and date to detect strategic news releases.

## Insights

- Bloomberg, Reuters, and MarketWatch are the top contributors.
- Short-term MAs respond quickly to news-driven price swings.
- RSI spikes correlate with high sentiment headlines.
- Most news is published during market open hours, with weekly spikes around earnings periods.

## Results

### EDA & Sentiment Analysis

- Headlines are generally short; a few publishers dominate the news flow.
- Publication times cluster around market open hours.
- Topic modeling reveals frequent terms like “price target”, “earnings”, “upgrade”, “FDA approval”.

### Quantitative Analysis

- Technical indicators computed for all tickers.
- Headline events merged with price data for event studies.

### Sentiment Correlation

- Sentiment scores analyzed for AMZN, GOOG, NVDA, MSFT.
- Correlation between daily sentiment and returns is generally weak, but spikes in sentiment can coincide with larger price moves.
- Relationship varies by ticker and news volume.
- For actionable strategies, combine sentiment with technical indicators and filter for high-sentiment days.

## How to Run

1. Clone the repository and install dependencies:

```bash
pip install -r requirements.txt
```

2. Place raw and processed data files in the `data/` folder.
3. Open notebooks in VS Code or Jupyter Lab and run cells sequentially.
4. Review results and visualizations for insights.

