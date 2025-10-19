from django.urls import path
from . import views

urlpatterns = [
   
    # URL to open home page 
    path("", views.home, name='home'),
]
