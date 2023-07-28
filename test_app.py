import pytest
from application import book
from application.book import Book

# test initialization of the Book class
def test_book_initialization():
    book = Book("title", 100, "978-3-16-148410-0", "genre", "author")
    assert book.title == "title"
    assert book.pages == 100
    assert book.isbn == "978-3-16-148410-0"
    assert book.genre == "genre"
    assert book.author == "author"

# test ISBN validation
def test_valid_isbn():
    valid_isbn = "978-3-16-148410-0"
    invalid_isbn = "123-456-789"

    assert Book.valid_isbn(valid_isbn) == True
    assert Book.valid_isbn(invalid_isbn) == False

# test search by author
def test_search_by_author():
    books_by_author = Book.search("F. Scott Fitzgerald")
    assert len(books_by_author) == 1
    assert books_by_author[0].title == "The Great Gatsby"

# test search by title
def test_search_by_title():
    book_by_title = Book.title_search("To Kill a Mockingbird")
    assert len(book_by_title) == 1
    assert book_by_title[0].author == "Harper Lee"

# test string representation
def test_str_representation():
    book = Book("1984", 328, "978-0451524935", "Science Fiction", "George Orwell")
    assert str(book) == "Written by George Orwell, 1984 is a gripping 328-page Science Fiction novel"