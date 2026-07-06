from django.urls import path  # Importa la función path para crear rutas URL desde el paquete principal de django y el modulo .urls

from . import views  # Importa el archivo views.py ubicado en la misma carpeta que urls.py para poder usar sus funciones


urlpatterns = [  # Lista que contiene todas las rutas de la aplicación

    path('', views.lista_recetas, name='lista'),  # Cuando se accede a la raíz (/) ejecuta la función lista_recetas y la ruta se llama 'lista'

    
    path('crear/', views.crear_receta, name='crear'),  # URL /crear/ ejecuta la función crear_receta y la ruta se llama 'crear'

    path('prueba/', views.prueba_receta, name='prueba'),  # URL /crear/ ejecuta la función crear_receta y la ruta se llama 'crear'

    path('prueba_2/', views.prueba_2_receta, name='prueba_2'),  # URL /crear/ ejecuta la función crear_receta y la ruta se llama 'crear'

    path('editar/<int:id>/', views.editar_receta, name='editar'),  # URL /editar/1/ o /editar/5/ pasa el id a editar_receta

    path('eliminar/<int:id>/', views.eliminar_receta, name='eliminar'),  # URL /eliminar/1/ o /eliminar/5/ pasa el id a eliminar_receta
]