from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView

from pfea_app.models import Herramienta

@method_decorator(login_required, name='dispatch')
class HerramientaCreate(CreateView):
    template_name = 'models/herramienta_registro.html'
    model = Herramienta
    fields = '__all__'
    success_url = reverse_lazy('pfea_app:lista_herramientas')
