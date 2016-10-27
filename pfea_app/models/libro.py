from django.db import models

class Libro (models.Model):
    Titulo = models.CharField(max_length = 200)
    Autor = models.CharField(max_length = 150)
    Edicion = models.CharField(max_length = 20)
    Publicacion = models.CharField(max_length = 40)
    Editorial = models.CharField(max_length = 50)
    Ano = models.CharField(max_length=4)
    Paginas = models.IntegerField()
    Volumen = models.CharField(max_length=10)
    Cantidad = models.IntegerField()

    class Meta:
        db_table = 'libro'
        app_label = 'pfea_app'

    def __unicode__(self):
        return "%s, Autor: %s, Volumen: %s"%(self.Titulo, self.Autor, self.Volumen)
