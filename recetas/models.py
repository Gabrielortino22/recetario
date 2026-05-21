from django.db import models

class Receta(models.Model):

    CATEGORIAS = [
        ('Dulce', 'Dulce'),
        ('Salada', 'Salada'),
    ]

    titulo = models.CharField(max_length=100)

    categoria = models.CharField(
        max_length=10,
        choices=CATEGORIAS
    )

    ingredientes = models.TextField()

    preparacion = models.TextField()

    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo