from django.contrib import admin  # Importa el panel de administración de Django

from django.urls import path, include  # path crea rutas e include importa rutas de otras apps

from django.conf import settings  # Importa las configuraciones del proyecto desde settings.py

from django.conf.urls.static import static  # Permite mostrar archivos media en desarrollo


urlpatterns = [  # Lista principal de rutas del proyecto

    path('admin/', admin.site.urls),  # Ruta del panel administrador -> /admin/

    path('', include('recetas.urls')),  # Incluye las rutas definidas en recetas/urls.py
]


urlpatterns += static(  # Agrega soporte para mostrar archivos media

    settings.MEDIA_URL,  # URL pública de acceso a archivos media

    document_root=settings.MEDIA_ROOT  # Carpeta física donde se guardan los archivos
)