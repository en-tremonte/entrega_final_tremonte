from django.db import models

class Articulos (models.Model):

    titulo = models.CharField(max_length = 30)
    subtitulo = models.CharField(max_length = 50)
    texto = models.CharField(max_length = 4000)
    autor =  models.CharField(max_length = 30)
    fecha = models.DateField()
    imagen = models.ImageField()

class Noticias (models.Model): 

    titulo = models.CharField(max_length = 30)
    subtitulo = models.CharField(max_length = 50)
    texto = models.CharField(max_length = 4000)
    autor =  models.CharField(max_length = 30)
    fecha = models.DateField()
    imagen = models.ImageField()

class Miembros (models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    foto = models.ImageField() 

