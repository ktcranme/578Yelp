import pymongo
from app.mongo.yelp_client import YelpClient
from app.mongo.business import Business
from app.mongo.reviews import Reviews
import json
import sys

#cluster = MongoClient("mongodb+srv://sid:siddharth23@cluster0-itfnh.mongodb.net/test?retryWrites=true&w=majority")
#db = cluster["yelp"]
#collection = db["reviews"]
business_db = Business()
print("starting..")
#reviews = review_db.getBusiness()
restaurants = business_db.getRestaurants()
print("done")
print(restaurants[:10])
out = open("restaurants.json", "w", encoding="utf-8")
business_ids = set()
for r in restaurants:
    business_ids.add(r['business_id'])
    out.write(str(r))
    out.write("\n")
out.close()
print("Added all business ids to the set : It is now...")
print(len(business_ids))

reviews_db = Reviews()
out = open("restaurant_reviews.json", "w")
print("Now collecting reviews...")
reviews = reviews_db.getReviews()

print("done!")
for review in reviews:
    json_object = json.dumps(review)
    if review['business_id'] in business_ids:
        print("Writing review : " + str(json_object) + " to the reviews file")
        out.write(json_object)
        out.write("\n")
    else:
        print("\n\nThe review : " + str(json_object) +
              " is not a restaurant review\n\n")

print("Done writing the reviews! Please open up the file restaurant_reviews.json in this directory")
sys.exit(0)

#print("connection successful")
# print(client.list_database_names())
