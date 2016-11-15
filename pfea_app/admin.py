from django.contrib import admin
from .models import Herramienta, Libro, SolicitudDeVoluntario

# Register your models here.
admin.site.register(Herramienta)
admin.site.register(Libro)
admin.site.register(SolicitudDeVoluntario)
