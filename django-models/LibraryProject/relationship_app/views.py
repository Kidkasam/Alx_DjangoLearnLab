from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Book, Library
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Function-based view: List all books
def list_books(request):
    """Function-based view to display all books"""
    books = Book.objects.all().select_related('author')
    context = {
        'books': books,
        'title': 'All Books'
    }
    return render(request, 'relationship_app/list_books.html', context)

# Class-based view: List all libraries
class LibraryListView(ListView):
    """Class-based view to display all libraries"""
    model = Library
    template_name = 'relationship_app/library_list.html'
    context_object_name = 'libraries'
    
    def get_queryset(self):
        return Library.objects.all().prefetch_related('books')

# Class-based view: Display library details
class LibraryDetailView(DetailView):
    """Class-based view to display library details with books"""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add additional context if needed
        return context

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('relationship_app:list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
