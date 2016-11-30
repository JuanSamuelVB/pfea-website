from django.db import models

class Herramienta(models.Model):
    Concepto = models.CharField(max_length=50, default='herramienta')
    Marca = models.CharField(max_length=100, null=True, blank=True)
    Modelo = models.CharField(max_length=20, null=True, blank=True)
    Numero_Serie = models.CharField(max_length=20, null=True, blank=True, verbose_name='Número de serie')
    Descripcion = models.CharField(max_length=200, null=True, blank=True)
    Cantidad = models.IntegerField(default=0)
    Codigo = models.CharField(max_length=20, default=0)

    def __str__(self):
        return "Articulo :%s, Codigo: %s, Cantidad: %s"%(self.Concepto, self.Codigo, self.Cantidad)

# crear una tabla muchos a muchos para cuando sean varios articulos?
# class Herramienta(models.Model):
#     Articulo = models.CharField(max_length=100)
#     Tipo = models.CharField(max_length=10)
#     Prestado = models.BooleanField(default=False)
#     Ultimo_presto = models.CharField(max_length=200, null=True, blank=True)
#n
#     class Meta:
#         db_table = 'herramienta'
#         app_label = 'pfea_app'
#
#     def __str__(self):
#         return "%s, Tipo: %s"%(self.Articulo, self.Tipo)
