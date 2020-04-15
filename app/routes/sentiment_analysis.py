from flask import Blueprint, jsonify
from app.mongo.reviews import Reviews
from app.ml.nlp import WordCloud


sentiment_analysis_bp = Blueprint('sentiment_analysis_api', __name__, url_prefix='/sentimentAnalysis')

@sentiment_analysis_bp.route('/testing',methods=['GET'])
def testing():
   value1 = [1,2.3,3.3,3.4,2.6,4,7]
   value2 = [1,3.2,3.2,2.3,4.3,5.5,6]
   value3 = [1,4,5,2,3,5.4,6]
   resp = []
   resp.append({'name' : 'Mexican' , 'data' : value1})
   resp.append({'name' : 'italian', 'data' : value2})
   resp.append({'name' : 'French' , 'data' : value3})
   print(resp)
   return jsonify(resp),200   #return the json response. Now the entire object is a list of python objects.