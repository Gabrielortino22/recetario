from django.contrib import admin
from .models import Receta


@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):

    list_display = (
        'titulo',
        'categoria',
        'fecha'
    )

    search_fields = (
        'titulo',
        'ingredientes'
    )

    list_filter = (
        'categoria',
    )


admin.site.site_header = "Administración del Recetario"

admin.site.site_title = "Panel Recetas"

admin.site.index_title = "Bienvenido al panel de recetas"