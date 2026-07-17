"""
Django settings for config project.
"""  # Archivo principal de configuración del proyecto Django
from pathlib import Path          # Importa la clase Path para trabajar con rutas de archivos y carpetas de forma segura y compatible con distintos sistemas operativos.

import os                         # Importa el módulo os, que permite interactuar con el sistema operativo y acceder a variables de entorno.

from dotenv import load_dotenv    # Importa la función load_dotenv, que carga las variables almacenadas en un archivo .env.


BASE_DIR = Path(__file__).resolve().parent.parent
# __file__ representa la ubicación del archivo settings.py.
# resolve() obtiene la ruta absoluta.
# parent sube un nivel de carpeta.
# parent.parent sube dos niveles.
# El resultado es la carpeta principal del proyecto (BASE_DIR).


load_dotenv(BASE_DIR / ".env")
# Busca el archivo ".env" dentro de la carpeta principal del proyecto
# y carga todas las variables de entorno que contiene para poder
# utilizarlas desde el código mediante os.getenv().
# Quick-start development settings - unsuitable for production  # Configuración rápida para desarrollo
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/  # Documentación oficial


SECRET_KEY = 'django-insecure-dx=we3bj4hp8(*ee*(%ha5-78_6oj^v8@)$qaocgc2&v!_2^%n'  # Clave secreta usada para seguridad interna de Django

DEBUG = True  # Muestra errores detallados mientras desarrollás

ALLOWED_HOSTS = ['*']  # Lista de dominios permitidos


# =========================================================
# APLICACIONES INSTALADAS
# =========================================================

INSTALLED_APPS = [  # Lista de aplicaciones que Django cargará al iniciar el proyecto

    'jazzmin',  # Personaliza y mejora la apariencia del panel de administración de Django

    'django.contrib.admin',  # Activa el panel de administración de Django

    'django.contrib.auth',  # Proporciona el sistema de usuarios, grupos y permisos

    'django.contrib.contenttypes',  # Permite manejar relaciones entre distintos tipos de modelos

    'django.contrib.sessions',  # Permite mantener sesiones de usuarios entre distintas páginas

    'django.contrib.messages',  # Permite mostrar mensajes temporales (éxito, error, advertencia, etc.)

    'django.contrib.staticfiles',  # Gestiona archivos estáticos como CSS, JavaScript e imágenes

    'recetas',  # Tu aplicación personalizada donde está el sistema de recetas
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

        'ENGINE': 'django.db.backends.postgresql',

        'NAME': os.getenv('DB_NAME'),

        'USER': os.getenv('DB_USER'),

        'PASSWORD': os.getenv('DB_PASSWORD'),

        'HOST': os.getenv('DB_HOST'),

        'PORT': os.getenv('DB_PORT'),

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

STATIC_URL = 'static/'                 
# Define la URL pública para acceder a los archivos estáticos
# como CSS, JavaScript e imágenes del diseño.

MEDIA_URL = '/media/'                  
# Define la URL pública para acceder a los archivos que suben
# los usuarios, por ejemplo imágenes o videos de recetas.

MEDIA_ROOT = BASE_DIR / 'media'        
# Indica la carpeta física donde Django guardará los archivos
# multimedia que suban los usuarios.

LOGIN_URL = '/accounts/login/'         
# Especifica la página de inicio de sesión.
# Si un usuario intenta acceder a una vista protegida con
# @login_required sin estar autenticado, será redirigido aquí.

LOGIN_REDIRECT_URL = '/'               
# Después de iniciar sesión correctamente,
# el usuario será redirigido a la página principal.

LOGOUT_REDIRECT_URL = '/'              
# Después de cerrar sesión, inicialmente estaba configurado
# para volver a la página principal.

LOGOUT_REDIRECT_URL = '/accounts/login/'  
# Esta línea reemplaza la configuración anterior.
# Ahora, después de cerrar sesión, el usuario será enviado
# a la página de login.
# Como aparece dos veces, la primera configuración ya no tiene efecto.

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# Configura el sistema de correo de Django para que,
# en lugar de enviar emails reales, los muestre en la consola.
# Es muy útil durante el desarrollo y las pruebas.