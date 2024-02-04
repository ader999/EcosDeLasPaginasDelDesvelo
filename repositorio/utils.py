from django.core.mail import send_mail
import random
import string


def enviar_codigo_confirmacion(correo_usuario):
    codigo = ''.join(random.choices(string.ascii_letters + string.digits, k=6))  # Generar un código aleatorio
    mensaje = f"Tu código de confirmación es: {codigo}"
    send_mail('Código de confirmación', mensaje, 'tu_correo@ejemplo.com', [correo_usuario])
    return codigo  # Devolver el código para su posterior validación


