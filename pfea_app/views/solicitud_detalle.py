from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView

from pfea_app.models import Voluntario

@method_decorator(login_required, name='dispatch')
class SolicitudDeVoluntariosDetail(DetailView):
    template_name = 'models/voluntarios_solicitud_detalle.html'
    model = Voluntario
