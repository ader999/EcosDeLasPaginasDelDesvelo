# Generated by Django 4.2.3 on 2023-11-14 01:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='Nombre de usuario')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=200, verbose_name='Apellidos')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Correo electrónico')),
                ('usuario_activo', models.BooleanField(default=True)),
                ('usuario_administrador', models.BooleanField(default=False)),
                ('codigo_confirmacion', models.CharField(blank=True, max_length=10)),
                ('correo_confirmado', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog_images/')),
                ('pdf_file', models.FileField(blank=True, null=True, upload_to='blog_pdfs/')),
                ('video', models.URLField(blank=True, null=True)),
                ('fecha_de_publicacion', models.DateTimeField(auto_now_add=True)),
                ('categoria', models.CharField(choices=[('Educacion', 'Educación, Humanidades y Artes'), ('Ciencia_Sociales', 'Ciencias Sociales, Económicas, Administrativas y Derecho'), ('Ciencias_de_la_vida', 'Ciencias de la Vida'), ('Fisica', 'Física'), ('Matematicas_Y_Estadisticas', 'Matemáticas y Estadísticas'), ('Ingenieria', 'Ingeniería, Industria, Arquitectura e Informática'), ('Ciencias_Agropecuarias_Ambientales', 'Ciencias Agropecuarias y Ambientales'), ('Salud_Servicios_sociales_Bienestar', 'Salud, Servicios Sociales y Bienestar')], max_length=255)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
