from django.db import models

class SolicitudDeVoluntario(models.Model):
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    E_mail = models.EmailField(verbose_name='E-mail')
    Celular = models.CharField(max_length=10)
# NIVELES ACADEMICOS
    Primaria = 1
    Secundaria = 2
    Preparatoria = 3
    Universidad = 4
    NIVELES = [
        (Primaria, 'Primaria'),
        (Secundaria, 'Secundaria'),
        (Preparatoria, 'Preparatoria'),
        (Universidad, 'Universidad'),
    ]
    Nivel_academico = models.IntegerField(choices=NIVELES,default=1,verbose_name='Nivel académico')
    Escuela = models.CharField(max_length=50, blank=True, null=True)
    Capacitacion = models.CharField(max_length=50, blank=True, null=True, verbose_name='Capacitación')
    Matricula = models.CharField(max_length=30, blank=True, null=True)
    Semestre = models.CharField(max_length=50, blank=True, null=True)
# PROGRAMAS
    Voluntariado = 1
    Servicio_social1 = 2
    Servicio_social2 = 3
    Practicas = 4
    Proyecto = 5
    PROGRAMAS = [
        (Voluntariado,'Voluntariado'),
        (Servicio_social1,'Servicio Social 1era Etapa'),
        (Servicio_social2,'Servicio Social 2da Etapa'),
        (Practicas,'Practicas Profesionales'),
        (Proyecto,'Proyecto de Vinculacion'),
    ]
    Programa = models.IntegerField(choices=PROGRAMAS, default = 1)
    Horas_realizar = models.IntegerField(verbose_name='Horas a realizar')
# TURNOS
    Matutino = 1
    Vespertino = 2
    Mixto = 3
    TURNOS = [
        (Matutino, 'Matutino'),
        (Vespertino,'Vespertino'),
        (Mixto,'Mixto'),
    ]
    Turno = models.IntegerField(choices=TURNOS, default = 1)
    Fecha_inicio = models.DateField(verbose_name='Fecha de inicio')
    Seguro = models.BooleanField(default=False)
    Contacto_emergencia = models.TextField(max_length = 200, blank=True, null=True)
    Informacion = models.BooleanField(default=True)

    class Meta:
        db_table = 'voluntario'
        app_label = 'pfea_app'

    def __str__(self):
        return "%s, %s Programa = %s"%(self.Nombre, self.Apellido, self.get_Programa_display())
