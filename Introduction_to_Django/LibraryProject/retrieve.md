# Retrieve Operation

## Command:
```python
from bookshelf.models import Book
# Retrieve all books
all_books = Book.objects.all()
print(f"All books: {all_books}")

# Retrieve specific book
book = Book.objects.get(title="1984")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")
```

## Output:
```text
All books: <QuerySet [<Book: 1984 by George Orwell (1949)>]>
Title: 1984
Author: George Orwell
Publication Year: 1949
```
