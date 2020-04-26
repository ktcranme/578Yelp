from flask import Blueprint, jsonify
import pandas
map_bp = Blueprint('map_api', __name__, url_prefix='/mappath')


@map_bp.route('/testing', methods=['GET'])
def testing():
    businesses = []
    with open('app/static/assets/mapData/2010data.csv') as f:
        for line in f:
            businesses.append(line.split(','))
    return jsonify(businesses), 200
