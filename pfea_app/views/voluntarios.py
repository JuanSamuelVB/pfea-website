from django.views.generic import ListView

from pfea_app.models import Voluntario

class VoluntarioList(ListView):
    template_name = 'models/voluntarios_lista.html'
    queryset = Voluntario.objects.filter(Solicitud_aceptada=True)
