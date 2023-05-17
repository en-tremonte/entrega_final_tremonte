from django.urls import path 
from blog_vista import views



urlpatterns = [
    path('', views.inicio, name = 'Inicio'),
    path('about/', views.about, name = 'About'),
    path('medicina', views.medicina, name = 'Medicina'),
    path('miembros/', views.miembros, name = 'Miembros'),
    path('biologia/', views.biologia, name = 'Biologia'),
    path('filosofia/', views.filosofia, name = 'Filosofia'),
    path('astronomia/', views.astronomia, name = 'Astronomia'),
    path('tecnologia/', views.tecnologia, name = 'Tecnologia'),
    path('buscar', views.buscar, name = 'Buscar'),
    path('medicina/list',views.MedicinaList.as_view(),name='MedicinaList'),
    path(r'^(?P<pk>\d+)$', views.MedicinaDetalle.as_view(),name='MedicinaDetail'),
    path('astronomia/list', views.AstronomiaList.as_view(), name = 'AstronomiaList'),
    path(r'^(?P<pk>\d+)$', views.AstronomiaDetalle.as_view(),name='AstronomiaDetail'),
    path('filosofia/list', views.FilosofiaList.as_view(), name = 'FilosofiaList'),
    path(r'^(?P<pk>\d+)$', views.FilosofiaDetalle.as_view(),name='FilosofiaDetail'),
    path('biologia/list', views.BiologiaList.as_view(), name = 'BiologiaList'),
    path(r'^(?P<pk>\d+)$', views.BiologiaDetalle.as_view(),name='BiologiaDetail'),
    path('tecnologia/list', views.TecnologiaList.as_view(), name = 'TecnologiaList'),
    path(r'^(?P<pk>\d+)$', views.TecnologiaDetalle.as_view(),name='TecnologiaDetail'),
    path('miembros/list', views.MiembrosList.as_view(), name = 'MiembrosList'),
    path(r'^(?P<pk>\d+)$', views.MiembrosDetalle.as_view(),name='MiembrosDetail'),
    
]
