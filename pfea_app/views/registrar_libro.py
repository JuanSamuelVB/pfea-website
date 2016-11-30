from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView

from pfea_app.models import Libro

@method_decorator(login_required, name='dispatch')
class LibroCreate(CreateView):
    template_name = 'models/libro_registro.html'
    model = Libro
    fields = '__all__'
    success_url = reverse_lazy('pfea_app:lista_libros')
