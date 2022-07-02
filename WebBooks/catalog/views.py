from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.views import generic


class BookListView(generic.ListView):
    model = Book
    paginate_by = 3

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 4

class AuthorDetailView(generic.DetailView):
    model = Author



# Create your views here.

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact=2).count()
    num_authors = Author.objects.count()


    return render(request, 'index.html',
                  context={ 'num_books': num_books,
                            'num_instances': num_instances,
                            'num_instances_available': num_instances_available,
                            'num_authors': num_authors,
                             }    )