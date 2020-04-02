from app.mongo.yelp_client import YelpClient

class Reviews(YelpClient):
    def __init__(self):
        super().__init__()
    
    def getReviews(self, f={}):
        res = list(self.getCollection('reviews').find(
            f,
            {'_id':0, 'user_id': 0}
        ))
        self.closeConnection()
        return res



    



    
    
