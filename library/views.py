from django.shortcuts import render
from .models import Book
from django.conf import settings
from datetime import datetime, timedelta


def index(request):
    return render(request, 'base.html')

#
# class BookAddView(CreateView):
#
#     template_name = 'add_book.html'
#     model = Book
#     fields = ['title', 'category']
#     success_url = '/'
#

# class AvailableBooksView(ListView):
#
#     model = Book
#     template_name = 'list_books.html'
#     context_object_name = 'all_books'
#
#     def get_queryset(self):
#         return Book.objects.all()


# class DetailBooksView(DetailView):
#
#     template_name = 'book_details.html'
#     model = Book
#
#     def get_queryset(self):
#         return Book.objects.all()


def list_available_books(request):

    context = {"Books": Book.objects.all()}
    return render(request, 'list_books.html', context)


def add_new_book_form(request):

    context = {"Categories": Book.Category}
    return render(request, 'add_book.html', context)


def add_new_book(request):

    title = request.POST["bookTitle"]
    category = request.POST["category"]
    error = None
    if any(element in [None, ""] for element in [title, category]):
        error = "All fields are mandatory"
        context = {"errorMessage": error, "Categories": Book.Category}
    else:
        book = Book(title=title, category=category)
        book.save()
        context = {}

    if error:
        template_name = "add_book.html"
    else:
        template_name = "base.html"

    return render(request, template_name, context)


def book_details(request):
    id = request.GET.get("id")
    book = Book.objects.filter(pk=id).first()
    context = {"Book": book}
    return render(request, "book_details.html", context)


def issue_book_form(request):

    books = Book.objects.filter(is_issued=False)
    context = {"Books": books}
    return render(request, 'issue_book.html', context)


def issue_book(request):

    id = request.POST["book_id"]
    user = request.POST["user"]

    error = None
    if any(element in [None, ""] for element in [id, user]):
        error = "All fields are mandatory"
        books = Book.objects.filter(is_issued=False)
        context = {"errorMessage": error, "Books": books}
    else:
        book = Book.objects.get(id=id)
        book.is_issued = True
        book.issued_to = user
        due_date = datetime.today() + timedelta(15)
        book.due_date = due_date.strftime(settings.DATE_INPUT_FORMATS[0])
        book.save()
        context = {}

    if error:
        template_name = "issue_book.html"
    else:
        template_name = "base.html"

    return render(request, template_name, context)


def return_book_form(request):

    books = Book.objects.filter(is_issued=True)
    context = {"Books": books}
    return render(request, 'return_book.html', context)


def return_book(request):

    id = request.POST["book_id"]

    book = Book.objects.get(id=id)
    book.is_issued = False
    book.issued_to = None
    book.due_date = None
    book.save()
    context = {}

    template_name = "base.html"

    return render(request, template_name, context)


def past_due_books(request):

    books = Book.objects.filter(is_issued=True)
    books_list = []
    current_date = datetime.today().strftime(settings.DATE_INPUT_FORMATS[0])
    current_date_format = datetime.strptime(current_date, settings.DATE_INPUT_FORMATS[0]).date()
    for book in books:
        due_date = datetime.strptime(book.due_date, settings.DATE_INPUT_FORMATS[0]).date()
        if due_date < current_date_format:
            books_list.append(book)

    context = {"Books": books_list}
    return render(request, 'past_due_books.html', context)
