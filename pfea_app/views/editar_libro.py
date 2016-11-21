from django.urls import reverse_lazy
from django.views.generic import UpdateView

from pfea_app.models import Libro

class LibroUpdate(UpdateView):
    template_name = 'models/libro_editar.html'
    model = Libro
    fields = '__all__'
    success_url = reverse_lazy('pfea_app:lista_libros')
