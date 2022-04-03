import pandas as pd
import numpy as np
import os

all_samples = []
all_locations = []
basepath = "./raw_samples/"
for path in [basepath+i for i in os.listdir(basepath)]:
	with open(path, "r") as f:
		data = f.read()
		data = [i for i in data.split('<div class="r_description">')][1:]
		data_sample = [i[:i.index('<a class="btn-show btn-more"')].strip().replace("\n", " ") for i in data]
		data_loc = [i[i.index('<p class="r_location">')+len('<p class="r_location">'):] for i in data]
		data_loc = [i[i.index('">')+2:i.index('</a></p>')] for i in data_loc]
		all_locations.extend(data_loc)
		all_samples.extend(data_sample)
df = pd.DataFrame({'samples': all_samples, "locations": all_locations})
df.to_csv("samples.csv", index=False)
	