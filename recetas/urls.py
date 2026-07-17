from django.urls import path             # Importa la función path, que permite crear rutas o URLs.

from . import views                      # Importa el archivo views.py de la misma aplicación.


urlpatterns = [                          # Lista que contiene todas las rutas de la aplicación.

    path('', views.lista_recetas, name='lista'),
    # Cuando el usuario entra a la página principal de la aplicación,
    # se ejecuta la función lista_recetas.
    # El nombre "lista" permite referenciar esta ruta desde las plantillas.

    path('crear/', views.crear_receta, name='crear'),
    # URL para crear una nueva receta.
    # Ejecuta la vista crear_receta.

    path('editar/<int:id>/', views.editar_receta, name='editar'),
    # URL para editar una receta.
    # <int:id> indica que la URL recibirá un número entero.
    # Ese número corresponde al ID de la receta que se quiere modificar.

    path('eliminar/<int:id>/', views.eliminar_receta, name='eliminar'),
    # URL para eliminar una receta.
    # También recibe el ID de la receta que se desea borrar.


    # ==========================
    # USUARIOS
    # ==========================

    path(
        'usuarios/',                      # URL para mostrar la lista de usuarios.
        views.lista_usuarios,             # Ejecuta la vista lista_usuarios.
        name='usuarios'                   # Nombre de la ruta.
    ),

    path(
        'usuarios/cambiar/<int:id>/',     # URL para cambiar el rol de un usuario.
        views.cambiar_rol,                # Ejecuta la vista cambiar_rol.
        name='cambiar_rol'                # Nombre de la ruta.
    ),

]