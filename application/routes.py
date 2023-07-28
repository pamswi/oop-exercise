from application import app

from flask import jsonify
from application import book
from application.book import Book

@app.route('/')
def index():
    return "hello world"


# add new books with information supplied via url/query params
@app.route('/add/<title>/<pages>/<isbn>/<genre>/<author>')
def add(title, pages, isbn, genre, author):
    '''
    the add function takes a number of inputs and uses Book object to initiate a new book object
    '''
    newbook = Book(title, pages, isbn, genre, author)
    return str(newbook)


# search for books by a given author
# serialization method for Book object
def serialize_book(book):
    '''
    serialise_book function takes a book data and translates it into json
    '''
    return {
        "title": book.title,
        "pages": book.pages,
        "isbn": book.isbn,
        "genre": book.genre,
        "author": book.author
    }

@app.route('/search/<author>')
def search_author(author):
    '''
    search_author function takes an author as an input, looks up books by given author and returns json data on all of the books
    '''
    books = Book.search(author)

    # convert the list of Book objects to a list of dictionaries
    books_data = [serialize_book(book) for book in books]

    # return json response
    return jsonify(books_data)
