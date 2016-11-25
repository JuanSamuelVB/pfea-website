from django.urls import reverse_lazy
from django.views.generic import DeleteView

from pfea_app.models import Voluntario

class SolicitudDeVoluntariosDelete(DeleteView):
    template_name = 'models/voluntarios_solicitud_confirmar_borrar.html'
    model = Voluntario
    success_url = reverse_lazy('pfea_app:solicitudes')
