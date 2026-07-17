from django.contrib import admin             # Importa el módulo de administración de Django.

from .models import Receta, Perfil           # Importa los modelos Receta y Perfil desde models.py.



# =====================================================
# ADMINISTRACIÓN DE RECETAS
# =====================================================

@admin.register(Receta)                      # Registra el modelo Receta en el panel de administración.
class RecetaAdmin(admin.ModelAdmin):         # Crea una clase para personalizar cómo se muestran las recetas.

    list_display = (                         # Define las columnas que aparecerán en la lista de recetas.

        'titulo',                            # Muestra el título de la receta.

        'categoria',                         # Muestra la categoría (Dulce o Salada).

        'fecha'                              # Muestra la fecha de creación.

    )

    search_fields = (                        # Campos sobre los que funcionará el buscador del administrador.

        'titulo',                            # Permite buscar recetas por el título.

        'ingredientes'                       # Permite buscar recetas por los ingredientes.

    )

    list_filter = (                          # Agrega filtros en el lateral derecho del administrador.

        'categoria',                         # Permite filtrar las recetas por categoría.

    )


# =====================================================
# ADMINISTRACIÓN DE PERFILES
# =====================================================

@admin.register(Perfil)                      # Registra el modelo Perfil en el panel de administración.
class PerfilAdmin(admin.ModelAdmin):         # Personaliza cómo se mostrarán los perfiles.

    list_display = (                         # Columnas que aparecerán en la lista de perfiles.

        'usuario',                           # Muestra el nombre del usuario.

        'rol',                               # Muestra el rol del usuario (Administrador o Lector).

    )

    list_filter = (                          # Agrega filtros para los perfiles.

        'rol',                               # Permite filtrar por tipo de rol.

    )

    search_fields = (                        # Habilita el buscador para los perfiles.

        'usuario__username',                 # Busca por el nombre de usuario relacionado.
                                             # usuario__username accede al campo username del modelo User.

    )


# =====================================================
# PERSONALIZACIÓN DEL PANEL
# =====================================================

admin.site.site_header = "Administración del Recetario"   # Cambia el título que aparece en la parte superior del panel.

admin.site.site_title = "Panel Recetas"                   # Cambia el título que aparece en la pestaña del navegador.

admin.site.index_title = "Bienvenido al panel de recetas" # Cambia el texto de bienvenida en la página principal del administrador.