from pathlib import Path
import os #improtamos para llamar a las rutas


BASE_DIR= Path(__file__).resolve().parent.parent
TEMPLATE_DIR = os.path.join(BASE_DIR,'templates') #ruta de la carpeta templates
STATIC_DIR = os.path.join(BASE_DIR,'static') #ruta de la carpeta static


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'NegocioModel',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR], #aqui le decimos a django donde esta la carpeta templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    }
]

STATIC_URL = '/static/' #ruta de la carpeta static
STATICFILES_DIRS = [
    STATIC_DIR,
]

LANGUAGE_CODE = 'es-cl'

TIME_ZONE = 'America/Santiago'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'negocio',
        'USER': 'user_negocio',
        'PASSWORD': 'Holitas01',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    },
}