# Problem 5: Library Book Search

books = [
    ("Python Basics", 5),
    ("Data Science", 0),
    ("Java Programming", 3),
    ("Machine Learning", 0)
]

# 1. Display unavailable books (copies = 0)
print("Unavailable books:")
for title, copies in books:
    if copies == 0:
        print(title)

# 2. Find all books with more than 3 copies
print("\nBooks with more than 3 copies:")
for title, copies in books:
    if copies > 3:
        print(title, "-", copies)

# 3. Count available books (copies > 0)
available_books = sum(1 for _, copies in books if copies > 0)
print("\nNumber of available books:", available_books)

# 4. Stop searching once a requested book is found
requested_book = "Java Programming"
print("\nSearching for:", requested_book)
for title, copies in books:
    if title == requested_book:
        print("Book found:", title, "-", copies, "copies")
        break
