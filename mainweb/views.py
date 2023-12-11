from django.shortcuts import render
from django.http import HttpResponse
from mainweb.models import Book,Contact
from mainweb.forms import NameForm


def index_views(request):
   return render(request,'index.html')



def test_view(request):
   if request.method=='POST':
      form=NameForm(request.POST)
      if form.is_valid():
        name=form.cleaned_data['name']
        email=form.cleaned_data['email']
        subject=form.cleaned_data['subject']
        message=form.cleaned_data['message']
        print(name,email,subject,message)
        return HttpResponse("Done")
      else:
         return HttpResponse("Error")

      
   form=NameForm()
   return render(request,'test.html',{'form':form})
