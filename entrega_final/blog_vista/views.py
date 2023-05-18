from django.shortcuts import render
from blog_vista.models import *
from django.http import HttpResponse


def inicio(request):  
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

from django.views.generic import ListView
from django.views.generic.detail import DetailView

class MedicinaList(ListView):
    model = Medicina 
    template_name='/blog_vista/medicina_list.html'

class AstronomiaList(ListView):
    model = Astronomía
    template_name = 'blog_vista/astronomia_list.html'

class FilosofiaList(ListView):
    model = Filosofía
    template_name = 'blog_vista/filosofia_list.html'

class MedicinaDetalle(DetailView):
    model= Medicina
    template_name= "blog_vista/medicina_detalle.html"


def detalle_astronomia(request, pk):
    astronomia = Astronomía.objects.get(pk=pk)
    contexto = {'astronomia': astronomia}
    return render(request, 'blog_vista/astronomia_detalle.html', contexto)



def detalle_filosofia(request, pk):
    filosofia = Filosofía.objects.get(pk=pk)
    contexto = {'filosofia': filosofia}
    return render(request, 'blog_vista/filosofia_detalle.html', contexto)

class BiologiaList(ListView):
    model = Biología
    template_name = 'blog_vista/biologia_list.html'


def detalle_biologia(request, pk):
    biologia = Biología.objects.get(pk=pk)
    contexto = {'biologia': biologia}
    return render(request, 'blog_vista/biologia_detalle.html', contexto)

class TecnologiaList(ListView):
    model = Tecnología
    template_name = 'blog_vista/tecnologia_list.html'



def detalle_tecnologia(request, pk):
    tecnologia = Tecnología.objects.get(pk=pk)
    contexto = {'tecnologia': tecnologia}
    return render(request, 'blog_vista/tecnologia_detalle.html', contexto)


class MiembrosList(ListView):
    model = Miembros
    template_name = 'blog_vista/miembros_list.html'

class MiembrosDetalle(DetailView):
    model = Miembros
    template_name = 'blog_vista/miembros_detalle.html'

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class MedicinaCreacion(CreateView):
    model = Medicina
    success_url= 'blog_vista/medicina/list'
    fields = ['titulo', 'subtitulo', 'texto', 'imagen', 'autor']



