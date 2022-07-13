from os import path
from django.urls import path
from bookstore.views import *

urlpatterns = [
    path('', base_books, name='books'),
    path('book/<int:index>', base_list, name='base'),
    path('author/<int:index_author>/', author_list, name='author'),
    path('author_book/<int:in_author>/author_book', author_book, name='author_book')
]
