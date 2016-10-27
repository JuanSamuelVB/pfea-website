from django.views.generic import TemplateView

class MensajeDireccionView(TemplateView):
    template_name = 'about/mensaje_de_la_direccion.html'
