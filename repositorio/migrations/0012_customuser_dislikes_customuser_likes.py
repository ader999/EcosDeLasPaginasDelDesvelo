# Generated by Django 4.2.3 on 2024-04-23 20:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("repositorio", "0011_alter_post_categoria"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="dislikes",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="customuser",
            name="likes",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
