from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says Hello World: <FONT COLOR = BLUE>"
                        "<A HREF = '/rango/about'> here is the about page </A></FONT>")

def about(request):
    return HttpResponse("Rango says here is the about page:"
                        "<FONT COLOR = BLUE>"
                        "<A HREF = '/rango'> here is the home page </A></FONT>"
                        "This tutorial has been put together by Jake Aldred, 2066891")
