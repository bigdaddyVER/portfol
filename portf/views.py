from django.shortcuts import render
from .models import *
from .models import Website
# Create your views here.

def home(request):
    return render(request, "portf/index.html")

def about(request):
    personal = Personal.objects.all()
    context = {
        'personal':personal,
    }
    return render(request, "portf/about.html", context)

def works(request):
    web = Website.objects.all()
    context = {
        'web':web,
    }
    return render(request, "portf/works.html", context)

def what(request):
    website = Website.objects.all()
    dohp = Doh.objects.all()
    context = {
        'website':website,
        'dohp':dohp,
     }
    return render(request, "portf/what.html", context)

def whatt(request):
    return render(request, 'index.html')

def art(request):
    artworks = Art.objects.all() 
    context = {    
        'artworks':artworks,
     }
    return render(request, "portf/inc/slider.html", {'artworks': context})
 
