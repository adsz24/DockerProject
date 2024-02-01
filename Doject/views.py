from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from datetime import datetime
from .models import Product


# Create your views here.

def home(request):                          #Funkcja dodajaca widok dla strony glownej
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'Doject/index.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
        }
    )

def product_catalog(request):                       #Funkcja pobieraj¹ca dane z models
    products = Product.objects.all()
    return render(
        request,
       'Doject/index.html', 
       {
           'products': products,
       }
    )