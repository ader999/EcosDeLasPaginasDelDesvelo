

from pathlib import Path
import os
import dj_database_url


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', default='your secret key')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'RENDER' not in os.environ

ALLOWED_HOSTS = ['ecos-de-las-paginas-del-desvelo.onrender.com']

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)




# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'repositorio',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'repositorio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['plantillas'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'repositorio.wsgi.application'


#------------------------------ Database________________________________________
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

credentials = {}
# Obtener la ruta completa al archivo config.txt
config_file_path = os.path.join(os.path.dirname(__file__), 'config.txt')

# Verificar si el archivo de texto existe
print(f"Ruta del archivo config.txt: {config_file_path}")
if os.path.isfile(config_file_path):
    # Leer las credenciales desde el archivo de texto
    with open(config_file_path) as f:
        for line in f:
            # Dividir cada línea en clave y valor
            key, value = map(str.strip, line.strip().split('='))

            # Almacenar las credenciales en el diccionario
            credentials[key] = value

    # Imprimir información adicional
    print(f"Credenciales leídas: {credentials}")

    # Construir el diccionario DATABASES utilizando las credenciales
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'repositorio_1',
            'USER': credentials.get('RDS_USER'),
            'PASSWORD': credentials.get('RDS_PWS'),
            'HOST': credentials.get('RDS_HOST'),
            'PORT': '5432',  # El puerto por defecto para PostgreSQL
        }
    }

elif 'RDS_USER' in os.environ:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'repositorio_1',
            'USER': os.environ.get('RDS_USER'),
            'PASSWORD': os.environ.get('RDS_PWS'),
            'HOST': os.environ.get('RDS_HOST'),
            'PORT': '5432',  # El puerto por defecto para PostgreSQL
        }
    }



#------------------------------ END Database________________________________________

"""
if 'USE_POSTGRESQL' in os.environ:
    DATABASES = {
        'default': dj_database_url.config(
            default='postgresql://postgres:postgres@localhost/postgres',
            conn_max_age=600
        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }"""


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]




# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

"""MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'media')
MEDIA_URL = '/static/media/'"""
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/



# Configuración para usar Amazon S3 como backend de almacenamiento
AWS_ACCESS_KEY_ID = 'AKIAWTKJKQQEH7EBSDES'
AWS_SECRET_ACCESS_KEY = '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'

"""AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')"""
AWS_STORAGE_BUCKET_NAME = 'codeader'
AWS_S3_REGION_NAME = 'us-east-1'  # Por ejemplo, 'us-east-1'

# Configuración para servir archivos estáticos y de medios desde Amazon S3
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# Configuración para almacenar archivos de medios en Amazon S3
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'





STATIC_URL = 'static/'

if not DEBUG:
    # Tell Django to copy statics to the `staticfiles` directory
    # in your application directory on Render.
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    # Turn on WhiteNoise storage backend that takes care of compressing static files
    # and creating unique names for each version so they can safely be cached forever.
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'




LOGIN_URL = 'iniciar_sesion'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# Configuarar correo
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST')  # Configura el host SMTP adecuado
EMAIL_PORT = 587  # Puerto para SMTP (587 para TLS, 465 para SSL)
EMAIL_USE_TLS = True  # Habilitar TLS (o SSL si estás usando el puerto 465)
EMAIL_HOST_USER =  os.environ.get('EMAIL_USER')  # Tu dirección de correo desde la que enviarás los mensajes
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PWS')  # Contraseña de tu correo electrónico


AUTH_USER_MODEL = 'repositorio.CustomUser'