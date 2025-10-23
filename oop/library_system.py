class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"Book('{self.title}', '{self.author}')"

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

class Library:
    books = []

    def add_book(self, book):
        self.books.append(book)
    
    def list_books(self):
        print(f"Book: {self.books[0].title} by {self.books[0].author}")
        print(f"EBook: {self.books[1].title} by {self.books[1].author}, File Size: {self.books[1].file_size}")
        print(f"Book: {self.books[2].title} by {self.books[2].author}, Page Count: {self.books[2].page_count}")