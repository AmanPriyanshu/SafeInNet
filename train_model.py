import pandas as pd
import os
import preprocessor as p
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import numpy as np

def get_data():
	path = "./data/sent_train.csv"
	if not os.path.exists(path):
		data_source_url = "https://raw.githubusercontent.com/kolaveridi/kaggle-Twitter-US-Airline-Sentiment-/master/Tweets.csv"
		airline_tweets = pd.read_csv(data_source_url)
		airline_tweets.to_csv(path, index=False)
	airline_tweets = pd.read_csv(path, usecols=["airline_sentiment", "text"])
	airline_tweets.text = [p.clean(i) for i in airline_tweets.text]
	airline_tweets.airline_sentiment = [1 if i in ["positive", "neutral"] else 0 for i in airline_tweets.airline_sentiment]
	return airline_tweets

def train_model(df, vector_path='./base_classifier/vectorizer.pickle', model_path='./base_classifier/model.pickle'):
	if not os.path.exists(vector_path):
		print("Initializing...")
		vectorizer = TfidfVectorizer(min_df=5)
		tfidf = vectorizer.fit([i for i in df.text])
		pickle.dump(tfidf, open(vector_path, "wb"))
	else:
		tfidf = pickle.load(open(vector_path, 'rb'))
	X = tfidf.transform([i for i in df.text])
	X = X.toarray()
	if not os.path.exists(model_path):
		clf = RandomForestClassifier(max_depth=5, n_estimators=500, random_state=0)
		clf.fit(X, [i for i in df.airline_sentiment])
		pickle.dump(clf, open(model_path, "wb"))
	clf = pickle.load(open(model_path, "rb"))
	y_ = clf.predict(X)
	print(classification_report([i for i in df.airline_sentiment], y_))

if __name__ == '__main__':
	data = get_data()
	train_model(data)