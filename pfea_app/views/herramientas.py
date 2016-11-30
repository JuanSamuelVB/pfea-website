from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from pfea_app.models.herramienta import Herramienta

@method_decorator(login_required, name='dispatch')
class HerramientaList(ListView):
    template_name = 'models/herramienta_lista.html'
    model = Herramienta
