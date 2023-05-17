from django.shortcuts import render
from blog_vista.models import *
from django.http import HttpResponse


def inicio(request):  #funcion de vista de inicio
    return render (request, 'blog_vista/inicio.html')

def about(request):
    return render (request, 'blog_vista/about.html')

def medicina(request):
    return render (request, 'blog_vista/medicina.html') 

def biologia (request):
    return render (request, 'blog_vista/biologia.html')

def filosofia (request):
    return render (request, 'blog_vista/filosofia.html')

def astronomia(request):
    return render (request, 'blog_vista/astronomia.html')

def tecnologia (request):
    return render (request, 'blog_vista/tecnologia.html')

def miembros (request):
    return render (request, 'blog_vista/miembros.html')

def buscar (request):
    return render (request, 'blog_vista/buscar.html')