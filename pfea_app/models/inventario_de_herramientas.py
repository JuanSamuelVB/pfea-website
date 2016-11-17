from django.db import models

class InventarioDeHerramientas(models.Model):
    Responsable1 = models.CharField(max_length=200)
    Responsable1 = models.CharField(max_length=200, null=True, blank=True)
    Fecha = models.DateField()
    Hora = models.TimeField()

    def __str__(self):
        return "Inventario del dia %s"%(self.Fecha)
