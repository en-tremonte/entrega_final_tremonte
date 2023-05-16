from django.shortcuts import render
from blog_vista.models import *
from django.http import HttpResponse


def inicio(request):  #funcion de vista de inicio
    return render (request, 'blog_vista/inicio.html')

def about(request):
    return render (request, 'blog_vista/about.html')

def articulos(request):
    return render (request, 'blog_vista/articulos.html') 

def noticias (request):
    return render (request, 'blog_vista/noticias.html')

def miembros (request):
    return render (request, 'blog_vista/miembros.html')

def buscar (request):
    return render (request, 'blog_vista/buscar.html')