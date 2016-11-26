from django.shortcuts import redirect

from pfea_app.models import Voluntario

def solicitud_aceptar(request, pk):
    voluntario = Voluntario.objects.get(pk=pk)
    voluntario.Solicitud_aceptada = True
    voluntario.save()

    return redirect('pfea_app:solicitudes')
