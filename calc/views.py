from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html', {'name': "Nathan"}) # Render page, JSON format

def add(request):  

    val1 = int(request.POST['num1']) # Get values from the request (from the form)
    val2 = int(request.POST['num2'])
    result = val1 + val2

    return render(request, 'result.html', {'result': result})