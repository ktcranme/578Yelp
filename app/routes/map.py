from flask import Blueprint, jsonify
import pandas
from app.mongo.business import Business
map_bp = Blueprint('map_api', __name__, url_prefix='/mappath')


@map_bp.route('/testing', methods=['GET'])
def testing():
    businesses = Business()
    bArr = []
    bs = businesses.getBusiness()
    for b in bs:
        bArr.append([b['business_id'], b['name'], b['latitude'], b['longitude'], b['stars'], b['review_count'], b['address']])
    return jsonify(bArr), 200
