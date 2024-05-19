from textblob import TextBlob

class SentimentAnalyzer:
    @staticmethod
    def analyze_text(text):
        analysis = TextBlob(text)
        if analysis.sentiment.polarity > 0:
            return "positive"
        elif analysis.sentiment.polarity == 0:
            return "neutral"
        else:
            return "negative"
