import pandas as pd
import numpy as np
from test_model import get_predictions

def read_reviews(latitude, longitude, N=10, dist=0.5):
	seed = int(latitude+longitude)
	np.random.seed(abs(seed))
	negatives = pd.read_csv("./data/negatives.csv")
	negatives = negatives.values
	negatives = negatives.flatten()
	positives = pd.read_csv("./data/positives.csv")
	positives = positives.values
	positives = positives.flatten()
	texts = np.stack([np.concatenate((positives, negatives)), np.concatenate(((np.random.random(size=len(positives))/2+0.5)**0.85, (np.random.random(size=len(negatives))/2)))**1.05]).T
	np.random.shuffle(texts)
	reviews = pd.read_csv("./data/user_data.csv")
	reviews = reviews.values
	closest_text = []
	for row in reviews:
		lat = float(row[1])
		lon = float(row[2])
		d = ((latitude-lat)**2+(longitude-lon)**2)**0.5
		if d<dist:
			closest_text.append(row[0])
	closest_text.reverse()
	return closest_text[:N]+[i[0] for i in texts][:N-len(closest_text)]

def predict_reviews(texts):
	preds = get_predictions(texts)
	return [[i, j] for i, j in zip(texts, preds)]

def get_reviews(latitude, longitude, N=10, d=0.5):
	reviews = read_reviews(latitude, longitude, N=N, dist=d)
	reviews = predict_reviews(reviews)
	return reviews

if __name__ == '__main__':
	reviews = read_reviews(40.6635697,-73.9299531)
	text_pred = predict_reviews(reviews)
	_ = [print(i) for i in text_pred]