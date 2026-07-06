from django.contrib import admin

from .models import Receta, Perfil



# =====================================================
# ADMINISTRACIÓN DE RECETAS
# =====================================================

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


# =====================================================
# ADMINISTRACIÓN DE PERFILES
# =====================================================

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):

    list_display = (

        'usuario',

        'rol',

    )

    list_filter = (

        'rol',

    )

    search_fields = (

        'usuario__username',

    )


# =====================================================
# PERSONALIZACIÓN DEL PANEL
# =====================================================

admin.site.site_header = "Administración del Recetario"

admin.site.site_title = "Panel Recetas"

admin.site.index_title = "Bienvenido al panel de recetas"