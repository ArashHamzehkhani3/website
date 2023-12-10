from django.shortcuts import render
#from django.http import HttpResponse
from mainweb.models import Book,Contact
from mainweb.forms import NameForm


def index_views(request):
   return render(request,'index.html')



def test_view(request):
   if request.method=='POST':
      name=request.POST.get('name')
      print(name)
   form=NameForm()
   return render(request,'test.html',{'form':form})
