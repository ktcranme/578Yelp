import sys
sys.path.append('../..')
import pymongo
# from app.mongo.yelp_client import YelpClient
from app.mongo.business import Business
from app.mongo.reviews import Reviews
import numpy as np
import copy
from scipy.spatial import distance
import pickle

business_db = Business()
restaurants = business_db.getBusiness()
distinct_categories = []

with open("app/static/restaurant_categories.txt", "rb") as fp:
	b = pickle.load(fp)
distinct_categories = b[722:]

def get_distinct_categories():
	for val in restaurants:
		print(val['business_id'])
		category_string = val['categories']
		category_list = category_string.split(',')
		for item in category_list:
			if item.strip() not in distinct_categories:
				distinct_categories.append(item.strip())


def create_restaurant_vectors():
	restaurant_dict = {}
	for val in restaurants:
		category_string = val['categories']
		inter_category_list = category_string.split(',')
		category_list = [x.strip() for x in inter_category_list]
		vec = []
		for category in distinct_categories:
			if category in category_list:
				vec.append(1)
			else: 
				vec.append(0)

		bid = val['business_id']	
		restaurant_dict[bid] = np.array(vec)
	return restaurant_dict

data_vector_dictionary = create_restaurant_vectors()
with open('app/static/data2.p', 'wb') as fp:
    pickle.dump(data_vector_dictionary, fp, protocol=pickle.HIGHEST_PROTOCOL)

array = np.array([0] * len(data_vector_dictionary['pQeaRpvuhoEqudo3uymHIQ']))
dist_list = []
for key in data_vector_dictionary:
	d = distance.euclidean(array, data_vector_dictionary[key])
	dist_list.append([key,d])
dist_list.sort(key=lambda x: x[1])
dist_list=sorted(dist_list, key = lambda x: x[1])     



