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
    newbook = Book(title, pages, isbn, genre, author)
    return str(newbook)


# search for books by a given author
# serialization method for Book object
def serialize_book(book):
    return {
        "title": book.title,
        "pages": book.pages,
        "isbn": book.isbn,
        "genre": book.genre,
        "author": book.author
    }

@app.route('/search/<author>')
def search_author(author):
    books = Book.search(author)

    # convert the list of Book objects to a list of dictionaries
    books_data = [serialize_book(book) for book in books]

    # return json response
    return jsonify(books_data)

# # update books that have already been added (stretch goal)
# # @app.route('/update/<title>/<update_cat>/<new_value>')
# @app.route('/update/<title>/<update_cat>/<new_value>')
# def update(title, update_cat, new_value): 
#     print(update_cat) 
#     print(new_value) # update_cat, new_value
#     for book in Book.books:
#         if book.title == title:
#             book.update_cat = new_value
#             print(book.title)


#     abook = Book.title_search(title)
#     # print(title)
#     print(abook)
#     book_data = [serialize_book(book) for book in abook]
#     return jsonify(book_data)
# @app.route('/update/<title>/<update_cat>/<new_value>')
# def update(title, update_cat, new_value):
#     for book in Book.books:
#         if book.title == title:
#             book.update_book(update_cat, new_value)

#     abook = Book.title_search(title)
#     book_data = [serialize_book(book) for book in abook]
#     return jsonify(book_data)