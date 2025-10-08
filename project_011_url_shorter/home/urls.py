from django.urls import path
from home import views

urlpatterns = [
    path('',views.index),
    path('index_form',views.index_form),
]
