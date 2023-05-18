from django.shortcuts import render
from blog_vista.models import *
from django.http import HttpResponse

#vistas principales de los models
from django.templatetags.static import static

def my_view(request):
    background_image_url = static('blog_vista/assets/img/home-bg.jpg')
    return render(request, 'padre.html', {'background_image_url': background_image_url})

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

#vistas en listas y detalles de cada model
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

#vistas de los forms: 
from django import forms
from .forms import *
def miembros_form(request): 
    if request.method == 'POST':
        form = MiembrosForm(request.POST)

        if form.is_valid(): 
            informacion = form.cleaned_data
            miembro = Miembros(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], universidad=informacion['universidad'], foto=informacion['foto'])
            miembro.save()
            return render(request, 'blog_vista/inicio.html')
        else:
            print(form.errors)
    
    else:
        form = MiembrosForm()
        
    return render(request, 'blog_vista/miembros_form.html', {'form': form})

def medicina_form(request): 
    if request.method == 'POST':
        form = MedicinaForm(request.POST)

        if form.is_valid(): 
            informacion = form.cleaned_data
            articulo_medicina = Medicina(titulo=informacion['titulo'], subtitulo=informacion['subtitulo'], texto=informacion['texto'], autor=informacion['autor'], imagen=informacion['imagen'])
            articulo_medicina.save()
            return render(request, 'blog_vista/inicio.html')
        else:
            print(form.errors)
    
    else:
        form = MedicinaForm()
        
    return render(request, 'blog_vista/medicina_form.html', {'form': form})


def filosofia_form(request): 
    if request.method == 'POST':
        form = FilosofiaForm(request.POST)

        if form.is_valid(): 
            informacion = form.cleaned_data
            articulo_filosofia = Filosofía(titulo=informacion['titulo'], subtitulo=informacion['subtitulo'], texto=informacion['texto'], autor=informacion['autor'], imagen=informacion['imagen'])
            articulo_filosofia.save()
            return render(request, 'blog_vista/inicio.html')
        else:
            print(form.errors)
    
    else:
        form = FilosofiaForm()
        
    return render(request, 'blog_vista/filosofía_form.html', {'form': form})

def biologia_form(request): 
    if request.method == 'POST':
        form = BiologiaForm(request.POST)

        if form.is_valid(): 
            informacion = form.cleaned_data
            articulo_biologia = Biología(titulo=informacion['titulo'], subtitulo=informacion['subtitulo'], texto=informacion['texto'], autor=informacion['autor'], imagen=informacion['imagen'])
            articulo_biologia.save()
            return render(request, 'blog_vista/inicio.html')
        else:
            print(form.errors)
    
    else:
        form = BiologiaForm()
        
    return render(request, 'blog_vista/biología_form.html', {'form': form})

def astronomia_form(request): 
    if request.method == 'POST':
        form = AstronomiaForm(request.POST)

        if form.is_valid(): 
            informacion = form.cleaned_data
            articulo_astronomia = Astronomía(titulo=informacion['titulo'], subtitulo=informacion['subtitulo'], texto=informacion['texto'], autor=informacion['autor'], imagen=informacion['imagen'])
            articulo_astronomia.save()
            return render(request, 'blog_vista/inicio.html')
        else:
            print(form.errors)
    
    else:
        form = AstronomiaForm()
        
    return render(request, 'blog_vista/astronomía_form.html', {'form': form})

def tecnologia_form(request): 

    if request.method == 'POST':
        form = TecnologiaForm(request.POST)

        if form.is_valid(): 
            informacion = form.cleaned_data
            articulo_tecnologia = Tecnología(titulo=informacion['titulo'], subtitulo=informacion['subtitulo'], texto=informacion['texto'], autor=informacion['autor'], imagen=informacion['imagen'])
            articulo_tecnologia.save()
            return render(request, 'blog_vista/inicio.html')
        else:
            print(form.errors)
    
    else:
        form = TecnologiaForm()
        
    return render(request, 'blog_vista/tecnología_form.html', {'form': form})

#vistas de edicion

from django.views.generic.edit import UpdateView, DeleteView

class MiembrosUpdate(UpdateView):
    model = Miembros
    success_url = 'blog_vista/miembros/list'
    fields = ['nombre', 'apellido', 'email', 'universidad', 'foto']

class MiembrosDelete(DeleteView):
    model = Miembros
    success_url = 'blog_vista/miembros/list'

class AstronomiaUpdate(UpdateView):
    model = Astronomía
    success_url = 'blog_vista/astronomia/list'
    fields = ['titulo', 'subtitulo', 'texto', 'autor', 'imagen']

class AstronomiaDelete(DeleteView):
    model = Astronomía
    success_url = 'blog_vista/astronomia/list'

class BiologiaUpdate(UpdateView):
    model = Biología
    success_url = 'blog_vista/biologia/list'
    fields = ['titulo', 'subtitulo', 'texto', 'autor', 'imagen']

class BiologiaDelete(DeleteView):
    model = Biología
    success_url = 'blog_vista/biologia/list'

class MedicinaUpdate(UpdateView):
    model = Medicina
    success_url = 'blog_vista/medicina/list'
    fields = ['titulo', 'subtitulo', 'texto', 'autor', 'imagen']

class MedicinaDelete(DeleteView):
    model = Medicina
    success_url = 'blog_vista/medicina/list'

class FilosofiaUpdate(UpdateView):
    model = Filosofía
    success_url = 'blog_vista/filosofia/list'
    fields = ['titulo', 'subtitulo', 'texto', 'autor', 'imagen']

class FilosofiaDelete(DeleteView):
    model = Filosofía
    success_url = 'blog_vista/filosofia/list'

class TecnologiaUpdate(UpdateView):
    model = Tecnología
    success_url = 'blog_vista/tecnologia/list'
    fields = ['titulo', 'subtitulo', 'texto', 'autor', 'imagen']

class TecnologiaDelete(DeleteView):
    model = Tecnología
    success_url = 'blog_vista/tecnologia/list'
