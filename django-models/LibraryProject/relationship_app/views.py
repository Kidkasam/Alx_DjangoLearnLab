from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Book, Library
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test

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

# RBAC Views and Checks
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
