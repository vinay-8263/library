class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def display_books(self):
        if len(self.books) == 0:
            print("No books in the library.")
        else:
            print("Book Catalog:")
            for book in self.books:
                availability = "Available" if book.available else "Not Available"
                print(f"Title: {book.title} | Author: {book.author} | ISBN: {book.isbn} | {availability}")

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Display Books")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            book = Book(title, author, isbn)
            library.add_book(book)
            print("Book added successfully.")

        elif choice == "2":
            title = input("Enter book title to search: ")
            book = library.search_book(title)
            if book:
                availability = "Available" if book.available else "Not Available"
                print(f"Title: {book.title} | Author: {book.author} | ISBN: {book.isbn} | {availability}")
            else:
                print("Book not found.")

        elif choice == "3":
            library.display_books()

        elif choice == "4":
            print("Thank you for using the Library Management System. Goodbye!")
            print("coded and develepoed by I.Vinay Datta")
            break

        else:
            print("Invalid choice. Please try again.")
            print("coded and develepoed by I.Vinay Datta")

if __name__ == "__main__":
    main()

