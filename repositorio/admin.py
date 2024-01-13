from django.contrib import admin
from .models import  Post, CustomUser

admin.site.site_header = 'Investigacion que transforma'
admin.site.index_title = 'Bienbenidos al Panel de control del sitio'
admin.site.site_title = 'ADMIN'



admin.site.register(Post)
admin.site.register(CustomUser)
