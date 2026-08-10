from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Book

def books_view(request):
    template = 'books/books_list.html'
    books_all = Book.objects.all().order_by('-pub_date')

    context = {
        'books':books_all,
    }
    return render(request, template, context)

def show_book(request, pub_date):

   template = 'books/book_date.html'
   current_books = get_list_or_404(Book, pub_date=pub_date)

   all_dates = Book.objects.values_list('pub_date', flat=True).distinct().order_by('pub_date')
   dates_list = list(all_dates)

   prev_date = None
   next_date = None
   try:
       current_index = dates_list.index(pub_date)
       if current_index > 0:
           prev_date = dates_list[current_index - 1]
       if current_index < len(dates_list)-1:
           next_date = dates_list[current_index + 1]
   except ValueError:
       pass

   context = {
       'current_books': current_books,
       'pub_date': pub_date,
       'prev_date': prev_date,
       'next_date': next_date,
   }
   return render(request, template, context)
