from django.db import models

class Mensaje(models.Model):
    nombre = models.CharField(max_length = 150)
    correo_electronico = models.EmailField()
    mensaje = models.TextField()

    def __str__(self):
        return "Mensaje de %s" % (self.nombre)
