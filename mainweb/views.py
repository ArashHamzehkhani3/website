from django.shortcuts import render
from django.http import HttpResponse
from mainweb.models import Book,Contact


def index_views(request):
   return render(request,'index.html')



def test_view(request):

   if request.method=="POST":
      name=request.POST.get('name')
      email=request.POST.get('email')
      subject=request.POST.get('subject')
      message=request.POST.get('message')
      
      c = Contact()

      c.name=name
      c.email=email
      c.subject=subject
      c.message=message

      c.save()
      print(name,email,subject,message)




   return render(request,'test.html',{})
