from app.mongo.yelp_client import YelpClient
import pymongo


class Checkins(YelpClient):
    def __init__(self):
        super().__init__()

    def getCheckins(self, f={}, cols={}):
        """Query reviews with filters and columns 

        Keyword Arguments:
            f {dict} -- filters to apply (default: {{}})
            cols {dict} -- cols to exclude/include (default: {{}})

        Returns:
            cur -- query cursor
        """
        cols['_id'] = 0
        res = list(self.getCollection('checkins').find(
            f,
            cols
        ))
        self.closeConnection()
        return res