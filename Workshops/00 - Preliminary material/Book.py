class Book:
    """
    A class representing a book.
    """

    def __init__(self, title, author, year, price):
        """
        Initialize the attributes of the class.
        Params:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The year the book was published.
            price (float): The price of the book, in £.
        """

        self.title = title
        self.author = author
        self.year = year
        self.price = price

    def print_info(self):
        """
        ​Prints information about the book.
        ​"""
        # The .2f format specifier formats
        # a float to 2 decimal places.
        print(f"{self.title} by {self.author}, {self.year}. Price £{self.price:.2f}")


class Bookshop:
    """
    A class representing a bookshop.
    """

    def __init__(self, name):
        """
        Initialize the attributes of the class.
        Params:
            name (str): The name of the bookshop.
        """

        self.name = name
        self.books = []

    def add_book(self, book):
        """
        Add a book to the bookshop.
        Params:
            book (Book): The book to add.
        """

        self.books.append(book)

    def remove_book(self, book):
        """
        Remove a book from the bookshop.
        Params:
            book (Book): The book to remove.
        """

        self.books.remove(book)


bookshop = Bookshop("Books for everyone")
bookshop.add_book(Book("Moby Dick", "Herman Melville", "1851", 20.50))
bookshop.add_book(
    Book("The Great Gatsby", "F. Scott Fitzgerald", "1925", 15.0))
bookshop.add_book(Book("The Hobbit", "J. R. R. Tolkien", "1937", 10.0))

for book in bookshop.books:
    book.print_info()