from django.db import models
from django.contrib.auth.models import User


# ==========================================
# RECETAS
# ==========================================

class Receta(models.Model):

    CATEGORIAS = [

        ('Dulce', 'Dulce'),

        ('Salada', 'Salada'),
    ]

    titulo = models.CharField(
        max_length=100
    )

    categoria = models.CharField(
        max_length=20,
        choices=CATEGORIAS
    )

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

    fecha = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.titulo


# ==========================================
# PERFIL DE USUARIO
# ==========================================

class Perfil(models.Model):

    ROLES = [

        ('editor', 'Editor'),

        ('lector', 'Lector'),
    ]

    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    rol = models.CharField(
        max_length=20,
        choices=ROLES,
        default='lector'
    )

    # 📷 Foto del usuario
    foto = models.ImageField(
        upload_to='perfiles/',
        blank=True,
        null=True
    )

    # 📅 Fecha de creación del perfil
    fecha_registro = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.usuario.username} ({self.rol})"