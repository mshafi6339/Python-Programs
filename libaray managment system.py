
## **Program Structure**

### **Data Structures**

  #`Library.books`**: A **dictionary** where the key is the book title and the value is the `Book` object. This allows for fast O(1) lookups.
  #Library.members`**: A **dictionary** where the key is the member ID and the value is the `Member` object. This provides efficient access to member information.
  #`Member.borrowed_books`**: A **list** within each `Member` object to track the books they have currently borrowed.
  #`Book.history`**: A **list** within each `Book` object to store a history of borrowing events (who borrowed it and when).

### **Classes**

 #`Book`: Represents a book. It includes a `history` list to log borrowing events.
  #`Member`: Represents a library member with a unique ID, name, and a list of `borrowed_books`.
#  `Library`: The main class that manages the collections of `Book` and `Member` objects.
import datetime

class Book:
    """Represents a book with a title, author, and status."""
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.status = "available"
        self.history = []  # List to store borrowing history

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.status})"

class Member:
    """Represents a library member."""
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []  # List of book titles currently borrowed

    def __str__(self):
        return f"Member ID: {self.member_id}, Name: {self.name}"

class Library:
    """Manages the collection of books and members."""
    def __init__(self):
        self.books = {}  # Dictionary: {title: Book_object} for quick lookup
        self.members = {}  # Dictionary: {member_id: Member_object} for quick lookup
        self.next_member_id = 1

    def add_book(self, title, author):
        """Adds a new Book object to the library."""
        if title in self.books:
            print(f"Error: The book '{title}' already exists.")
        else:
            new_book = Book(title, author)
            self.books[title] = new_book
            print(f"Book added: {new_book}")

    def register_member(self, name):
        """Registers a new member with a unique ID."""
        member_id = self.next_member_id
        new_member = Member(member_id, name)
        self.members[member_id] = new_member
        self.next_member_id += 1
        print(f"Member '{name}' registered with ID: {member_id}")

    def display_all_books(self):
        """Displays all books in the library."""
        if not self.books:
            print("The library is currently empty.")
            return
        print("\n--- Current Library Collection ---")
        for book in self.books.values():
            print(book)
        print("----------------------------------\n")

    def display_all_members(self):
        """Displays all registered members."""
        if not self.members:
            print("No members are currently registered.")
            return
        print("\n--- Registered Members ---")
        for member in self.members.values():
            print(member)
        print("--------------------------\n")

    def search_book(self, title):
        """Searches for a book by its title."""
        book = self.books.get(title)
        if book:
            print("\n--- Book Found ---")
            print(f"Title: {book.title}")
            print(f"Author: {book.author}")
            print(f"Status: {book.status}")
            print(f"Borrowing History: {book.history}")
            print("------------------\n")
        else:
            print(f"Error: The book '{title}' is not found in the library.")

    def borrow_book(self, member_id, title):
        """Allows a member to borrow a book."""
        member = self.members.get(member_id)
        book = self.books.get(title)

        if not member:
            print(f"Error: Member with ID {member_id} not found.")
            return
        if not book:
            print(f"Error: Book '{title}' not found.")
            return
        
        if book.status == "available":
            book.status = "borrowed"
            borrow_info = {"member_id": member.member_id, "name": member.name, "date": datetime.date.today().isoformat()}
            book.history.append(borrow_info)
            member.borrowed_books.append(title)
            print(f"'{title}' has been successfully borrowed by {member.name}.")
        else:
            print(f"Error: '{title}' is currently unavailable.")

    def return_book(self, member_id, title):
        """Allows a member to return a book."""
        member = self.members.get(member_id)
        book = self.books.get(title)

        if not member:
            print(f"Error: Member with ID {member_id} not found.")
            return
        if not book:
            print(f"Error: Book '{title}' not found.")
            return

        if title in member.borrowed_books and book.status == "borrowed":
            book.status = "available"
            member.borrowed_books.remove(title)
            print(f"Thank you, {member.name}, for returning '{title}'.")
        else:
            print(f"Error: '{title}' was not borrowed by member ID {member_id}.")


def main():
    """Main function to run the library system's user interface."""
    library = Library()

    # Initial setup
    library.add_book("The Hobbit", "J.R.R. Tolkien")
    library.add_book("1984", "George Orwell")
    library.register_member("Alice")
    library.register_member("Bob")

    while True:
        print("\n===== Library Management System =====")
        print("1. Display all books")
        print("2. Display all members")
        print("3. Add a new book")
        print("4. Register a new member")
        print("5. Search for a book")
        print("6. Borrow a book")
        print("7. Return a book")
        print("8. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            library.display_all_books()
        elif choice == '2':
            library.display_all_members()
        elif choice == '3':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(title, author)
        elif choice == '4':
            name = input("Enter member's name: ")
            library.register_member(name)
        elif choice == '5':
            title = input("Enter the title of the book to search for: ")
            library.search_book(title)
        elif choice == '6':
            member_id = int(input("Enter member ID: "))
            title = input("Enter the title of the book to borrow: ")
            library.borrow_book(member_id, title)
        elif choice == '7':
            member_id = int(input("Enter member ID: "))
            title = input("Enter the title of the book to return: ")
            library.return_book(member_id, title)
        elif choice == '8':
            print("Thank you for using the Library Management System. Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
