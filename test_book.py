from book import Book

def test_search_method():
    book1 = Book("Sample text", 300, "123-4-56-789012-3", "Fantasy", "Alice Jones")
    book2 = Book("Generic title", 125, "321-4-57-787812-3", "Biography", "John Smith")
    book3 = Book("Sample text 2", 254, "213-5-46-779812-3", "Fantasy", "Alice Jones")
    assert Book.search("Alice Jones") == [book1, book3]
    assert Book.search("John Smith") == [book2]
    assert Book.search("not a real author") == []

def test_isbn_checker():
    assert Book.valid_isbn("978-0-00-821843-0")
    assert not Book.valid_isbn("978-0-00-821843-1")