from django.db import models

class Herramienta(models.Model):
    Articulo = models.CharField(max_length=100)
    Tipo = models.CharField(max_length=10)
    Prestado = models.BooleanField(default=False)
    Ultimo_presto = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'herramienta'
        app_label = 'pfea_app'

    def __unicode__(self):
        return "%s, Tipo: %s"%(self.Articulo, self.Tipo)
