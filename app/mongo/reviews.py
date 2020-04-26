from app.mongo.yelp_client import YelpClient


class Reviews(YelpClient):
    def __init__(self):
        super().__init__()

    def getReviews(self, f={}, cols={}):
        """Query reviews with filters and columns 

        Keyword Arguments:
            f {dict} -- filters to apply (default: {{}})
            cols {dict} -- cols to exclude/include (default: {{}})

        Returns:
            cur -- query cursor
        """
        cols['_id'] = 0
        res = list(self.getCollection('reviews').find(
            f,
            cols
        ))  # .sort('date',pymongo.ASCENDING)
        self.closeConnection()
        return res
