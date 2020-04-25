from flask import Blueprint, jsonify
import pandas
map_bp = Blueprint('map_api', __name__, url_prefix='/mappath')


@map_bp.route('/testing', methods=['GET'])
def testing():
    with open('../static/assets/mapData/2010data.csv') as f:
        for line in f:
            print(line)
            return jsonify(line), 200
