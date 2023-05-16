from django.urls import path 
from blog_vista import views



urlpatterns = [
    path('', views.inicio, name = 'Inicio'),
    path('about/', views.about, name = 'About'),
    path('articulos/', views.articulos, name = 'Articulos'),
    path('miembros/', views.miembros, name = 'Miembros'),
    path('noticias/', views.noticias, name = 'Noticias'),
    path('buscar', views.buscar, name = 'Buscar'),

]
