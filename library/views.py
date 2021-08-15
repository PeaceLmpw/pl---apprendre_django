from django.shortcuts import render
from django.http import HttpResponse
from .models import books

# Create your views here.

def books_view(request):
    

    # all = {'books':books}

    return render(request, 'library/books.html', {'books':books})
