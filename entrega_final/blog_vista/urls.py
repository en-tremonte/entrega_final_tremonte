from django.urls import path 
from blog_vista import views



urlpatterns = [
    path('', views.inicio, name = 'Inicio'),
    path('about/', views.about, name = 'About'),
    path('medicina/', views.medicina, name = 'Medicina'),
    path('miembros/', views.miembros, name = 'Miembros'),
    path('biologia/', views.biologia, name = 'Biologia'),
    path('filosofia/', views.filosofia, name = 'Filosofia'),
    path('astronomia/', views.astronomia, name = 'Astronomia'),
    path('tecnologia/', views.tecnologia, name = 'Tecnologia'),
    path('buscar', views.buscar, name = 'Buscar'),

]
