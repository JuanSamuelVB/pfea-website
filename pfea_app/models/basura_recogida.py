from django.db import models

class BasuraRecogida(models.Model):
    Zona = models.CharField(max_length=50)
    Adultos = models.IntegerField()
    Ninos = models.IntegerField(verbose_name='Niños')

    # Objetos mas comunmente encontrados
    Colillas = models.IntegerField()
    Envoltorios = models.IntegerField()
    Envases_para_llevar_plastico = models.IntegerField()
    Envases_para_llevar_unicel = models.IntegerField()
    Taparroscas = models.IntegerField()
    Corcholatas = models.IntegerField()
    Tapas = models.IntegerField()
    Popotes = models.IntegerField()
    Cubiertos = models.IntegerField()
    Botellas_plastico = models.IntegerField()
    Botellas_vidrio = models.IntegerField()
    Latas = models.IntegerField()
    Bolsas_comestibles_plastico = models.IntegerField()
    Bolsas_plastico = models.IntegerField()
    Bolsas_papel = models.IntegerField()
    Vasos_platos_papel = models.IntegerField()
    Vasos_platos_plastico = models.IntegerField()
    Vasos_platos_unicel = models.IntegerField()

    # Avios de pesca
    Boyas_trampas = models.IntegerField()
    Redes_pesca = models.IntegerField()
    Cuerda = models.IntegerField()
    Linea_pesca = models.IntegerField()

    # Materiales de empaque
    Contenedores_6_latas = models.IntegerField()
    Otros_plastico_unicel = models.IntegerField()
    Otras_botellas_plastico = models.IntegerField()
    Cintas_embalar= models.IntegerField()
    Envoltorio_tabaco = models.IntegerField()

    # Otros residuos
    Electrodomesticos = models.IntegerField()
    Globos = models.IntegerField()
    Puntas_puros = models.IntegerField()
    Encendedores = models.IntegerField()
    Materiales_construccion = models.IntegerField()
    Cohetes = models.IntegerField()
    Llantas = models.IntegerField()

    # Higiene personal
    Condones = models.IntegerField()
    Pañales = models.IntegerField()
    Jeringas = models.IntegerField()
    Tampones = models.IntegerField()
    Ropa = models.IntegerField()
    Guantes_latex = models.IntegerField()

    # Basura pequeña
    Pedazos_unicel = models.IntegerField()
    Pedazos_vidrio = models.IntegerField()
    Pedazos_plastico = models.IntegerField()
    Pedazos_papel = models.IntegerField()

    # Animales muertos o lesionados
    Animales_muertos = models.IntegerField()
    Animales_lesionados = models.IntegerField()
    Animales_enredados = models.IntegerField()
    Animales_notas = models.TextField()

    Objetos_preocupacion_local = models.TextField()

    Costales_basura = models.IntegerField()
    Peso_costales = models.IntegerField()
    Distancia_limpiada = models.IntegerField()

    def __str__(self):
        return "Tarjeta no. %d de %s"%(self.pk, self.Zona)
