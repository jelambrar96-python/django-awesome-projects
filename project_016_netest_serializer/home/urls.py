from django.contrib import admin 
from django.urls import path, include 

from .views import * 

  
urlpatterns = [ 
   path('get-item/', get_item), 
    
]