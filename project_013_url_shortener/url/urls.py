# url/urls.py
from django.urls import path
from . import views

app_name = "url"

urlpatterns = [
    path("", views.urlShort, name="home"),  # Home route for URL shortening form
    path("u/<str:slugs>", views.urlRedirect, name="redirect"),  # Redirect using the slug
]
