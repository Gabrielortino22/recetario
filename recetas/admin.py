from django.contrib import admin  # Importa el módulo de administración de Django

from .models import Receta  # Importa el modelo Receta desde models.py


@admin.register(Receta)  # Registra el modelo Receta en el panel de administración
class RecetaAdmin(admin.ModelAdmin):  # Crea una configuración personalizada para mostrar Receta en el admin

    list_display = (  # Define las columnas que se mostrarán en la lista de recetas

        'titulo',  # Muestra el campo título

        'categoria',  # Muestra el campo categoría

        'fecha'  # Muestra la fecha de creación
    )

    search_fields = (  # Campos sobre los que funcionará el buscador del admin

        'titulo',  # Permite buscar por título

        'ingredientes'  # Permite buscar palabras dentro de ingredientes
    )

    list_filter = (  # Agrega filtros en el lateral derecho del panel admin

        'categoria',  # Permite filtrar recetas por categoría
    )


admin.site.site_header = "Administración del Recetario"  # Cambia el encabezado principal que aparece en la parte superior del panel de administración de Django

admin.site.site_title = "Panel Recetas"  # Cambia el título HTML del panel de administración que aparece en la pestaña del navegador

admin.site.index_title = "Bienvenido al panel de recetas"  # Cambia el título que aparece en la página principal del panel de administración, debajo del encabezado principal