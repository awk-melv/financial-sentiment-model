#from src.sentiment_model import train_sentiment_model
#from src.stock_predictor import predict_stock_impact
from src.data_loader import load_articles


if __name__ == "__main__":
    # print("Training sentiment model...")
    # train_sentiment_model()

    # print("Predicting stock impact...")
    # predict_stock_impact()

    df = load_articles('data/articles.csv')
    print(df.head())
