# Generated by Django 4.2.3 on 2023-11-18 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repositorio', '0005_customuser_foto_perfil_alter_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='foto_perfil',
            field=models.ImageField(default='fotos_perfil/default.jpg', upload_to='profile_pics/', verbose_name='Foto de perfil'),
        ),
    ]
