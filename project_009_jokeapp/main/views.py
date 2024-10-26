from django.shortcuts import render
import pyjokes
# Create your views here.

def home(request):
    joke=pyjokes.get_joke()
    return render(request,"main/index.html",{"joke":joke})
