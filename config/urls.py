from django.contrib import admin          # Importa el panel de administración de Django.
from django.urls import path, include     # path crea rutas; include permite importar rutas de otras aplicaciones.
from django.conf import settings          # Importa la configuración del proyecto (settings.py).
from django.conf.urls.static import static # Permite servir archivos media (imágenes) durante el desarrollo.

from recetas import views                 # Importa las vistas de la aplicación "recetas".


urlpatterns = [                           # Lista donde se definen todas las URLs del proyecto.

    # -------------------------------
    # Rutas de la aplicación Recetas
    # -------------------------------

    path(                                 # Define una nueva ruta.
        '',                               # Ruta vacía: corresponde a la página principal (http://127.0.0.1:8000/).
        include('recetas.urls')           # Importa todas las rutas definidas en recetas/urls.py.
    ),

    # -------------------------------
    # Registro de usuarios
    # -------------------------------

    path(                                 # Nueva ruta.
        'accounts/registro/',             # URL para registrar un usuario.
        views.registro_usuario,           # Vista que procesa el registro.
        name='registro'                   # Nombre de la ruta para usar con {% url 'registro' %}.
    ),

    # -------------------------------
    # Login personalizado
    # -------------------------------

    path(                                 # Nueva ruta.
        'accounts/login/',                # URL donde los usuarios inician sesión.
        views.login_usuario,              # Vista personalizada para el login.
        name='login'                      # Nombre de la ruta.
    ),

    # -------------------------------
    # Otras funciones de autenticación
    # -------------------------------

    path(                                 # Nueva ruta.
        'accounts/',                      # Todas las rutas comenzarán con /accounts/.
        include('django.contrib.auth.urls') # Incluye las rutas que ya trae Django:
                                           # logout/
                                           # password_change/
                                           # password_change/done/
                                           # password_reset/
                                           # password_reset/done/
                                           # reset/<uidb64>/<token>/
                                           # reset/done/
    ),

    # -------------------------------
    # Panel de administración
    # -------------------------------

    # Si algún día querés volver a usar el administrador de Django,
    # simplemente descomentás la siguiente línea:

    # path('admin/', admin.site.urls),    # Habilita el panel de administración.

]


# --------------------------------------------------
# Configuración para mostrar archivos subidos (Media)
# --------------------------------------------------

urlpatterns += static(                    # Agrega rutas especiales para servir archivos media.

    settings.MEDIA_URL,                   # URL pública donde se accederá a las imágenes (por ejemplo /media/).

    document_root=settings.MEDIA_ROOT     # Carpeta física donde se guardan las imágenes.

)