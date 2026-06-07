"""
Django settings for config project.
"""  # Archivo principal de configuración del proyecto Django

from pathlib import Path  #importa la clase Path, que sirve para trabajar con rutas (paths) de archivos y carpetas de una manera más simple y segura.

BASE_DIR = Path(__file__).resolve().parent.parent  # Guarda la ruta principal del proyecto


# Quick-start development settings - unsuitable for production  # Configuración rápida para desarrollo
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/  # Documentación oficial


SECRET_KEY = 'django-insecure-dx=we3bj4hp8(*ee*(%ha5-78_6oj^v8@)$qaocgc2&v!_2^%n'  # Clave secreta usada para seguridad interna de Django

DEBUG = True  # Muestra errores detallados mientras desarrollás

ALLOWED_HOSTS = []  # Lista de dominios permitidos


# =========================================================
# APLICACIONES INSTALADAS
# =========================================================

INSTALLED_APPS = [
     'jazzmin',

    'django.contrib.admin',  # Panel de administración de Django

    'django.contrib.auth',  # Sistema de autenticación y usuarios

    'django.contrib.contenttypes',  # Manejo de tipos de contenido

    'django.contrib.sessions',  # Manejo de sesiones de usuarios

    'django.contrib.messages',  # Sistema de mensajes temporales

    'django.contrib.staticfiles',  # Manejo de archivos estáticos

    'recetas',  # Aplicación personalizada del proyecto
]


# =========================================================
# MIDDLEWARE
# =========================================================

MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',  # Seguridad general del proyecto

    'django.contrib.sessions.middleware.SessionMiddleware',  # Manejo de sesiones

    'django.middleware.common.CommonMiddleware',  # Funciones comunes de Django

    'django.middleware.csrf.CsrfViewMiddleware',  # Protección contra ataques CSRF

    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Manejo de usuarios autenticados

    'django.contrib.messages.middleware.MessageMiddleware',  # Sistema de mensajes

    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Protección contra clickjacking
]


ROOT_URLCONF = 'config.urls'  # Archivo principal de rutas del proyecto


# =========================================================
# CONFIGURACIÓN DE TEMPLATES
# =========================================================

TEMPLATES = [  # Lista de configuraciones del sistema de templates de Django
    {

        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Motor de templates que utilizará Django

        'DIRS': [BASE_DIR / 'templates'],  # Carpetas adicionales donde Django buscará archivos HTML

        'APP_DIRS': True,  # Busca automáticamente templates dentro de cada app instalada

        'OPTIONS': {  # Configuraciones extra del motor de templates

            'context_processors': [  # Variables que estarán disponibles automáticamente en todos los templates

                'django.template.context_processors.request',  # Agrega el objeto request a los templates

                'django.contrib.auth.context_processors.auth',  # Agrega información del usuario autenticado

                'django.contrib.messages.context_processors.messages',  # Agrega el sistema de mensajes de Django
            ],
        },
    },
]


WSGI_APPLICATION = 'config.wsgi.application'  # Punto de entrada WSGI para producción


# =========================================================
# BASE DE DATOS
# =========================================================

DATABASES = {
    'default': {

        'ENGINE': 'django.db.backends.sqlite3',  # Usa SQLite como motor de base de datos

        'NAME': BASE_DIR / 'db.sqlite3',  # Nombre y ubicación de la base de datos
    }
}


# =========================================================
# VALIDADORES DE CONTRASEÑAS
# =========================================================

AUTH_PASSWORD_VALIDATORS = [

    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # Evita contraseñas parecidas al usuario
    },

    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # Exige longitud mínima
    },

    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # Bloquea contraseñas comunes
    },

    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # Evita contraseñas solo numéricas
    },
]


# =========================================================
# INTERNACIONALIZACIÓN
# =========================================================

LANGUAGE_CODE = 'es-ar'  # Idioma principal del proyecto

TIME_ZONE = 'UTC'  # Zona horaria del proyecto

USE_I18N = True  # Activa traducciones internacionales

USE_TZ = True  # Activa soporte de zonas horarias


# =========================================================
# ARCHIVOS ESTÁTICOS
# =========================================================

STATIC_URL = 'static/'  # URL para acceder a archivos estáticos

MEDIA_URL = '/media/'  # URL para acceder a archivos subidos

MEDIA_ROOT = BASE_DIR / 'media'  # Carpeta física donde se guardan los archivos media

LOGIN_URL = '/accounts/login/'

LOGIN_REDIRECT_URL = '/'

LOGOUT_REDIRECT_URL = '/'

LOGOUT_REDIRECT_URL = '/accounts/login/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'