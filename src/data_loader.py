class DataLoader:
    def __init__(self, data_dir='../data', processed_dir=None):
        from pathlib import Path
        self.data_dir = Path(data_dir)
        self.processed_dir = Path(processed_dir) if processed_dir else self.data_dir / 'processed'

    def load_news(self):
        import pandas as pd
        news_path = self.data_dir / 'raw_analyst_ratings.csv'
        df_news = pd.read_csv(news_path)
        df_news['date'] = pd.to_datetime(df_news['date'], utc=True, errors='coerce')
        df_news['date_day'] = df_news['date'].dt.date
        df_news['headline'] = df_news['headline'].astype(str)
        return df_news

    def load_stock(self, ticker):
        import pandas as pd
        stock_path = self.processed_dir / f'{ticker}_processed.csv'
        df_stock = pd.read_csv(stock_path, parse_dates=['Date'])
        df_stock['date_day'] = df_stock['Date'].dt.date
        return df_stock
