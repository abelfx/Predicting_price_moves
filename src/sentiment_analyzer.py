class SentimentAnalyzer:
    def __init__(self, method='textblob'):
        if method == 'textblob':
            from textblob import TextBlob
            self.analyze = lambda text: TextBlob(text).sentiment.polarity
        else:
            raise NotImplementedError('Only textblob supported for now')

    def add_sentiment(self, df, text_col='headline', out_col='sentiment'):
        df[out_col] = df[text_col].apply(self.analyze)
        return df
