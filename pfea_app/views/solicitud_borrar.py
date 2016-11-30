from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView

from pfea_app.models import Voluntario

@method_decorator(login_required, name='dispatch')
class SolicitudDeVoluntariosDelete(DeleteView):
    template_name = 'models/voluntarios_solicitud_confirmar_borrar.html'
    model = Voluntario
    success_url = reverse_lazy('pfea_app:solicitudes')
