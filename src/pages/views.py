from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    # return HttpResponse("<h1>Hello there!<h1>")  # HTML code
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Our Contacts<h1>")
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    my_context = {                  # this is context that can be preloaded into the view for the user
        "my_text": "This is about us",
        "my_number": 123,
        "my_list": ['A1', 'A', 'A-', 'B+', 'B', 'B-']
    }
    # return HttpResponse("<h1>About us<h1>")
    return render(request, "about.html", my_context)


def social_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Our Socials<h1>")
    return render(request, "socials.html", {})
