from django.urls import reverse_lazy
from django.views.generic import CreateView

from pfea_app.models import Voluntario

class SolicitudDeVoluntariosCreate(CreateView):
    template_name = 'models/voluntarios_solicitud.html'
    model = Voluntario
    fields = '__all__'
    exclude = ['Horas_hechas', 'Solicitud_aceptada']
    success_url = reverse_lazy('pfea_app:gracias')
