from flask import Blueprint, jsonify, request
from app.mongo.reviews import Reviews
from app.mongo.business import Business
import time

sentiment_analysis_bp = Blueprint(
    'sentiment_analysis_api', __name__, url_prefix='/sentimentAnalysis')


@sentiment_analysis_bp.route('/testing', methods=['GET'])
def testing():
    start = time.time()
    business_id = request.args.get('business_id')
    print("Business id is : " , business_id)
# let's get data for a single restaurant and simply display it out first

    reviews = Reviews()
    business = Business()
    response = []
    response.append(getScore(reviews, business, business_id))

    print("TIME TAKEN : ", time.time()-start)
    return jsonify(response), 200


def getScore(reviews, business, business_id):
    #   print("getting business..")

# get all reviews for that restaurant using its business_id
    name = business.getBusiness(f={'business_id' : business_id})[0]['name']
    print("Data taken from the business table : ", name)
    res = reviews.getReviews(f={'business_id': business_id})
    print("Restaurant name : " , name)

    total_score = {}
    num_reviews = {}
    avg_score = {}

# collect for all years
    for y in range(2010, 2020):
        total_score[y] = 0
        num_reviews[y] = 0
        avg_score[y] = 0

    for r in res:
        # print(r)
        year = int(r['date'][:4])
        if year not in total_score:
            total_score[year] = r['stars']
            avg_score[year] = 0
            num_reviews[year] = 1
            continue
        total_score[year] += r['stars']
        num_reviews[year] += 1
    #   print("\n\n")

    data = []

    for y in range(2010, 2020):
        #   print("\n\n")
        #   print("YEAR : " , y)
        #   print("TOTAL SCORE : " , total_score[y])
        avg_score = total_score[y]
        if num_reviews[y] != 0:
            avg_score = total_score[y]/num_reviews[y]

        data.append(avg_score)
    #   print("AVERAGE SCORE : " , avg_score)

    result = {'name': name, 'data': data}
    return result
