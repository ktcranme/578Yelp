from app.mongo.yelp_client import YelpClient

class Business(YelpClient):
    def __init__(self):
        super().__init__()
    
    def getBusiness(self, f={}):
        res = list(self.getCollection('business').find(
            f,
            {'user': 0, '_id': 0} 
        ))
        self.closeConnection()
        return res
    
