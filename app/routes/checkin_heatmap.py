from flask import Blueprint, jsonify
from app.mongo.business import Business
from app.mongo.checkins import Checkins
from datetime import datetime

checkin_heatmap_bp = Blueprint(
    'checkin_heatmap_api', __name__, url_prefix='/checkinHeatmap')


def generateResult(heat_map):
    result = []
    for y in range(0, 10):
        for m in range(0, 12):
            if(heat_map[y][m] != 0):
                result.append([y, m, heat_map[y][m]])

    return result


def genHeatMap(checkin_dates):
    months = 12
    years = 10
    heat_map = [[0 for i in range(months)] for j in range(years)]
    for date in checkin_dates.split(','):
        # print("Working on date : " + date)
        datetime_obj = datetime.strptime(date.strip(), '%Y-%m-%d %H:%M:%S')
        month_index = datetime_obj.month-1  # 0 for Jan, 1 for Feb and so on...
        # 0 for 2010, 1 for 2011 and so on...
        year_index = datetime_obj.year-2010
        heat_map[year_index][month_index] += 1
        # print("year ", year_index, " month ", month_index, "\n")
    return heat_map


@checkin_heatmap_bp.route('/testing', methods=['GET'])
def testing():
    resp = []
    target_name = "Starbucks"
    address = "3950 Las Vegas Blvd So"

    # get the business id from rest name
    restaurant = Business().getBusiness(
        f={'name': target_name, 'address': "3950 Las Vegas Blvd So"})
    business_id = restaurant[0]['business_id']

    print("business id : ", business_id)

    # get the checkins data from business id
    checkins = Checkins()
    checkins_data = checkins.getCheckins({'business_id': business_id})

    # months start from 0-11, 0 for jan, 1 for feb and so on...
    # years start from 0-9, 0 for 2010, 1 for 2011, 2 for 2012 and so on...
    years = 10
    months = 12

    checkin_dates = checkins_data[0]['date']
    heat_map = genHeatMap(checkin_dates)

    result = generateResult(heat_map)

    resp = {
        'name': target_name,
        'heat_map': result
    }

    print("Returning json response..")
    # print(resp)
    return jsonify(resp), 200
