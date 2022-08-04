from nturl2path import url2pathname
from urllib.parse import urlparse
from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('quienes_somos', views.quienes_somos, name='quienes_somos'),
    path('noticias', views.noticias, name='noticias'),
    path('noticias/crear', views.crear_noticia, name='crear_noticia'),
    path('noticias/editar', views.editar_noticia, name='editar_noticia'),
    path('descargas', views.descargas, name='descargas'),
    path('contacto', views.contacto, name='contacto')
]