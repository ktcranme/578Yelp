from flask import Blueprint, jsonify
from app.mongo.reviews import Reviews
from app.ml.nlp import WordCloud


word_cloud_bp = Blueprint('word_cloud_api', __name__, url_prefix='/wordCloud')

@word_cloud_bp.route('/testing', methods=['GET'])
def testing():
    # fetch all data
    reviews = Reviews()
    f = {}
    f['date'] = {"$gte" : "2015-01-01 00:00:00" , "$lte" : "2015-01-01 1:00:00"}
    res = reviews.getReviews(f=f)
    res = [each['text'] for each in res]

    # fetch word frequency
    cloud = WordCloud(res)
    word_frequencies = cloud.getCounter()

    # transform
    resp = []
    for each in word_frequencies.most_common(35):
        resp.append({'name': each[0], 'weight': each[1], 'sentimentScore': 0.7212508438888889})

    return jsonify(resp), 200
    