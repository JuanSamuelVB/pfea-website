from django.db import models

NIVELES_ACADEMICOS = [
    (1, 'Primaria'),
    (2, 'Secundaria'),
    (3, 'Preparatoria'),
    (4, 'Universidad'),
]

PROGRAMAS = [
    (1,'Voluntariado'),
    (2,'Servicio Social 1era Etapa'),
    (3,'Servicio Social 2da Etapa'),
    (4,'Practicas Profesionales'),
    (5,'Proyecto de Vinculacion'),
]

TURNOS = [
    (1, 'Matutino'),
    (2,'Vespertino'),
    (3,'Mixto'),
]

class Voluntario(models.Model):
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    E_mail = models.EmailField(verbose_name='E-mail')
    Celular = models.CharField(max_length=10)
    Nivel_academico = models.IntegerField(choices=NIVELES_ACADEMICOS,default=1,verbose_name='Nivel académico')
    Escuela = models.CharField(max_length=50, blank=True, null=True)
    Capacitacion = models.CharField(max_length=50, blank=True, null=True, verbose_name='Capacitación')
    Matricula = models.CharField(max_length=30, blank=True, null=True)
    Semestre = models.CharField(max_length=50, blank=True, null=True)
    Programa = models.IntegerField(choices=PROGRAMAS, default=1)
    Horas_realizar = models.IntegerField(verbose_name='Horas a realizar')
    Horas_hechas = models.IntegerField(blank=True, null=True)
    Turno = models.IntegerField(choices=TURNOS, default=1)
    Fecha_inicio = models.DateField(verbose_name='Fecha de inicio')
    Seguro = models.BooleanField(default=False)
    Contacto_emergencia = models.TextField(max_length=200, blank=True, null=True)
    Informacion = models.BooleanField(default=True)
    Solicitud_aceptada = models.BooleanField(default=False, blank=True)

    def __str__(self):
        if self.Solicitud_aceptada:
            return "%s %s" % (self.Nombre, self.Apellido)
        else:
            return "Solicitud de %s %s" % (self.Nombre, self.Apellido)
