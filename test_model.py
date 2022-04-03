import pickle
import numpy as np

def get_predictions(texts, vector_path='./base_classifier/vectorizer.pickle', model_path='./base_classifier/model.pickle'):
	tfidf = pickle.load(open(vector_path, 'rb'))
	X = tfidf.transform(texts)
	X = X.toarray()
	clf = pickle.load(open(model_path, "rb"))
	y_ = clf.predict_proba(X)
	return y_.T[1]