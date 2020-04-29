from flask import Blueprint, jsonify, request
from app.mongo.business import Business
from app.mongo.checkins import Checkins
from datetime import datetime
from scipy.spatial import distance
import pickle
import numpy as np

business_db = Business()


recommender_bp = Blueprint(
    'recommender_api', __name__, url_prefix='/recommender')

@recommender_bp.route('/testing', methods=['GET'])
def recommender_entry():
    categories = request.args.get('categories')
    print("In recommender api, categories : " , categories)
    print(type(categories))

##call recommender here and store data in this variable.
    # resp = [{
    #     'name': "Domino's Pizza",
    #     'business_id' : '1tUUCVKiFRfocWjKJgL3Gg',
    #     'latitude' : 50.9324294753,
    #     'longitude' : -113.9830968356,
    #     'stars' : 1.5 
    # }]
    inter = recommender()
    resp = []
    for val in inter:
        inter_dict = {'name':val[0], 'business_id':val[4], 'latitude':val[2], 'longitude' : val[3], 'stars':val[1]}
        resp.append(inter_dict)


    print("Returning json response..")
    print(resp)
    return jsonify(resp), 200

def recommender():
    with open('data2.p', 'rb') as fp:
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
			    restaurant_display_list.append([val['name'],val['stars'],val['latitude'],val['longitude'],val['business_id']]) 

    restaurant_display_list=sorted(restaurant_display_list, key = lambda x: x[1], reverse=True)  
    return restaurant_display_list   
    # for val in restaurant_display_list:
	   #  print(val[0],val[1])