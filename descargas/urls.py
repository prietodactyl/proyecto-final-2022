from nturl2path import url2pathname
from urllib.parse import urlparse
from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.ListaDescargas.as_view(), name='descargas'),
    path('crear/', views.CrearDescarga.as_view(), name='cargar_archivo'),
    path("borrar/<int:pk>/", views.BorrarArchivo.as_view(), name = 'borrar_archivo'),
]