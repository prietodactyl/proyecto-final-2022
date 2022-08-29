# Generated by Django 4.0.7 on 2022-08-29 02:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=30, verbose_name='Apellido')),
                ('email', models.EmailField(max_length=254, verbose_name='User Email')),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Venue Name')),
                ('address', models.CharField(max_length=255)),
                ('zip_code', models.CharField(blank=True, max_length=10, verbose_name='Zip Code')),
                ('phone', models.CharField(blank=True, max_length=25, verbose_name='Contact Phone')),
                ('web', models.URLField(verbose_name='Website Address')),
                ('email_address', models.EmailField(blank=True, max_length=254, verbose_name='Email Address')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Evento')),
                ('event_date', models.DateTimeField(verbose_name='Fecha del evento')),
                ('description', models.TextField(blank=True)),
                ('attendees', models.ManyToManyField(blank=True, to='calendario.usuario')),
                ('venue', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='calendario.venue')),
            ],
        ),
    ]