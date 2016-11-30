from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from pfea_app.models import Voluntario

@method_decorator(login_required, name='dispatch')
class SolicitudDeVoluntariosList(ListView):
    template_name = 'models/voluntarios_solicitudes.html'
    queryset = Voluntario.objects.filter(Solicitud_aceptada=False)
