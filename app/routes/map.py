from flask import Blueprint, jsonify
from app.mongo.reviews import Reviews
from app.ml.nlp import WordCloud
map_bp = Blueprint('map_api', __name__, url_prefix='/map')


@map_bp.route('/testing', methods=['GET'])
def testing():
    """API to generate word cloud

    Returns:
        json -- words with weights and
        sentiment color {'name':, 'weight':, 'color':}
    """
    reviews = Reviews()
    f = {'business_id': 'XKOAi4J47i-YEhhHfKkPRQ'}
    res = reviews.getReviews(f=f, cols={'text': 1, 'stars': 1})
    reviews, stars = [], []
    for each in res:
        reviews.append(each['text'])
        stars.append(each['stars'])

    cloud = WordCloud(docs=reviews, ratings=stars)
    word_count, word_color, word_sentiment = cloud.getCounter()

    resp = []
    for index, each in enumerate(word_count.most_common(50)):
        resp.append({
            'name': each[0],
            'weight': each[1],
            'color': word_color[each[0]],
            'sentiment': word_sentiment[each[0]]
        })

    return jsonify(resp), 200