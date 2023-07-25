from book import Book

def test_setup():
    with open("test.books.list", 'w') as f:
        pass
    Book("Sample text", 300, "123-4-56-789012-3", "Fantasy", author="Alice Jones", bookfile="test.books.list")
    Book("Generic title", 125, "321-4-57-787812-3", "Biography", author="John Smith", bookfile="test.books.list")
    Book("Sample text 2", 254, "213-5-46-779812-3", "Fantasy", author="Alice Jones", bookfile="test.books.list")
    Book.books = []
    Book.initialise_list('test.books.list')


def test_search_method():
    assert list(map(lambda x: x.title, Book.search("Alice Jones"))) == ["Sample text", "Sample text 2"]
    assert list(map(lambda x: x.title, Book.search("John Smith"))) == ["Generic title"]
    assert Book.search("not a real author") == []

def test_isbn_checker():
    assert Book.valid_isbn("978-0-00-821843-0")
    assert not Book.valid_isbn("978-0-00-821843-1")