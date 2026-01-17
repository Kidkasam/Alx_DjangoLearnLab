# CRUD Operations Documentation

## 1. Create Operation
```python
from bookshelf.models import Book
book = Book.objects.create(
    title="1984",
    author="George Orwell", 
    publication_year=1949
)
print(f"Book created: {book.title}")
```
Output:
```text
Book created: 1984
```

## 2. Retrieve Operation  
```python
from bookshelf.models import Book
# Retrieve specific book
book = Book.objects.get(title="1984")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")
```
Output:
```text
Title: 1984
Author: George Orwell
Publication Year: 1949
```

## 3. Update Operation
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(f"Updated title: {book.title}")
```
Output:
```text
Updated title: Nineteen Eighty-Four
```

## 4. Delete Operation
```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
remaining_books = Book.objects.all()
print(f"Books remaining: {len(remaining_books)}")
```
Output:
```text
Books remaining: 0
```
