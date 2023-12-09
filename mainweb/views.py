from django.shortcuts import render
from django.http import HttpResponse
from mainweb.models import Book


def index_views(request):
   return render(request,'index.html')



def test_view(request):

   if request.method=="POST":
      name=request.POST.get('name')
      email=request.POST.get('email')
      subject=request.POST.get('subject')
      message=request.POST.get('message')
      print(name,email,subject,message)


   return render(request,'test.html',{})
