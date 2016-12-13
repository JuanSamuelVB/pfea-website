from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView

from pfea_app.models import Mensaje

@method_decorator(login_required, name='dispatch')
class MensajeDelete(DeleteView):
    template_name = 'models/mensaje_confirmar_borrar.html'
    model = Mensaje
    success_url = reverse_lazy('pfea_app:mensajes')
