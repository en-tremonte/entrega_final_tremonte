from django.urls import path 
from blog_vista import views

from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('about/', views.about, name='About'),
    path('medicina/', views.medicina, name='Medicina'),
    path('miembros/', views.miembros, name='Miembros'),
    path('biologia/', views.biologia, name='Biologia'),
    path('filosofia/', views.filosofia, name='Filosofia'),
    path('astronomia/', views.astronomia, name='Astronomia'),
    path('tecnologia/', views.tecnologia, name='Tecnologia'),
    path('buscar/', views.buscar, name='Buscar'),
    path('medicina/list', views.MedicinaList.as_view(), name='MedicinaList'),
    path('medicina/detalle/<int:pk>', views.MedicinaDetalle.as_view(), name='MedicinaDetail'),
    path('astronomia/list', views.AstronomiaList.as_view(), name='AstronomiaList'),
    path('astronomia/detalle/<int:pk>', views.detalle_astronomia, name='AstronomiaDetail'),
    path('filosofia/list', views.FilosofiaList.as_view(), name='FilosofiaList'),
    path('filosofia/detalle/<int:pk>', views.detalle_filosofia, name='FilosofiaDetail'),
    path('biologia/list', views.BiologiaList.as_view(), name='BiologiaList'), 
    path('biologia/detalle/<int:pk>', views.detalle_biologia, name='BiologiaDetail'),
    path('tecnologia/list', views.TecnologiaList.as_view(), name='TecnologiaList'),
    path('tecnologia/detalle/<int:pk>', views.detalle_tecnologia, name = 'TecnologiaDetail'),
    path('miembros/list', views.MiembrosList.as_view(), name='MiembrosList'),
    path('miembros/detalle/<int:pk>', views.MiembrosDetalle.as_view(), name='MiembrosDetail'),
    path('miembrosForm', views.miembros_form, name = 'MiembrosForm'),
    path('medicinaForm', views.medicina_form, name ='MedicinaForm' ),
    path('biologiaForm', views.biologia_form, name ='BiologiaForm' ),
    path('astronomiaForm', views.astronomia_form, name ='AstronomiaForm' ),
    path('filosofiaForm', views.filosofia_form, name ='FilosofiaForm' ),
    path('tecnologiaForm', views.tecnologia_form, name ='TecnologiaForm' ),
]




    

