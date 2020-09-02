from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

# Create your views here.

def index(request):
    # dest1 = Destination()
    # dest2 = Destination()
    # dest3 = Destination()

    # dest1.setAll("Mumbai", "Cool Place", 700, 'destination_1.jpg', False)
    # dest2.setAll("Compton", "Bad Place", 200, 'destination_2.jpg', True)
    # dest3.setAll("Los Angeles", "Ok Place", 400, 'destination_3.jpg', False)

    # dest_list = [dest1, dest2, dest3]

    dest_list = Destination.objects.all()

    return render(request, 'index.html', {'dest_list': dest_list}) # Render page, JSON format


    