from django.db import models                    # Importa el módulo de modelos de Django para crear tablas en la base de datos.
from django.contrib.auth.models import User     # Importa el modelo User que trae Django para gestionar usuarios.


# ==========================================
# RECETAS
# ==========================================

class Receta(models.Model):                     # Define el modelo Receta. Cada objeto será un registro de la tabla recetas.

    CATEGORIAS = [                              # Lista de opciones disponibles para el campo categoría.

        ('Dulce', 'Dulce'),                     # Valor guardado en la base de datos y texto que verá el usuario.

        ('Salada', 'Salada'),                   # Segunda opción de categoría.
    ]

    titulo = models.CharField(                  # Campo de texto corto para el título de la receta.
        max_length=100                          # Permite almacenar hasta 100 caracteres.
    )

    categoria = models.CharField(               # Campo de texto para la categoría.
        max_length=20,                          # Longitud máxima de 20 caracteres.
        choices=CATEGORIAS                      # Solo permite elegir entre Dulce o Salada.
    )

    ingredientes = models.TextField()           # Campo de texto largo para los ingredientes.

    preparacion = models.TextField()            # Campo de texto largo para explicar la preparación.

    imagen = models.ImageField(                 # Campo para guardar una imagen de la receta.
        upload_to='recetas/',                   # Las imágenes se guardarán en la carpeta media/recetas/.
        blank=True,                             # El campo puede dejarse vacío en los formularios.
        null=True                               # En la base de datos puede guardar un valor nulo.
    )

    video = models.FileField(                   # Campo para subir un archivo de video.
        upload_to='videos/',                    # Los videos se guardarán en la carpeta media/videos/.
        blank=True,                             # No es obligatorio subir un video.
        null=True                               # Puede quedar vacío en la base de datos.
    )

    fecha = models.DateTimeField(               # Campo que almacena fecha y hora.
        auto_now_add=True                       # Guarda automáticamente la fecha y hora al crear la receta.
    )

    def __str__(self):                          # Método que define cómo se mostrará el objeto.
        return self.titulo                      # Cuando se imprima una receta se verá su título.


# ==========================================
# PERFIL DE USUARIO
# ==========================================

class Perfil(models.Model):                     # Define el modelo Perfil. Cada objeto será un registro de la tabla perfiles.

    ROLES = [                                   # Lista de roles posibles para los usuarios.

        ('editor', 'Editor'),                   # Rol con permisos para modificar contenido.

        ('lector', 'Lector'),                   # Rol con permisos solo de lectura.
    ]

    usuario = models.OneToOneField(             # Relación uno a uno con el modelo User.
        User,                                   # Se relaciona con un usuario del sistema.
        on_delete=models.CASCADE                # Si el usuario se elimina, su perfil también se elimina.
    )

    rol = models.CharField(                     # Campo para almacenar el rol del usuario.
        max_length=20,                          # Longitud máxima de 20 caracteres.
        choices=ROLES,                          # Solo permite Editor o Lector.
        default='lector'                        # Si no se especifica, el rol será Lector.
    )

    # 📷 Foto del usuario
    foto = models.ImageField(                   # Campo para almacenar una imagen del perfil.
        upload_to='perfiles/',                  # Las imágenes se guardarán en media/perfiles/.
        blank=True,                             # No es obligatorio subir una foto.
        null=True                               # Puede quedar vacía en la base de datos.
    )

    # 📅 Fecha de creación del perfil
    fecha_registro = models.DateTimeField(      # Campo para guardar la fecha de creación del perfil.
        auto_now_add=True                       # Se completa automáticamente al crear el perfil.
    )

    def __str__(self):                          # Define cómo se mostrará un perfil.
        return f"{self.usuario.username} ({self.rol})"   # Muestra el nombre del usuario y su rol.