from django.shortcuts import render
from django.http import HttpResponse


def index_views(request):
   return render(request,'index.html')
