from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from pfea_app.models import Voluntario

@method_decorator(login_required, name='dispatch')
class VoluntarioList(ListView):
    template_name = 'models/voluntarios_lista.html'
    queryset = Voluntario.objects.filter(Solicitud_aceptada=True)
