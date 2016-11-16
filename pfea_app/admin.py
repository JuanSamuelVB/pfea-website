from django.contrib import admin
from .models import (Herramienta, InventarioDeHerramientas, Libro,
    SolicitudDeVoluntario, Voluntario)

# Register your models here.
admin.site.register(Herramienta)
admin.site.register(InventarioDeHerramientas)
admin.site.register(Libro)
admin.site.register(SolicitudDeVoluntario)
admin.site.register(Voluntario)
