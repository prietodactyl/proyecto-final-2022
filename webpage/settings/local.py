from .base import *

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "static"),
)

DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'proyecto-final-2022',
        'USER':'AnaM',
        'PASSWORD':'fatiga1995',
        'HOST':'localhost\SQLEXPRESS',
        'PORT': '',
        'OPTIONS': {
            'DRIVER':'ODBC Driver 17 for SQL Server',
        }
    }
}
