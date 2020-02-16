import os

from pymongo import MongoClient


mongo_url = os.getenv('MONGO_URL')
if not mongo_url:
    raise RuntimeError('MongoDB URL (MONGO_URL) environment variable was not set.')

client = MongoClient(mongo_url)


class MongoDAO:
    """DAO for MongoDB

    """
    def __init__(self, database_name='librarydatabase'):

        self.db = client[database_name]

    def search_by_id(self, collection, entry_id):
        """

        Args:
            collection (str): Collection to search
            entry_id (str): Specific id to be find in collection

        Returns:
            dict: Dictionary with parameters of the entry with specified id code
        """

        return self.db[collection].find_one({'id': entry_id})
