# Generated by Django 4.2.3 on 2023-12-21 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repositorio', '0010_alter_post_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categoria',
            field=models.CharField(choices=[('Educacion', 'Educación, Humanidades y Artes'), ('Ciencia_Sociales', 'Ciencias Sociales, Económicas, Administrativas y Derecho'), ('Ciencias_de_la_vida', 'Ciencias de la Vida'), ('Fisica', 'Física'), ('Matematicas_Y_Estadisticas', 'Matemáticas y Estadísticas'), ('Ingenieria', 'Ingeniería, Industria, Arquitectura e Informática'), ('Ciencias_Agropecuarias_Ambientales', 'Ciencias Agropecuarias y Ambientales'), ('Salud_Servicios_sociales_Bienestar', 'Salud, Servicios Sociales y Bienestar')], max_length=255),
        ),
    ]
