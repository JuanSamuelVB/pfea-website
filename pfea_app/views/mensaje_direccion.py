from django.views.generic import TemplateView

class MensajeDireccionView(TemplateView):
    template_name = 'pfea_app/mensaje_de_la_direccion.html'
