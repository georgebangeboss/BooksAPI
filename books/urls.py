from django.urls import path
from .views import get_authors,get_books

urlpatterns = [
    path('get-books',get_books),
    path('get-authors',get_authors),
]