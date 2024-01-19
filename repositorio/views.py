from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, Page
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout, get_user_model
#from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseForbidden
from functools import wraps

from django.contrib.auth.decorators import user_passes_test

from django.utils.safestring import mark_safe

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
import markdown
from django.contrib.auth import update_session_auth_hash

from .forms import PostForm, RegistroForm, CambiarContraseñaForm
from .models import Post, CustomUser
from .utils import enviar_codigo_confirmacion

User = get_user_model()

def validar_correo_confirmado(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            custom_user = CustomUser.objects.get(username=request.user.username)
            if not custom_user.correo_confirmado:
                return redirect('validar_codigo')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def pasar_usuario(request):
    usuario = request.user.username
    return usuario

def inicio(request):
    # Obtener todos los objetos Post ordenados por fecha de publicación en orden descendente
    posts = Post.objects.all().order_by('-fecha_de_publicacion')

    # Configurar la paginación
    paginator = Paginator(posts, 5)  # Divide las publicaciones en páginas de 10 elementos por página

    page_number = request.GET.get('page')  # Obtiene el número de página de la URL
    page = paginator.get_page(page_number)  # Obtiene la página actual

    # Definir el contexto con los posts paginados
    context = {
        'page': page,
        'usr': pasar_usuario(request),
        'mostrar_fondo_oscuro': request.COOKIES.get('mostrar_fondo_oscuro', 'false') == 'true'
    }

    # Renderizar la plantilla y pasar el contexto
    return render(request, 'inicio.html', context)



@login_required
@validar_correo_confirmado
def detalle_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'detalle_post.html', {'post': post,'usr':pasar_usuario(request)})

def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data['nombre']
            user.last_name = form.cleaned_data['apellidos']
            user.save()

            # Autenticar al usuario después de registrar
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=raw_password)
            login(request, user)

            # Generar y enviar el código de confirmación por correo electrónico
            codigo = enviar_codigo_confirmacion(user.email)  # Genera un código de confirmación

            # Asignar el código de confirmación al usuario recién creado
            user.codigo_confirmacion = codigo
            user.save()

            # Obtener el content type del modelo Post
            content_type = ContentType.objects.get_for_model(Post)

            # Crear el permiso 'add_post' si no existe
            if not Permission.objects.filter(content_type=content_type, codename='add_post').exists():
                add_post_permission = Permission.objects.create(
                    codename='add_post',
                    name='Can add post',
                    content_type=content_type,
                )

            # Asignar el permiso 'add_post' al usuario recién creado (CustomUser)
            add_post_perm = Permission.objects.get(codename='add_post')
            user.user_permissions.add(add_post_perm)

            # Redirigir a la página de validación de código
            return redirect('validar_codigo')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})




def iniciar_sesion(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        contraseña = request.POST.get('contraseña')

        # Autenticar al usuario con las credenciales proporcionadas
        user = authenticate(request, username=usuario, password=contraseña)

        if user is not None:
            login(request, user)
            messages.success(request, '¡Inicio de sesión exitoso!')
            return redirect('inicio')  # Redirigir a la página de inicio si las credenciales son válidas
        else:
            messages.error(request, 'Credenciales inválidas. Inténtalo de nuevo.')

    return render(request, 'login.html')

def cerrar_sesion(request):
    logout(request)
    # Redirigir a la página de inicio u otra página luego de cerrar sesión
    return redirect('inicio')

@login_required
@validar_correo_confirmado
def crear_post(request):
    print(f'Usuario actual: {request.user}')
    print(f'Tiene permiso: {request.user.has_perm("app_label.add_post")}')

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('done')  # Redirigir a la página deseada
    else:
        form = PostForm()

    return render(request, 'trepar_post.html', {'form': form,'usr':pasar_usuario(request)})




def done(request):
    return render(request, 'done.html',{'usr':pasar_usuario(request)})


@login_required
def validar_codigo(request):
    if request.method == 'POST':
        codigo_ingresado = request.POST.get('codigo')
        usuario = request.user

        # Obtener el modelo User actualmente autenticado
        try:
            usuario_personalizado = CustomUser.objects.get(username=usuario.username)
        except CustomUser.DoesNotExist:
            usuario_personalizado = None

        if usuario_personalizado:
            if codigo_ingresado == usuario_personalizado.codigo_confirmacion:
                usuario_personalizado.correo_confirmado = True
                usuario_personalizado.save()
                messages.success(request, 'Correo confirmado correctamente.')
                return redirect('inicio')
            else:
                messages.error(request, 'Código incorrecto. Inténtalo de nuevo.')
        else:
            messages.error(request, 'No se encontró un usuario personalizado asociado.')

    return render(request, 'validar_codigo.html')

def buscar_post(request):
    query = request.GET.get('query')
    if query:
        # Realizar la búsqueda en la base de datos
        search_results = Post.objects.filter(title__startswith=query)

        return render(request, 'resultado_busqueda.html', {'search_results': search_results, 'query': query})
    else:
        return render(request, 'resultado_busqueda.html', {'search_results': None, 'query': query})

def perfil(request, username):
    author = get_object_or_404(CustomUser, username=username)
    posts = Post.objects.filter(author=author)
    nombre_completo = f"{author.nombre} {author.apellidos}"
    return render(request, 'perfil.html', {'author': author, 'posts': posts, 'nombre_completo': nombre_completo,'usr':pasar_usuario(request)})

def configuraciones(request):
    if request.method == 'POST':
        # Procesar la actualización de la foto de perfil directamente en la vista
        new_photo = request.FILES.get('foto_perfil')
        if new_photo:
            request.user.foto_perfil = new_photo
            request.user.save()
            messages.success(request, 'La foto de perfil se ha cambiado con éxito.')
            return redirect('perfil', username=request.user.username)

        # Procesar el cambio de contraseña
        cambiar_contraseña_form = CambiarContraseñaForm(request.user, request.POST)
        if cambiar_contraseña_form.is_valid():
            user = cambiar_contraseña_form.save()
            update_session_auth_hash(request, user)  # Actualizar la sesión para evitar desconexiones
            messages.success(request, 'La contraseña se ha cambiado con éxito.')

            logout(request)
            return redirect('iniciar_sesion')

    else:
        cambiar_contraseña_form = CambiarContraseñaForm(request.user)

    return render(request, 'configuraciones.html', {'usr': pasar_usuario(request), 'cambiar_contraseña_form': cambiar_contraseña_form})


def cambiar_fondo(request):
    modo_actual = request.COOKIES.get('modo_fondo', 'modo_claro')

    # Cambia el modo: si estaba en modo oscuro, cambia a modo claro, y viceversa
    nuevo_modo = 'modo_claro' if modo_actual == 'modo_oscuro' else 'modo_oscuro'

    response = redirect('inicio')
    response.set_cookie('modo_fondo', nuevo_modo, expires=None)

    return response