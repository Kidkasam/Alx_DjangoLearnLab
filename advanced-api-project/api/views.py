from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# ListView: Retrieve all books
# Allows read-only access for unauthenticated users, but restricts modification.
class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# DetailView: Retrieve a single book by ID
# Allows read-only access for unauthenticated users.
class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# CreateView: Add a new book
# Restricted to authenticated users only.
class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    # Custom behavior: Ensure validation logic is handled in the serializer (already implemented)
    def perform_create(self, serializer):
        # We can add custom logic here if needed, for now standard save is sufficient
        serializer.save()

# UpdateView: Modify an existing book
# Restricted to authenticated users only.
class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    # Custom behavior: Example of restricting updates (if requirements evolved)
    def perform_update(self, serializer):
        serializer.save()

# DeleteView: Remove a book
# Restricted to authenticated users only.
class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
