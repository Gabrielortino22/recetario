from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from .models import Perfil


@receiver(post_save, sender=User)
def crear_perfil(sender, instance, created, **kwargs):

    if created:

        # Si es un superusuario será Editor.
        # Si no, será Lector.
        rol = "editor" if instance.is_superuser else "lector"

        Perfil.objects.create(
            usuario=instance,
            rol=rol
        )


@receiver(post_save, sender=User)
def guardar_perfil(sender, instance, **kwargs):

    Perfil.objects.get_or_create(usuario=instance)

    instance.perfil.save()