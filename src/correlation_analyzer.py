class CorrelationAnalyzer:
    def __init__(self, ticker):
        self.ticker = ticker

    def aggregate_daily_sentiment(self, df_news):
        return df_news[df_news['stock'] == self.ticker].groupby('date_day').agg(
            avg_sentiment=('sentiment', 'mean'),
            count=('sentiment', 'count')
        ).reset_index()

    def merge_and_correlate(self, df_stock, daily_sentiment):
        import pandas as pd
        df_stock['return'] = df_stock['Close'].pct_change()
        merged = pd.merge(df_stock, daily_sentiment, how='left', on='date_day')
        merged['avg_sentiment'] = merged['avg_sentiment'].fillna(0)
        corr = merged[['avg_sentiment', 'return']].corr().iloc[0,1]
        return merged, corr
