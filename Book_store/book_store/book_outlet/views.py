from django.shortcuts import render
from .models import Book
from django.http import Http404

# Create your views here.



def index(request):
    Books=Book.objects.all()
    return render(request,"book_outlet/index.html",{
        'book':Books
    })


def book_detail(request,id):
    try:
        Books=Book.objects.get(pk=id)
    except:
        raise Http404()
    return render(request,"book_outlet/book_detail.html",{
        'title':Books.title,
        'author':Books.author,
        'rating':Books.rating
    })