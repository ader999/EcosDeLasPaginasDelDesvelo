# Generated by Django 4.2.3 on 2024-04-23 21:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("repositorio", "0012_customuser_dislikes_customuser_likes"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="dislikes",
        ),
        migrations.RemoveField(
            model_name="customuser",
            name="likes",
        ),
        migrations.AddField(
            model_name="post",
            name="dislikes",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="post",
            name="likes",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
