from nturl2path import url2pathname
from urllib.parse import urlparse
from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.noticias, name='noticias'),
    path('/crear', views.crear_noticia, name='crear_noticia'),
    path('/editar', views.editar_noticia, name='editar_noticia'),
]