from asyncio.windows_events import NULL
from pickle import TRUE
from django.db import models

from django.utils import timezone

from usuarios.models import Usuario


# Create your models here.
class Noticia(models.Model):

    author = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=TRUE)

    title = models.CharField(max_length=200)

    text = models.TextField()

    picture = models.ImageField(upload_to="fotos_noticias", null=True, blank=True)

    created_date = models.DateTimeField(

            default=timezone.now)

    published_date = models.DateTimeField(

            blank=True, null=True)
    

    def publish(self):

        self.published_date = timezone.now()

        self.save()


    def __str__(self):

        return self.title

class Comentario(models.Model):

    creator = models.ForeignKey(Usuario, on_delete= models.CASCADE)

    noticia = models.ForeignKey(Noticia, related_name= "comentarios", on_delete= models.CASCADE)    

    comment = models.TextField()

    date_added = models.DateTimeField(auto_now_add=True)
    
