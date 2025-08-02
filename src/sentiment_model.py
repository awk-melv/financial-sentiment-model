from textblob import TextBlob
import pandas as pd

def analyze_sentiment(text: str) -> float:
    """
    Analyze the sentiment of a given text.

    Args:
        text (str): Input text to analyze

    Returns:
        float: Polarity score from -1 (negative) to +1 (positive)
    """
    if not isinstance(text, str) or not text.strip():
        return None  # Neutral by default if text is empty or invalid

    blob = TextBlob(text)
    return blob.sentiment.polarity


def add_sentiment_scores(df: pd.DataFrame, text_column: str = "content") -> pd.DataFrame:
    """
    Adds a sentiment score column to a DataFrame.

    Args:
        df (pd.DataFrame): DataFrame containing text content
        text_column (str): Name of column containing text

    Returns:
        pd.DataFrame: DataFrame with a new 'sentiment_score' column
    """
    df = df.copy()
    df["sentiment_score"] = df[text_column].apply(analyze_sentiment)
    return df
