import pymongo
from app.mongo.yelp_client import YelpClient
from app.mongo.business import Business
from app.mongo.reviews import Reviews
import numpy as np
business_db = Business()
from scipy.spatial import distance
import pickle


with open('data.p', 'rb') as fp:
    data_vector_dictionary = pickle.load(fp)

input_array = np.array([0] * len(data_vector_dictionary['pQeaRpvuhoEqudo3uymHIQ']))
topk = 10
restaurant_display_list = []
dist_list = []

for key in data_vector_dictionary:
	d = distance.euclidean(input_array, data_vector_dictionary[key])
	dist_list.append([key,d])
dist_list.sort(key=lambda x: x[1])

restaurants = business_db.getBusiness()
for i in range(0,topk):
	for val in restaurants:
		if (val['business_id'] == dist_list[i][0]):
			restaurant_display_list.append([val['name'],val['stars']]) 

restaurant_display_list=sorted(restaurant_display_list, key = lambda x: x[1], reverse=True)     
for val in restaurant_display_list:
	print(val[0],val[1])



