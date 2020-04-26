from app.mongo.yelp_client import YelpClient


class Business(YelpClient):
    def __init__(self):
        super().__init__()

    def getBusiness(self, f={}, cols={'user': 0, '_id': 0}):
        """query business with filters and columns

        Keyword Arguments:
            f {dict} -- filters to apply (default: {{}})
            cols {dict} -- cols to include/exclude (default: {{'user': 0, '_id': 0}})

        Returns:
            cursore -- query cursor
        """
        res = list(self.getCollection('business').find(
            f,
            cols
        ))
        self.closeConnection()
        return res

    def getCategories(self, f={}):
        res = list(self.getCollection('business').distinct("categories"))    
        self.closeConnection()
        return res