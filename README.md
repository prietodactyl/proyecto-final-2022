# Proyecto de aplicación Web tipo Blog

Informatorio 2022 - Grupo 2 - Comisión 4

El objetivo de este proyecto es desarrollar una aplicación web que tenga funcionalidades tipo blog, para subir noticias, comentarlas, editarlas, etc., todo ello usando el framework Django, el cual se utilizó durante la cursada del Informatorio.

La organización para la cual realizamos el proyecto es una Institución educativa "U.E.G.P. Nº 161 "Instituto Barranqueras" que implementa la formación Técnica en Economía Social y Desarrollo Local en la Provincia del Chaco.

El trabajo se realizó de manera grupal, dividiendo funciones y utilizando github con el fin de facilitar esta metodología.

Este trabajo tenía ciertos requisitos básicos a tener en cueneta, por ejemplo que hubiera dos tipos de perfil, admin y visitante. Cada uno de ellos con diferentes funciones y privilegios.


## Para obtener una copia del proyecto debemos realizar los siguientes pasos:

* Creamos una carpeta donde vamos a colocar el repositorio
* Abrimos Visual Studio Code o el software de edición que utilicemos.
* Abrimos la carpeta contenedora
* Con VS code iniciamos una nueva terminal dentro de esa carpeta
* Copiamos la dirección del repositorio de la página github.com
* Utilizamos el siguiente comando: git clone "dirección que copiamos previamente sin comillas"
* Nos movemos a la carpeta que se creó
* Ahora es recomendable crear un entorno virtual. Para ello, desde la terminal que abrimos, usamos el comando: "python -m venv env" - sin comillas.(crea el entorno virtual env)
* Activamos el entorno virtual
* Instalamos las dependencias necesarias con el comando: "pip install -r requeriments.txt
* Ahora es necesario realizar una migración, para ello se utiliza el comando: "python manage.py migrate"
* En caso que todo se haya realizado correctamente, estamos en condiciones de ejecutar el servidor con el comando: "python manage.py runserver"
* Ahora desde nuestro navegador web entramos a la dirección: "127.0.0.1:8000" y tendremos acceso a nuestra página Web.

_Tener en cuenta que se encuentra ignorado el archivo "local.py" por lo cual deberán crear un archivo con ese nombre, la cual quedará dentro de una carpeta settings (a nivel proyecto) junto a "base.py"._
El archivo "local.py" debe tener el siguiente formato:
```
from .base import *

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "static"),
)

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'engine-name',
        'NAME': 'db name',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'host name',
        'PORT': '',
        'OPTIONS': {
            'driver': 'driver correspondiente',
        }       
    }
}
```
_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._


## Herramientas que utilizamos en el proyecto

    Django - El framework web usado
    Python - Lenguaje utilizado
    Visual Studio Code - Editor de texto
    HTML, CSS, Bootstrap


## Participantes del proyecto:
* Agustín Prieto
* Ana Mazal
* Fernando Bergagno
* Santiago Pagno

## Links de interés:
* Informatorio - https://empleo.chaco.gob.ar/informatorio#/
* Instituto Barranqueras - https://www.facebook.com/institutobarranqueras
* Video de la página en funcionamiento - https://www.youtube.com/watch?v=2LKWnX_UosM

