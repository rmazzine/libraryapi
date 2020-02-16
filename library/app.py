"""This is the server configuration script

"""
from flask import Flask

from library.operations.db_operations import Search

search_op = Search()

app = Flask(__name__)


@app.route('/book/<id_book>')
def find_book_by_id(id_book):
    """ Gets a book code from URL and returns a JSON with info about it

    Args:
        id_book (str): A code to locate a book
    """

    json_data = search_op.find_by_id('books', id_book)

    print(json_data)

    response = app.response_class(
        response=json_data,
        status=200,
        mimetype='application/json'
    )

    return response
