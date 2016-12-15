from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from pfea_app.models import Mensaje

@method_decorator(login_required, name='dispatch')
class MensajeList(ListView):
    template_name = 'models/mensaje_lista.html'
    model = Mensaje
