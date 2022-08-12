from nturl2path import url2pathname
from urllib.parse import urlparse
from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.descargas, name='descargas'),
]