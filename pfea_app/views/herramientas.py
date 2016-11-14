from django.shortcuts import render
from django.views.generic import ListView
from pfea_app.models.herramienta import Herramienta

class HerramientaList(ListView):
    template_name = 'models/herramienta_lista.html'
    model = Herramienta
