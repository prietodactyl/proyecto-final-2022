from nturl2path import url2pathname
from urllib.parse import urlparse
from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.ListaNoticias.as_view(), name='noticias'),
    path('crear/', views.CrearNoticias.as_view(), name='crear_noticia'),
    path('editar/<int:pk>', views.EditarNoticia.as_view(), name='editar_noticia'),
    path("detalle/<int:pk>/", views.DetalleNoticia.as_view(), name = 'detalle'),
    path("borrar/<int:pk>/", views.BorrarNoticia.as_view(), name = 'borrar'),
    path("comentar/<int:pk>", views.CrearComentario.as_view(), name = 'comentar'),
    path("borrar-comentario/<int:pk>", views.BorrarComentario.as_view(), name = 'borrar-comentario'),
]