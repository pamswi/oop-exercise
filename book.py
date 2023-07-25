'''
Create a class Book. Each book object should have the attributes: 
- title
- author (default unknown) 
- number of pages
- genre
- ISBN. 
The class should define the following methods:
- __init__ to set the attributes described above
- __str__ to print a description of the book
- a search method which returns all books by a given author (requires tracking of objects) - if there are no books by the given author return an empty list
- a method to check the validity of a given ISBN-13 - should return true if the ISBN is valid, false otherwise
As an additional stretch goal, create 2 subclasses for specific 
genres and override the __init__ method and __str__ methods appropriately
'''

class Book():
    books = []
    def __init__(self, title, pages, isbn, genre, author = "Unknown"):
        self.title = title
        self.pages = pages
        self.isbn = isbn
        self.genre = genre
        self.author = author
        Book.books.append(self)
    
    @staticmethod
    def valid_isbn(isbn):
        digits = ''.join(isbn.split('-'))
        if len(digits) != 13:
            return False
        diglist = [int(digit) for digit in digits]
        return ((sum([diglist[i] for i in range(12) if i % 2 == 0]) + 3 * sum([diglist[i] for i in range(12) if i % 2 != 0]) + diglist[-1]) % 10) == 0
    
    @staticmethod
    def search(author):
        return list(filter(lambda book: book.author == author, Book.books))

    def __str__(self):
        return f"Written by {self.author}, {self.title} is a gripping {self.pages}-page {self.genre} novel"


