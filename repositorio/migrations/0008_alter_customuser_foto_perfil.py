# Generated by Django 4.2.3 on 2023-11-18 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repositorio', '0007_alter_customuser_foto_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='foto_perfil',
            field=models.ImageField(blank=True, null=True, upload_to='fotos_perfil/', verbose_name='Foto de perfil'),
        ),
    ]
