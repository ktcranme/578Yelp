from pymongo import MongoClient
import pymongo

class YelpMongo(object):
    def __init__(self):
        self.client = self.getClient()

    def getClient(self):
        return MongoClient('localhost', 27017)

    def getCollection(self, coll_name):
        return self.client['yelp'][coll_name]
    
    def getReviews(self, date_filter={}):
        return self.getCollection('reviews').find(
            {'date': date_filter},
            {'user': 0, '_id': 0} 
        )
    
    def closeConnection(self):
        self.client.close()



