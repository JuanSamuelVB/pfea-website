from django.contrib import admin
from .models import (Herramienta, Libro,
    Voluntario, BasuraRecogida)

# Deprecated, InventarioDeHerramientas

# Register your models here.
admin.site.register(Herramienta)
#admin.site.register(InventarioDeHerramientas)
admin.site.register(Libro)
admin.site.register(Voluntario)
admin.site.register(BasuraRecogida)
