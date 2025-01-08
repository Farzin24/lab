class Publisher:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Publisher Name: {self.name}")

class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)  # Call to base class constructor
        self.title = title
        self.author = author

    def display(self):
        super().display()  # Call to base class method
        print(f"Book Title: {self.title}")
        print(f"Author: {self.author}")

class Python(Book):
    def __init__(self, name, title, author, price, no_of_pages):
        super().__init__(name, title, author)  # Call to parent class constructor
        self.price = price
        self.no_of_pages = no_of_pages

    def display(self):
        super().display()  # Call to parent class method
        print(f"Price: ₹{self.price}")
        print(f"Number of Pages: {self.no_of_pages}")

# Taking user input
publisher_name = input("Enter publisher name: ")
book_title = input("Enter book title: ")
book_author = input("Enter book author: ")
book_price = float(input("Enter book price: "))
book_pages = int(input("Enter number of pages: "))

# Create a Python book object
python_book = Python(publisher_name, book_title, book_author, book_price, book_pages)

# Display book details
print("\nPython Book Details:")
python_book.display()

