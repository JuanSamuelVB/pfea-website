from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from pfea_app.models import Voluntario

@login_required
def solicitud_aceptar(request, pk):
    voluntario = Voluntario.objects.get(pk=pk)
    voluntario.Solicitud_aceptada = True
    voluntario.save()

    return redirect('pfea_app:solicitudes')
