from django.contrib import admin
from .models import Mensaje, Producto, ImagenProducto, ImagenCarrusel, Destacados

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display  = ('nombre', 'categoria')
    search_fields = ('nombre', 'categoria')
    # Para que puedas subir la imagen principal y la exclusiva del header:
    fields = (
        'nombre',
        'categoria',
        'imagen',        # imagen “estándar” o miniatura
        'header_image',  # nueva imagen exclusiva para el header
        'descripcion',
    )

@admin.register(ImagenProducto)
class ImagenProductoAdmin(admin.ModelAdmin):
    list_display = ('producto', 'imagen')

@admin.register(Mensaje)
class MensajeAdmin(admin.ModelAdmin):
    list_display  = ('nombre', 'telefono', 'correo', 'fecha')
    search_fields = ('nombre', 'correo')

@admin.register(ImagenCarrusel)
class ImagenCarruselAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'orden')
    ordering     = ['orden']

@admin.register(Destacados)
class DestacadosAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
