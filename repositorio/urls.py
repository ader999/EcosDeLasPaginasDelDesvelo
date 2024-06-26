"""
URL configuration for repositorio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from repositorio import views
from django.conf import settings

from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('post/<int:post_id>/', views.detalle_post, name='detalle_post'),
    path('registro/', views.registro_usuario, name='registro_usuario'),
    path('login/', views.iniciar_sesion, name='iniciar_sesion'),
    path('cerrar-sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('trepar_post/', views.crear_post, name='trepar_post'),
    path('done/', views.done, name='done'),
    path('validar_codigo/', views.validar_codigo, name='validar_codigo'),
    path('resultado_busqueda/', views.buscar_post, name='resultado_busqueda'),
    path('perfil/<str:username>/', views.perfil, name='perfil'),
    path('configuraciones/', views.configuraciones, name='configuraciones'),
    path('cambair_fondo/', views.cambiar_fondo, name='cambiar_fondo'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)