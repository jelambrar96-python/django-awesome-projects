from django.shortcuts import render
from django.contrib import messages
from .models import newslatteremail

def home(request):
    
    # if post request comes from the subscribe button
    # then saving user email in our database
    if 'subscribe' in request.POST and request.POST.get("email"):
        email = newslatteremail()
        email.userEmail = request.POST.get("email")
        try:
            email.save()
        except:
            messages.info(request, 'Error: You are already subscribed!!!')
            return render(request, 'news.html')
        messages.info(
            request, 'You have successfully subscribed to our newslatter.')
    
    # if post request comes from the unsubscribe button
    # then deleting the user email from our database
    if 'unsubscribe' in request.POST and request.POST.get("email"):
        newslatteremail.objects.get(
            userEmail=request.POST.get("email")).delete()
        messages.info(request, 'sorry to see you!!!')
        
    return render(request, 'news.html')
