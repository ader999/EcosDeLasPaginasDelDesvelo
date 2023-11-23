from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Permission


# ... (otras importaciones)

class UsuarioManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('El campo de correo electrónico debe establecerse')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superusuario debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superusuario debe tener is_superuser=True.')

        return self.create_user(email, username, password, **extra_fields)

class CustomUser(AbstractUser):
    username = models.CharField("Nombre de usuario", unique=True, max_length=100)
    nombre = models.CharField("Nombres", max_length=200, null=False)
    apellidos = models.CharField("Apellidos", max_length=200, null=False)
    email = models.EmailField("Correo electrónico", max_length=254, unique=True)
    foto_perfil = models.ImageField("Foto de perfil", upload_to='fotos_perfil/', blank=True, null=True)
    usuario_activo = models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=False)
    posts = models.ManyToManyField('Post', related_name='posts', blank=True)
    codigo_confirmacion = models.CharField(max_length=10, blank=True)
    correo_confirmado = models.BooleanField(default=False)


    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nombre', 'apellidos', 'email']

    def __str__(self):
        return f"{self.nombre}, {self.apellidos}"

    def save(self, *args, **kwargs):
        if not self.foto_perfil:
            self.foto_perfil.name = 'fotos_perfil/usuario.png'
        super().save(*args, **kwargs)




class Post(models.Model):
    lista_areasConocimiento = (
        ('Educacion', 'Educación, Humanidades y Artes'),
        ('Ciencia_Sociales', 'Ciencias Sociales, Económicas, Administrativas y Derecho'),
        ('Ciencias_de_la_vida', 'Ciencias de la Vida'),
        ('Fisica', 'Física'),
        ('Matematicas_Y_Estadisticas', 'Matemáticas y Estadísticas'),
        ('Ingenieria', 'Ingeniería, Industria, Arquitectura e Informática'),
        ('Ciencias_Agropecuarias_Ambientales', 'Ciencias Agropecuarias y Ambientales'),
        ('Salud_Servicios_sociales_Bienestar', 'Salud, Servicios Sociales y Bienestar'),
    )

    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=False, null=False)
    pdf_file = models.FileField(upload_to='blog_pdfs/', blank=True, null=True)
    video = models.URLField(blank=True, null=True)
    fecha_de_publicacion = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE,editable=False)
    categoria = models.CharField(max_length=255,choices=lista_areasConocimiento)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Asignar el usuario que ha iniciado sesión como autor solo si no se ha asignado previamente
        if not self.author_id:
            self.author = get_user_model().objects.get(pk=kwargs.get('user').pk)
        super().save(*args, **kwargs)





"""class Usr(models.Model):


    PROFESIONES = [
        ('medico', 'Médico/a'),
        ('ingeniero', 'Ingeniero/a'),
        ('docente', 'Docente/Profesor/a'),
        ('abogado', 'Abogado/a'),
        ('contador', 'Contador/a'),
        ('arquitecto', 'Arquitecto/a'),
        ('diseñador', 'Diseñador/a'),
        ('programador', 'Programador/a'),
        ('periodista', 'Periodista/Comunicador/a'),
        ('psicologo', 'Psicólogo/a'),
        ('investigador', 'Investigador/a'),  # Opción genérica para investigadores
        ('sin_especificar', 'Sin Especificar'),  # Opción genérica para no especificado
        ('estudiante', 'Estudiante'),
        # Agrega más opciones según sea necesario
    ]

    UNIVERSIDADES = [
        ('UCA', 'Universidad Centroamericana (UCA)'),
        ('UNAN-Managua', 'Universidad Nacional Autónoma de Nicaragua-Managua'),
        ('INCAE', 'INCAE Business School, Nicaragua'),
        ('UNI', 'Universidad Nacional de Ingenieria'),
        ('UNAN-Leon', 'Universidad Nacional Autónoma de Nicaragua, León'),
        ('UNA', 'Universidad Nacional Agraria'),
        ('UAM', 'Universidad Americana, Nicaragua'),
        ('UCRM', 'Universidad Catolica Redemptoris Mater'),
        ('URACCAN', 'Universidad de las Regiones Autónomas de la Costa Caribe Nicaragüense'),
        ('UCC', 'Universidad de Ciencias Comerciales'),
        ('LUTERO', 'Universidad Martín Lutero'),
        ('extranjero', 'Estudié en el extranjero'),
        ('otra', 'Otra universidad'),
        ('sin_especificar', 'Sin Especificar'),
        ('no_universidad', 'No estudié en una universidad'),
    ]

    nombre = models.CharField(max_length=100, null=False)
    apellido = models.CharField(max_length=100, null=False)
    usr = models.CharField(max_length=20, null=False)
    correo = models.EmailField(max_length=100, null=False,unique=True)
    contraseña = models.CharField(max_length=50, null=False)
    universidad = universidad = models.CharField(max_length=100, choices=UNIVERSIDADES, default='sin_especificar')
    profecion = models.CharField(max_length=100, choices=PROFESIONES, default='sin_especificar')
"""


