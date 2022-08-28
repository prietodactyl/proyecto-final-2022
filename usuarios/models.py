from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    es_administrador=models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + " " + self.last_name