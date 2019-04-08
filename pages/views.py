from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    # return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, "home.html", {})
     
def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

    
def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 123
        
    }
    return render(request, "about.html", {})

    
def social_view(request, *args, **kwargs):
    return HttpResponse("<h1>Social Page</h1>")        