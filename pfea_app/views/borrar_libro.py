from django.urls import reverse_lazy
from django.views.generic import DeleteView

from pfea_app.models import Libro

class LibroDelete(DeleteView):
    template_name = 'models/libro_confirmar_borrar.html'
    model = Libro
    success_url = reverse_lazy('pfea_app:lista_libros')
