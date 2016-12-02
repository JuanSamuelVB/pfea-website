from django.db import models

class Libro (models.Model):
    Autor = models.CharField(max_length = 150)
    Ano = models.CharField(max_length=4)
    Titulo = models.CharField(max_length = 200)
    Edicion = models.CharField(max_length = 20)
    Publicacion = models.CharField(max_length = 40)
    Editorial = models.CharField(max_length = 100)
    Volumen = models.CharField(max_length=10, blank = True, null=True)
    Cantidad = models.IntegerField(default=1)

    def __str__(self):
        return "Autor: %s, Titulo: %s, Ano: %s, Cantidad: %s"%(self.Autor, self.Titulo, self.Ano, self.Cantidad)
