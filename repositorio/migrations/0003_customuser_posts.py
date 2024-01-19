# Generated by Django 4.2.3 on 2023-11-14 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repositorio', '0002_customuser_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='posts',
            field=models.ManyToManyField(blank=True, related_name='posts', to='repositorio.post'),
        ),
    ]
