from library.search.mongo_dao import MongoDAO
from library.utils.output_model import simple_output

db = MongoDAO()


class Search:

    def find_by_id(self, collection, book_id):

        return simple_output(db.search_by_id(collection, book_id))
