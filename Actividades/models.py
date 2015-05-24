from django.db import models


class Actividad(models.Model):
    id_evento = models.IntegerField()
    titulo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    precio = models.CharField(max_length=100)
    fecha = models.CharField(max_length=100)
    hora = models.CharField(max_length=32)
    duracion = models.CharField(max_length=100)
    larga_duracion = models.CharField(max_length=100)
    url  = models.CharField(max_length=200)
    seleccionado = models.CharField(max_length=100)
    puntos = models.IntegerField()

class Usuario(models.Model):
    nombre = models.CharField(max_length = 32)
    url = models.CharField(max_length = 64)
    titulo_p = models.CharField(max_length = 64)
    fondo = models.CharField(max_length = 32)
    pagina = models.ManyToManyField(Actividad)
    rss =  models.CharField(max_length = 64)
