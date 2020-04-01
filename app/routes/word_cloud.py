from flask import Blueprint
from app.query import YelpMongo

word_cloud_bp = Blueprint('word_cloud_api', __name__, url_prefix='/wordCloud')

@word_cloud_bp.route('/testing', methods=['GET'])
def testing():
    k = YelpMongo()
    f = {}
    f['date'] = {"$gte" : "2015-01-01 00:00:00" , "$lte" : "2015-01-01 01:00:00"}
    res = list(k.getReviews(f=f))
    k.closeConnection()
    return str(res[:20]), 200
    