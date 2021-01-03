from django.conf.urls import url
from .views import add_new_book, add_new_book_form, list_available_books, book_details, issue_book, issue_book_form, \
    index, return_book, return_book_form, past_due_books

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
