from django.shortcuts import render
# books/views.py
from django.views.generic import ListView
from .models import Book
class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'all_books_list'
# Create your views here.
