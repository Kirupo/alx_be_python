# File: main.py

from library_system import Book, EBook, PrintBook, Library

def main():
    my_library = Library()

    # Create instances
    book1 = Book("Pride and Prejudice", "Jane Austen")
    ebook1 = EBook("Snow Crash", "Neal Stephenson", 500)
    printbook1 = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add to library
    my_library.add_book(book1)
    my_library.add_book(ebook1)
    my_library.add_book(printbook1)

    # List all books
    my_library.list_books()

if __name__ == "__main__":
    main()
