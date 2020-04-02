from pymongo import MongoClient
import pymongo

class YelpClient(object):
    def __init__(self):
        self.client = self.getClient()

    def getClient(self):
        return MongoClient('localhost', 27017)  

    def getCollection(self, coll_name):
        return self.client['yelp'][coll_name]
    
    def closeConnection(self):
        self.client.close()


