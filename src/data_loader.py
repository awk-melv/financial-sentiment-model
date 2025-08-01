# src/data_loader.py

import pandas as pd
import os

def load_articles(file_path: str) -> pd.DataFrame:
    """
    Load financial articles from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: DataFrame containing article data.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    df = pd.read_csv(file_path)

    # Optional: Clean up common whitespace issues
    df['title'] = df['title'].astype(str).str.strip()
    df['content'] = df['content'].astype(str).str.strip()

    return df
