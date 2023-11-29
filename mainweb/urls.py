
from django.urls import path
from mainweb.views import *



app_name='mainweb'

urlpatterns = [
 
    path('',index_views, name='index'),
    path('test',test_view,name='test')

    
]
