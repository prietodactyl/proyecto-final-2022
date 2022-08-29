from django.db import models
from django.contrib.auth.models import User


class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=255)
    address = models.CharField(max_length=255)
    zip_code = models.CharField('Zip Code', max_length=10, blank=True)
    phone = models.CharField('Contact Phone', max_length=25, blank=True)
    web = models.URLField('Website Address')
    email_address = models.EmailField('Email Address', blank=True)

    def __str__(self):
        return self.name


class Usuario(models.Model):
    first_name = models.CharField('Nombre', max_length=30)
    last_name = models.CharField('Apellido', max_length=30)
    email = models.EmailField('User Email')

    def __str__(self):
        return self.first_name + ' ' + self.last_name



class Event(models.Model):
    name = models.CharField('Evento', max_length=120)
    event_date = models.DateTimeField('Fecha del evento')
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    # venue = models.CharField(max_length=120)
    #manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

