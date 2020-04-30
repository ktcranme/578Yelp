from flask import Blueprint, jsonify, request
from app.mongo.business import Business
from app.mongo.checkins import Checkins
from datetime import datetime
from scipy.spatial import distance
import pickle
import numpy as np

recommender_bp = Blueprint(
    'recommender_api', __name__, url_prefix='/recommender')

@recommender_bp.route('/testing', methods=['GET'])
def recommender_entry():
    categories = request.args.get('categories')    
    category_list = [c for c in categories.split(',')]
    inter = recommender(category_list)
    resp = []
    for val in inter:
        inter_dict = {'name':val[0], 'business_id':val[4], 'latitude':val[2], 'longitude' : val[3], 'stars':val[1]}
        resp.append(inter_dict)
    return jsonify(resp), 200

def recommender(category_list):
    business_db = Business()
    with open('app/static/data2.p', 'rb') as fp:
        data_vector_dictionary = pickle.load(fp)
    input_array = np.array([0] * len(data_vector_dictionary['pQeaRpvuhoEqudo3uymHIQ']))

    with open("restaurant_categories.txt", "rb") as fp:
	      b = pickle.load(fp)
    distinct_categories = b[722:]

    category_map = {}
    for i in range(0,len(distinct_categories)):
       category_map[distinct_categories[i]] = i

    for cat in category_list:
       input_array[category_map[cat]] = 1

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
			    restaurant_display_list.append([val['name'],val['stars'],val['latitude'],val['longitude'],val['business_id']]) 

    restaurant_display_list=sorted(restaurant_display_list, key = lambda x: x[1], reverse=True)  
    return restaurant_display_list   