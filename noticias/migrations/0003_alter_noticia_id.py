# Generated by Django 4.0.7 on 2022-08-28 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0002_noticia_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
