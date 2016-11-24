from django.urls import reverse_lazy
from django.views.generic import ListView

from pfea_app.models import SolicitudDeVoluntario

class SolicitudDeVoluntariosList(ListView):
    template_name = 'models/voluntarios_solicitudes.html'
    model = SolicitudDeVoluntario
