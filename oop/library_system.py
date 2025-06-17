# File: library_system.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        print(f"Initializing Book: {self.title} by {self.author}")

    def get_info(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size
        print(f"Initializing EBook: {self.title} by {self.author}, File Size: {self.file_size}KB")

    def get_info(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count
        print(f"Initializing PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}")

    def get_info(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        self.books = []
        print("Library initialized.")

    def add_book(self, book):
        print(f"Adding book: {book.title}")
        self.books.append(book)

    def list_books(self):
        print("Listing all books in the library:")
        for book in self.books:
            print(book.get_info())
