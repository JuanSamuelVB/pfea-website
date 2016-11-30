from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView

from pfea_app.models import Libro

@method_decorator(login_required, name='dispatch')
class LibroDelete(DeleteView):
    template_name = 'models/libro_confirmar_borrar.html'
    model = Libro
    success_url = reverse_lazy('pfea_app:lista_libros')
