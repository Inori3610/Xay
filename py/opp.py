class Book:
    # Initialize a list to store books directly in the class
    books = []

    def __init__(self, id, title, author, year):
        self.id = id
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Book ID : {self.id} Title :'{self.title}' by {self.author}, published in {self.year}"

    @classmethod
    def setinfo(cls, id, title, author, year):
        # Create a new book object and add it to the books list
        new_book = Book(id, title, author, year)
        cls.books.append(new_book)
        print ("----------------------------------------------------")
        print(f"Book added: {new_book}")

    @classmethod
    def show_books(cls):
        if not cls.books:
            print("The library is empty!")
        else:
            print("----------------------------------------------------")
            print("Books in the collection:")
            for book in cls.books:
                print(book)

# Example usage
Book.setinfo("STE01", "Stranger in the Rainy Day", "Steve Wakin", 2004)
Book.setinfo("STE02", "Mystery of the Hidden Path", "John Doe", 2012)
Book.setinfo("DF01", "How to live in this world", "Van Dice",1993)
Book.show_books()
