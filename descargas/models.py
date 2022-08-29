from django.db import models
from asyncio.windows_events import NULL
from pickle import TRUE
from django.utils import timezone
from usuarios.models import Usuario

class Archivo(models.Model):

    author = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=TRUE)

    title = models.CharField(max_length=200)

    description = models.TextField()

    archive = models.FileField(upload_to="archivos", null=False, blank=False)

    created_date = models.DateTimeField(

            default=timezone.now)
    

    def publish(self):

        self.published_date = timezone.now()

        self.save()


    def __str__(self):

        return self.title