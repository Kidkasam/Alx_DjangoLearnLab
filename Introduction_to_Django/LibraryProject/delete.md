# Delete Operation

## Command:
```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
remaining_books = Book.objects.all()
print(f"Books remaining: {len(remaining_books)}")
```

## Output:
```text
Books remaining: 0
```
