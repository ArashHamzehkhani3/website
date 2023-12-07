from django.shortcuts import render
from django.http import HttpResponse
from mainweb.models import Book


def index_views(request):
   return render(request,'index.html')



def test_view(request):

   book=Book.objects.all()
   context={'book':book}

   return render(request,'test.html',context)
