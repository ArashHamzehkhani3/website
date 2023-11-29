from django.shortcuts import render
from django.http import HttpResponse


def index_views(request):
   return render(request,'index.html')



def test_view(request):


   context={'name':'arash'}

   return render(request,'test.html',context)
