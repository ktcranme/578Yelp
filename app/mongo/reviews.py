from app.mongo.yelp_client import YelpClient

class Reviews(YelpClient):
    def __init__(self):
        super().__init__()
    
    def getReviews(self, f={}, cols={}):
        cols['_id'] = 0
        res = list(self.getCollection('reviews').find(
            f,
            cols
        ))
        self.closeConnection()
        return res

    



    
    
