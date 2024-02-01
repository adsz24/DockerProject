from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from datetime import datetime



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