from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from pfea_app.models.libro import Libro

@method_decorator(login_required, name='dispatch')
class LibroList(ListView):
    template_name = 'models/libro_lista.html'
    model = Libro
