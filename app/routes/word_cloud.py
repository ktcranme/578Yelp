from flask import Blueprint, jsonify, request
from app.mongo.reviews import Reviews
from app.mongo.business import Business
from app.ml.nlp import WordCloud
word_cloud_bp = Blueprint('word_cloud_api', __name__, url_prefix='/wordCloud')


@word_cloud_bp.route('/testing', methods=['GET'])
def testing():
    """API to generate word cloud

    Returns:
        json -- words with weights and
        sentiment color {'name':, 'weight':, 'color':}
    """
    business_id = request.args.get('business_id')
    business = Business()
    business_details = list(business.getBusiness(
        {'business_id': business_id}, {'name': 1}))
    business_name = business_details[0]['name'] if business_details else 'None'

    reviews = Reviews()
    f = {'business_id': business_id}
    res = reviews.getReviews(f=f, cols={'text': 1, 'stars': 1})
    reviews, stars = [], []
    for each in res:
        reviews.append(each['text'])
        stars.append(each['stars'])

    cloud = WordCloud(docs=reviews, ratings=stars)
    word_count, word_color, word_sentiment = cloud.getCounter()

    resp = []
    for index, each in enumerate(word_count.most_common(50)):
        word = each[0]
        resp.append({
            'name': word,
            'weight': each[1],
            'color': word_color[word],
            'sentiment': word_sentiment[word]
        })

    return jsonify({'data': resp, 'name': business_name}), 200
