from django.contrib import admin
from django.urls import path

from home import views

urlpatterns = [
    path('logout/', views.custom_logout, name="logout"),
    path('pdf/', views.pdf , name='pdf'),
    path('admin/', admin.site.urls),
    path('login/' , views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    
    path('', views.recipes, name='recipes'),
    path('update_recipe/<id>', views.update_recipe, name='update_recipe'),
    path('delete_recipe/<id>', views.delete_recipe, name='delete_recipe'),
]
