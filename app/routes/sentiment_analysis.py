from flask import Blueprint, jsonify
from app.mongo.reviews import Reviews
from app.mongo.business import Business
from app.ml.nlp import WordCloud
import time
import pandas as pd
import numpy as np

sentiment_analysis_bp = Blueprint('sentiment_analysis_api', __name__, url_prefix='/sentimentAnalysis')

@sentiment_analysis_bp.route('/testing',methods=['GET'])
def testing():
   start = time.time()

##let's get data for a single restaurant and simply display it out first
   businesses = Business()
   reviews = Reviews()

   restaurant_list = ["Firehouse Subs"]
 #  ["Dirty South","Chipotle Mexican Grill","Eddie V's Prime Seafood","Firehouse Subs","Flower Child","Wonton Chai Noodle"]
   response = []
   for r in restaurant_list:
      response.append(getScore(businesses, reviews, r))
   
   print("TIME TAKEN : ",time.time()-start)
   return jsonify(response),200

def getScore(businesses, reviews, target_name):   
#   print("getting business..")

##get the restaurant to obtain its business id.
   restaurant = businesses.getBusiness(f={'name' : target_name})
   business_info = restaurant[0]
#   print("getting reviews..")

##get all reviews for that restaurant using its business_id
   res = reviews.getReviews(f={'business_id' : business_info['business_id']})
#   print("Number of reviews : " , len(res))

   total_score = {}
   num_reviews = {}
   avg_score = {}

##collect for all years
   for y in range(2010,2020):
      total_score[y] = 0
      num_reviews[y] = 0
      avg_score[y] = 0

   for r in res:
  #    print(r)
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

   for y in range(2010,2020):
   #   print("\n\n")
   #   print("YEAR : " , y)
   #   print("TOTAL SCORE : " , total_score[y])

      avg_score = total_score[y]
      if num_reviews[y] != 0:
         avg_score = total_score[y]/num_reviews[y]
      
      data.append(avg_score)
   #   print("AVERAGE SCORE : " , avg_score)

   result = {'name' : target_name, 'data' : data}
   return result