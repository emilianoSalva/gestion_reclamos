
from django.urls import path
#from ejemploDjango import hola_mudo
from hola_mudo.views import saludar, saludarAdios




urlpatterns = [
    path('saludar/',saludar), 
    path('saludarAdios/',saludarAdios),   
]
