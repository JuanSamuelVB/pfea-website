from django.views.decorators.http import require_POST
from django.shortcuts import redirect

from pfea_app.models import Mensaje

@require_POST
def nuevo_mensaje(request):
    mensaje = Mensaje()

    mensaje.nombre = request.POST.get('name', 'Anónimo')
    mensaje.correo_electronico = request.POST.get('email', '-')
    mensaje.mensaje = request.POST.get('message', 'Sin mensaje')

    mensaje.save()

    return redirect('pfea_app:gracias')
