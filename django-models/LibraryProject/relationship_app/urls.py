from django.urls import path
from . import views
from .views import list_books

app_name = 'relationship_app'

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('libraries/', views.LibraryListView.as_view(), name='library_list'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
