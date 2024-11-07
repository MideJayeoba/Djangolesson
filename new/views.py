#from django.http import HttpResponse
from django.shortcuts import render

def Homepage(request):
    #return HttpResponse("Hello World! I'm flying already")
    return render(request, "home.html")

def about(request):
    #return HttpResponse("My name is Jayeoba Peace Olamide and i like programming.")
    return render(request, 'about.html')