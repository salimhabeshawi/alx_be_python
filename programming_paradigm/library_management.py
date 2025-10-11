class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        # each book instance should track its own check-out status
        self._is_checked_out = False

    def return_book(self):
        """Mark this book as returned (not checked out)."""
        self._is_checked_out = False


class Library:
    def __init__(self):
        # use an instance-level list to avoid shared mutable default across instances
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                book._is_checked_out = True

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                book._is_checked_out = False

    def list_available_books(self):
        for book in self._books:
            if not book._is_checked_out:
                print(f"{book.title} by {book.author}")
