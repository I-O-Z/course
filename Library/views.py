from django.shortcuts import render

from Library.models import Book


def home_page(request):
    context = {
        'title': 'Тебе доступно:',
        'user_greeting': 'Привет пользователь!'
    }
    return render(request, 'library/home.html', context)


def books_list(request):
    context = {'books': Book.objects.all(),
               'title': 'Книги:'
               }
    return render(request, 'library/books.html', context)


def book_detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'library/book.html', {'book': book})


def not_ready(request):
    return render(request, 'Library/n0t_ready.html', {'message': 'Страница в процессе создания.'})
