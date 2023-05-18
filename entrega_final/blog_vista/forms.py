from django import forms
from .models import *




class MiembrosForm(forms.ModelForm):
    class Meta:
        model = Miembros
        fields = ['nombre', 'apellido', 'email', 'universidad', 'foto']
        widgets = {'foto': forms.FileInput()}

class MedicinaForm(forms.ModelForm):
    class Meta:
        model = Medicina
        fields = ['titulo', 'subtitulo', 'texto', 'autor', 'imagen']
        widgets = {'imagen': forms.FileInput()}

class BiologiaForm(forms.ModelForm):
    class Meta:
        model = Biología
        fields = ['titulo', 'subtitulo', 'texto', 'autor', 'imagen']
        widgets = {'imagen': forms.FileInput()}

class FilosofiaForm(forms.ModelForm):
    class Meta:
        model = Filosofía
        fields = ['titulo', 'subtitulo', 'texto', 'autor', 'imagen']
        widgets = {'imagen': forms.FileInput()}
    
class AstronomiaForm(forms.ModelForm):
    class Meta:
        model = Astronomía
        fields = ['titulo', 'subtitulo', 'texto', 'autor', 'imagen']
        widgets = {'imagen': forms.FileInput()}

class TecnologiaForm(forms.ModelForm):
    class Meta:
        model = Tecnología
        fields = ['titulo', 'subtitulo', 'texto', 'autor', 'imagen']
        widgets = {'imagen': forms.FileInput()}






