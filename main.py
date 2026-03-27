import json

# ---------- File Handling ----------
def load_library():
    try:
        with open("library.json", "r") as file:
            return json.load(file)
    except:
        return []

def save_library(library):
    with open("library.json", "w") as file:
        json.dump(library, file, indent=4)

# ---------- Core Functions ----------
def add_book(library):
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    genre = input("Enter genre: ")

    book = {
        "title": title,
        "author": author,
        "genre": genre,
        "available": True
    }

    library.append(book)
    save_library(library)
    print("Book added successfully.")

def show_books(library):
    if not library:
        print("Library is empty.")
        return

    print("\n--- Library Books ---")
    for i, book in enumerate(library):
        status = "Available" if book["available"] else "Borrowed"
        print(f"{i+1}. {book['title']} by {book['author']} ({book['genre']}) - {status}")

def borrow_book(library, history):
    show_books(library)
    try:
        choice = int(input("Enter book number to borrow: ")) - 1
        if library[choice]["available"]:
            library[choice]["available"] = False
            history.append(library[choice])
            save_library(library)
            print("Book borrowed successfully.")
        else:
            print("Book is already borrowed.")
    except:
        print("Invalid selection.")

def return_book(library):
    title = input("Enter book title to return: ").lower()

    for book in library:
        if book["title"].lower() == title:
            if not book["available"]:
                book["available"] = True
                save_library(library)
                print("Book returned successfully.")
                return
            else:
                print("This book was not borrowed.")
                return

    print("Book not found.")

def recommend_books(library, history):
    if not history:
        print("No borrowing history yet.")
        return

    last_genre = history[-1]["genre"]
    print(f"\nRecommended books based on genre '{last_genre}':")

    found = False
    for book in library:
        if book["genre"] == last_genre and book["available"]:
            print(f"- {book['title']} by {book['author']}")
            found = True

    if not found:
        print("No recommendations available.")

# ---------- Main Menu ----------
def main():
    library = load_library()
    borrow_history = []

    while True:
        print("\n====== Smart Library System ======")
        print("1. Add Book")
        print("2. View Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Recommend Books")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(library)
        elif choice == "2":
            show_books(library)
        elif choice == "3":
            borrow_book(library, borrow_history)
        elif choice == "4":
            return_book(library)
        elif choice == "5":
            recommend_books(library, borrow_history)
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
