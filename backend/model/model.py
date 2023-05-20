import pandas as pd
from sklearn.model_selection import train_test_split
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
import joblib

def main():
    news = pd.read_csv('data/news.csv')
    options = ['REAL', 'FAKE']
    news = news.loc[news['label'].isin(options)]

    # Divide Dataset into features and labels
    # Features only include the text not the title of the article
    features = news.loc[:, 'text'].values
    labels = news.loc[:, 'label'].values

    # Split into training and test data (80/20 split)

    x_training_data, x_test_data, y_training_data, y_test_data = train_test_split(
        news['text'],labels, test_size=0.2, random_state=7)
    
    nltk.download('stopwords')

    # Initialize TfidfVectorizer
    vectorizer = TfidfVectorizer(stop_words=('english'), max_df=0.7)

    # Fit and transform train set, transform test set
    tfidf_train = vectorizer.fit_transform(x_training_data)

    # Initialize PassiveAggressiveClassifier
    pa = PassiveAggressiveClassifier(max_iter=50)
    pa.fit(tfidf_train, y_training_data)

    # Save model and vectorizer
    joblib.dump(pa, 'pa_model.pkl')
    joblib.dump(vectorizer, 'vectorizer.pkl')

if __name__ == "__main__":
    main()