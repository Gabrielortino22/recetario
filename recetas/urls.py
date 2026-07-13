from django.urls import path

from . import views


urlpatterns = [

    path('', views.lista_recetas, name='lista'),

    path('crear/', views.crear_receta, name='crear'),

    path('editar/<int:id>/', views.editar_receta, name='editar'),

    path('eliminar/<int:id>/', views.eliminar_receta, name='eliminar'),

    # ==========================
    # USUARIOS
    # ==========================

    path(
        'usuarios/',
        views.lista_usuarios,
        name='usuarios'
    ),

    path(
        'usuarios/cambiar/<int:id>/',
        views.cambiar_rol,
        name='cambiar_rol'
    ),

]