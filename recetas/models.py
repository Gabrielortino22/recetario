# Importa el módulo models de Django.
# Sirve para crear tablas y campos de la base de datos.
from django.db import models


# Define una clase llamada Receta.
# Hereda de models.Model para convertirla en una tabla de la base de datos.
class Receta(models.Model):


    # Lista de opciones permitidas para el campo categoría.
    # Cada tupla tiene:
    # ('valor_guardado', 'texto_visible')
    CATEGORIAS = [

        # Opción Dulce
        ('Dulce', 'Dulce'),

        # Opción Salada
        ('Salada', 'Salada'),
    ]


    # Campo de texto corto.
    # max_length=100 significa máximo 100 caracteres.
    titulo = models.CharField(max_length=100)


    # Campo de texto corto para la categoría.
    categoria = models.CharField(

        # Máximo de caracteres permitidos
        max_length=10,

        # choices obliga a elegir entre las opciones definidas.
        choices=CATEGORIAS
    )


    # Campo de texto largo.
    # Ideal para ingredientes extensos.
    ingredientes = models.TextField()


    # Campo de texto largo para la preparación.
    preparacion = models.TextField()


    # Campo para subir imágenes.
    imagen = models.ImageField(

        # Carpeta dentro de media/ donde se guardarán las imágenes.
        upload_to='recetas/',

        # Permite guardar el campo vacío en la base de datos.
        null=True,

        # Permite dejar el campo vacío en formularios.
        blank=True
    )


    # Campo de fecha y hora.
    # auto_now_add=True guarda automáticamente la fecha de creación.
    fecha = models.DateTimeField(auto_now_add=True)


    # Método especial que define cómo se mostrará el objeto.
    # Ejemplo:
    # en el panel admin aparecerá el título de la receta.
    def __str__(self):

        # Devuelve el título de la receta como texto.
        return self.titulo

     
class Receta(models.Model):

    titulo = models.CharField(max_length=100)

    categoria = models.CharField(max_length=20)

    ingredientes = models.TextField()

    preparacion = models.TextField()

    imagen = models.ImageField(
        upload_to='recetas/',
        blank=True,
        null=True
    )

    video = models.FileField(
        upload_to='videos/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.titulo   
    from django.db import models

class Receta(models.Model):

    titulo = models.CharField(max_length=100)
    categoria = models.CharField(max_length=20)
    ingredientes = models.TextField()
    preparacion = models.TextField()

    imagen = models.ImageField(upload_to='recetas/', blank=True, null=True)

    video = models.FileField(upload_to='videos/', blank=True, null=True)

    fecha = models.DateTimeField(auto_now_add=True)  # 👈 NUEVO

    def __str__(self):
        return self.titulo