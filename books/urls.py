from django.urls import path
from .views import create_book,get_all_books

urlpatterns = [
    path('create-book',create_book),
    path('get-all-books',get_all_books)
]