from django.db import models

class Medicina (models.Model):

    titulo = models.CharField(max_length = 30)
    subtitulo = models.CharField(max_length = 50)
    texto = models.CharField(max_length = 4000)
    autor =  models.CharField(max_length = 30)
    fecha = models.DateField(auto_now_add=True)
    imagen = models.ImageField()

    def __str__ (self):
        return f'Titulo: {self.titulo} | Autor: {self.autor} | Fecha: {self.fecha}'

class Biología (models.Model): 

    titulo = models.CharField(max_length = 30)
    subtitulo = models.CharField(max_length = 50)
    texto = models.CharField(max_length = 4000)
    autor =  models.CharField(max_length = 30)
    fecha = models.DateField(auto_now_add=True)
    imagen = models.ImageField()
    
    def __str__ (self):
        return f'Titulo: {self.titulo} | Autor: {self.autor} | Fecha: {self.fecha}'

class Filosofía (models.Model): 

    titulo = models.CharField(max_length = 30)
    subtitulo = models.CharField(max_length = 50)
    texto = models.CharField(max_length = 4000)
    autor =  models.CharField(max_length = 30)
    fecha = models.DateField(auto_now_add=True)
    imagen = models.ImageField()

    def __str__ (self):
        return f'Titulo: {self.titulo} | Autor: {self.autor} | Fecha: {self.fecha}'

class Astronomía (models.Model): 

    titulo = models.CharField(max_length = 30)
    subtitulo = models.CharField(max_length = 50)
    texto = models.CharField(max_length = 4000)
    autor =  models.CharField(max_length = 30)
    fecha = models.DateField(auto_now_add=True)
    imagen = models.ImageField()

    def __str__ (self):
        return f'Titulo: {self.titulo} | Autor: {self.autor} | Fecha: {self.fecha}'

class Tecnología (models.Model): 

    titulo = models.CharField(max_length = 30)
    subtitulo = models.CharField(max_length = 50)
    texto = models.CharField(max_length = 4000)
    autor =  models.CharField(max_length = 30)
    fecha = models.DateField(auto_now_add=True)
    imagen = models.ImageField()

    def __str__ (self):
        return f'Titulo: {self.titulo} | Autor: {self.autor} | Fecha: {self.fecha}'

class Miembros (models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    foto = models.ImageField() 

    def __str__ (self):
        return f'Nombre: {self.nombre} | Apellido: {self.apellido} | Email: {self.email}'

