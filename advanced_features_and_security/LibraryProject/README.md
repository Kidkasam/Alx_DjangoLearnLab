# Permissions and Groups Setup

## Permissions
The `Book` model has custom permissions:
- `can_view`: Allows viewing book lists and details.
- `can_create`: Allows creating new books.
- `can_edit`: Allows editing existing books.
- `can_delete`: Allows deleting books.

## Groups
Run `python manage.py setup_groups` to create the following groups:

### Viewers
- Permissions: `can_view`

### Editors
- Permissions: `can_create`, `can_edit`

### Admins
- Permissions: `can_view`, `can_create`, `can_edit`, `can_delete`

## Usage
Permissions are enforced in views using the `@permission_required` decorator:
```python
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    ...
```