import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def read_ratings(latitude, longitude, scores=[0.7]*10, path="./data/user_ratings.csv", dist=0.5):
	df = pd.read_csv(path)
	df = df.values
	closest_ratings = []
	for row in df:
		lat = float(row[1])
		lon = float(row[2])
		d = ((latitude-lat)**2+(longitude-lon)**2)**0.5
		if d<dist:
			closest_ratings.append(row[0])
	if len(closest_ratings)==0:
		user_rating = 0
		scores_weight = 1
	else:
		user_rating = (sum(closest_ratings)/len(closest_ratings))/5
		scores_weight = 0.2
	return round(5*(user_rating*(1-scores_weight)+sum(scores)/len(scores)*scores_weight), 2)

def image_generator(rating):
	plt.cla()
	img = np.zeros((10, 100, 3))
	img[:, :int(20*rating), 1] = 1.0
	img[:, int(20*rating):, 0] = 1.0
	plt.imshow(img)
	plt.axis('off')
	plt.savefig('bar_graph.png', bbox_inches='tight', pad_inches=0, transparent=True)

def get_ratings_bar(latitude, longitude, scores=[0.7]*10, path="./data/user_ratings.csv", dist=0.5):
	rating = read_ratings(latitude, longitude, scores=scores, path=path, dist=dist)
	image_generator(rating)
	return 'bar_graph.png'

if __name__ == '__main__':
	r = read_ratings(40.6635697,-73.9299531)
	image_generator(r)