from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def saludar(request):
    return HttpResponse("hola")

def saludarAdios(request):
    return HttpResponse("<h1>chau</h1><br> <h1><i>Adios</i></h1>")
    
