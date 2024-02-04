from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from .models import Post

User = get_user_model()

@receiver(post_save, sender=User)
def asignar_permiso_add_post(sender, instance, created, **kwargs):
    if created:
        # Obtener el content type del modelo Post
        content_type = ContentType.objects.get_for_model(Post)

        # Crear el permiso 'add_post' si no existe
        if not Permission.objects.filter(content_type=content_type, codename='add_post').exists():
            add_post_permission = Permission.objects.create(
                codename='add_post',
                name='Can add post',
                content_type=content_type,
            )

        # Asignar el permiso 'add_post' al usuario recién creado (CustomUser)
        add_post_perm = Permission.objects.get(codename='add_post')
        instance.user_permissions.add(add_post_perm)
