# Problem-Solving-Project
# Smart Library Management and Recommendation System

## Overview

The Smart Library Management and Recommendation System is a console-based Python application designed to manage basic library operations such as adding books, borrowing books, returning books, and recommending books based on user borrowing history.

This project demonstrates fundamental programming concepts such as functions, loops, conditionals, file handling, and data structures in Python.

---

## Problem Statement

In traditional library systems, users can borrow and return books, but they often receive no assistance in choosing what to read next. This project addresses that issue by introducing a simple recommendation feature based on previously borrowed books.

---

## Features

* Add new books to the library
* View all available and borrowed books
* Borrow a book
* Return a borrowed book
* Recommend books based on the last borrowed genre
* Persistent storage using JSON file handling

---

## Technologies Used

* Python 3
* JSON for data storage

---

## Project Structure

```
smart-library/
│
├── main.py          # Main application code
├── library.json     # Stores book data (auto-generated)
└── README.md        # Project documentation
```

---

## How the System Works

### 1. Add Book

Users can add books by providing:

* Title
* Author
* Genre

The book is then stored in the library database.

### 2. View Books

Displays all books along with their:

* Title
* Author
* Genre
* Availability status

### 3. Borrow Book

Allows users to borrow a book if it is currently available. The system updates the availability status and records borrowing history.

### 4. Return Book

Users return a book by entering the exact title. The system marks the book as available again.

### 5. Recommendation System

After a book is borrowed, the system recommends other available books from the same genre.

---

## Installation and Setup

### Step 1: Install Python

Make sure Python 3 is installed on your system.

You can check by running:

```
python --version
```

### Step 2: Clone the Repository

```
git clone https://github.com/your-username/smart-library.git
cd smart-library
```

### Step 3: Run the Program

```
python main.py
```

The system will automatically create a `library.json` file when you add your first book.

---

## Sample Menu

```
====== Smart Library System ======
1. Add Book
2. View Books
3. Borrow Book
4. Return Book
5. Recommend Books
6. Exit
```

---

## Example Usage

### Adding a Book

```
Enter book title: Harry Potter
Enter author name: J.K. Rowling
Enter genre: Fantasy
```

### Borrowing a Book

```
Enter book number to borrow: 1
Book borrowed successfully.
```

### Returning a Book

```
Enter book title to return: Harry Potter
Book returned successfully.
```

## **Photos of Output**


<img width="409" height="816" alt="Screenshot 2026-03-28 022143" src="https://github.com/user-attachments/assets/e8161898-56d3-4513-9337-e2e12d43eb41" />

---

## Key Programming Concepts Demonstrated

* Lists and dictionaries for data storage
* Functions for modular programming
* Loops and conditional statements for logic control
* File handling using JSON for persistent data storage
* Basic recommendation logic using previous user actions

---

## Limitations

* The system is console-based and does not have a graphical user interface.
* The recommendation feature is based only on genre and does not use advanced algorithms.

---

## Future Improvements

* Add user accounts and login system
* Implement a graphical user interface
* Use a database such as SQLite instead of JSON
* Add search functionality for books

---

## Author

Aahana Satapathy

25BOE10087

Course: Introduction to Problem Solving and Programming
