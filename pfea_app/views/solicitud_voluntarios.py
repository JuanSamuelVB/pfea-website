from django.urls import reverse_lazy
from django.views.generic import CreateView

from pfea_app.models import SolicitudDeVoluntario

class SolicitudDeVoluntariosCreate(CreateView):
    template_name = 'models/voluntarios_solicitud.html'
    model = SolicitudDeVoluntario
    fields = '__all__'
    success_url = reverse_lazy('pfea_app:lista_libros')
