from django.contrib import admin
from .models import (Herramienta, InventarioDeHerramientas, Libro,
    Voluntario, BasuraRecogida)

# Register your models here.
admin.site.register(Herramienta)
admin.site.register(InventarioDeHerramientas)
admin.site.register(Libro)
admin.site.register(Voluntario)
admin.site.register(BasuraRecogida)
