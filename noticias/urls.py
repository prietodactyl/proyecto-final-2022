from nturl2path import url2pathname
from urllib.parse import urlparse
from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.ListaNoticias.as_view(), name='noticias'),
    path('crear/', views.CrearNoticias.as_view(), name='crear_noticia'),
    path('editar/', views.editar_noticia, name='editar_noticia'),
    path("detalle/<int:pk>/", views.DetalleNoticia.as_view(), name = "detalle"),
]