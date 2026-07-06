from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from recetas import views


urlpatterns = [

    # Rutas de la aplicación
    path(
        '',
        include('recetas.urls')
    ),

    path(
        'accounts/registro/',
        views.registro_usuario,
        name='registro'
    ),


    # Login personalizado
    path(
        'accounts/login/',
        views.login_usuario,
        name='login'
    ),

    # Logout, cambio de contraseña, recuperar contraseña, etc.
    path(
        'accounts/',
        include('django.contrib.auth.urls')
    ),



    # Si algún día querés volver a usar el admin
    # path('admin/', admin.site.urls),

]


urlpatterns += static(

    settings.MEDIA_URL,

    document_root=settings.MEDIA_ROOT

)