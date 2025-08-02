#from src.sentiment_model import train_sentiment_model
#from src.stock_predictor import predict_stock_impact
from src.data_loader import load_articles
from src.sentiment_model import add_sentiment_scores


if __name__ == "__main__":
    # print("Training sentiment model...")
    # train_sentiment_model()

    # print("Predicting stock impact...")
    # predict_stock_impact()

    df = load_articles('data/articles.csv')
    df = add_sentiment_scores(df, text_column="content")
    print(df[["title", "sentiment_score"]].head())
