from django.conf.urls import url
from .views import *


urlpatterns = [

    url(r'^$', index, name='base'),
    url('add-book-form', add_new_book_form, name='add book form'),
    url('list-books', list_available_books, name='list books'),
    url(r'^book/$', book_details, name='book details'),
    url('add-book', add_new_book, name='add book'),
    url('issue-book-form', issue_book_form, name='issue book form'),
    url('issue-book', issue_book, name='issue book'),
    url('return-book-form', return_book_form, name='return book form'),
    url('return-book', return_book, name='return book'),
    url('past-due-books', past_due_books, name='past due books')
]
