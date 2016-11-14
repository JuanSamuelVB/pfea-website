from django.shortcuts import render
from django.views.generic import ListView
from pfea_app.models.libro import Libro

class LibroList(ListView):
    template_name = 'models/libro_lista.html'
    model = Libro
