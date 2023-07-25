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
    def __init__(self, title, pages, isbn, genre, author = "Unknown"):
        ...
    
    @staticmethod
    def valid_isbn(isbn):
        ...
    
    @staticmethod
    def search(author):
        ...

    def __str__(self):
        ...


