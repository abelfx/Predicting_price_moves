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

| Column     | Description |
|-----------|-------------|
| headline  | Title of the news article, often indicating key financial actions. |
| url       | Direct link to the full article. |
| publisher | Author or source of the news. |
| date      | Publication date & time (UTC-4). |
| stock     | Stock ticker symbol (e.g., AAPL for Apple). |

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


## Task Summary
- **Task 1 – EDA:**  
  - Descriptive statistics: headline length, publisher frequency, publication trends.  
  - Text analysis: keyword extraction, topic modeling.  
  - Time series analysis: publication spikes and patterns.

- **Task 2 – Quantitative Analysis:**  
  - Stock data preparation and alignment.  
  - Technical indicators: Moving Averages (MA), Relative Strength Index (RSI), MACD.  
  - Visualization of indicators against historical stock prices.

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

## Tech Stack
- **Python 3.11**  
- **Libraries:** pandas, numpy, matplotlib, seaborn, nltk, TextBlob, TA-Lib, PyNance  
- **Version Control:** Git, GitHub  
- **Environment Management:** virtualenv / pip  

## Reproducing the Environment
1. Clone the repository:
```bash
git clone https://github.com/<username>/financial-news-sentiment.git
cd predicting_price_moves
```
2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```
3. install dependencies
```bash
pip install -r requirements.txt
```

   
