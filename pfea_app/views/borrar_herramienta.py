from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView

from pfea_app.models import Herramienta

@method_decorator(login_required, name='dispatch')
class HerramientaDelete(DeleteView):
    template_name = 'models/herramienta_confirmar_borrar.html'
    model = Herramienta
    success_url = reverse_lazy('pfea_app:lista_herramientas')
