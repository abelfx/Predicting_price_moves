# EDA and Sentiment Analysis Notebook

This notebook performs exploratory data analysis (EDA) and sentiment analysis on financial news headlines.  
It is part of the **Predicting Price Moves with News Sentiment** project.

## Overview

- Loads the raw analyst ratings dataset (`raw_analyst_ratings.csv`).
- Ensures date columns are timezone-aware (UTC-4).
- Computes basic descriptive statistics on headlines (length, counts, etc.).
- Preprocesses text (cleaning, stopword removal, tokenization).
- Conducts topic modeling using frequent words and n-grams.
- Applies sentiment scoring using VADER.
- Performs time series analysis of publication patterns.
- Analyzes publisher activity and domains.

## Key Sections

1. **Load Dataset**
   - Reads CSV into Pandas.
   - Converts date column to UTC timezone.
   - Prints initial rows and dataset size.

2. **Descriptive Statistics**
   - Calculates headline lengths.
   - Counts articles per publisher.
   - Generates summary statistics.

3. **Text Preprocessing**
   - Cleans headlines (removes URLs, non-alphanumeric chars, converts to lowercase).
   - Removes stopwords.
   - Computes token counts.

4. **Topic Modeling**
   - Uses `CountVectorizer` to extract frequent words and bigrams.
   - Sorts terms by frequency to detect common market events or themes.

5. **Sentiment Scoring**
   - Uses `VADER` sentiment analysis.
   - Adds compound sentiment score to dataset.
   - Samples dataset if large for faster processing.

6. **Time Series Analysis**
   - Aggregates articles per day and per hour.
   - Plots daily publication counts.
   - Plots hourly distribution of news release times.

7. **Publisher Analysis**
   - Counts articles per publisher.
   - Extracts domains from publisher emails for additional insight.
   - Plots top 10 domains and publisher activity.

## Usage

1. Open the notebook in Jupyter Lab or VS Code.
2. Ensure the `data/` folder contains:
   - `raw_analyst_ratings.csv`
3. Install dependencies:

```bash
pip install -r ../requirements.txt
```
4. Run cells sequentially to reproduce EDA and sentiment analysis.


Output
- Cleaned and tokenized dataset with sentiment scores.
Plots:
- Articles per day
- Articles by hour
- Top publishers and domains
- Frequent topic keywords.
