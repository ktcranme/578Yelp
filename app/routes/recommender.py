from flask import Blueprint, jsonify, request
from app.mongo.business import Business
from app.mongo.checkins import Checkins
from datetime import datetime
from scipy.spatial.distance import euclidean
import pickle
import numpy as np

recommender_bp = Blueprint(
    'recommender_api', __name__, url_prefix='/recommender')

@recommender_bp.route('/testing', methods=['POST'])
def recommender_entry():
    post_data = request.get_json()
    category_list = post_data['category_list']
    lat = post_data['lat']
    long = post_data['long']
    map_center = np.array([float(lat),float(long)])
    inter = recommender(category_list, map_center)
    resp = []
    for val in inter:
        inter_dict = {
            'name': val[0],
            'business_id': val[4],
            'latitude': val[2],
            'longitude': val[3],
            'stars': val[1]
        }
        resp.append(inter_dict)
    return jsonify(resp), 200


def recommender(category_list, map_center):
    business_db = Business()
    with open('app/static/data2.p', 'rb') as fp:
        data_vector_dictionary = pickle.load(fp)
    with open('app/static/cat_to_bid.p', 'rb') as fp:
        cat_to_bid = pickle.load(fp)

    input_array = np.array(
        [0] * len(data_vector_dictionary['pQeaRpvuhoEqudo3uymHIQ']))

    #get business_ids and lat,lng belonging to selected categories only
    bid_to_latlong = {}
    for category in category_list: 
        for bid_to_coord in cat_to_bid[category]:
            business_id = bid_to_coord['business_id']
            coordinates = bid_to_coord['coordinates']
            bid_to_latlong[business_id] = coordinates
    valid_business_ids = bid_to_latlong.keys()

    #prune data dictionary to use only filtered businesses
    data_vector_dictionary = {
        key: val
        for key, val in data_vector_dictionary.items()
        if key in valid_business_ids
    }

    with open("app/static/restaurant_categories.txt", "rb") as fp:
        b = pickle.load(fp)
    distinct_categories = b[722:]

    category_map = {}
    for i in range(0, len(distinct_categories)):
        category_map[distinct_categories[i]] = i

    for cat in category_list:
        input_array[category_map[cat]] = 1

    topk = 10
    restaurant_display_list = []
    dist_list = []

    # multiple vector dist with map distance to get best closest restaurants
    for key in data_vector_dictionary:
        dist_from_center = euclidean(map_center, bid_to_latlong[key])
        dist_from_category = euclidean(input_array, data_vector_dictionary[key])
        d = dist_from_center * dist_from_category
        dist_list.append([key, d])
    dist_list.sort(key=lambda x: x[1])
    dist_list = dist_list[:10]

    #get all business details of top restaurant for response
    topRestaurants = business_db.getBusiness(
        f={'business_id': {
            '$in': [each[0] for each in dist_list]
        }}, )
    topRestaurants = {
        restaurant['business_id']: restaurant
        for restaurant in topRestaurants
    }

    #prepare response
    for each in dist_list:
        restaurant = topRestaurants[each[0]]
        restaurant_display_list.append([
            restaurant['name'], restaurant['stars'], restaurant['latitude'],
            restaurant['longitude'], restaurant['business_id']
        ])

    restaurant_display_list = sorted(restaurant_display_list, key=lambda x: x[1], reverse=True)
    return restaurant_display_list
