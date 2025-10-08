from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
import wikipedia

def home(request):
    if request.method == "POST":
        search = request.POST['search']
        try:
            # No of sentences that you want as output
            # print( search)
            result = wikipedia.summary(search, sentences=3)
        except Exception as e:
            # print(e)
            return HttpResponse("Wrong Input")
        return render(request,"main/index.html",{"result":result})
    return render(request,"main/index.html")
