from django.urls import reverse_lazy
from django.views.generic import CreateView

from pfea_app.models import Libro

class LibroCreate(CreateView):
    template_name = 'models/libro_registro.html'
    model = Libro
    fields = '__all__'
    success_url = reverse_lazy('pfea_app:lista_libros')
