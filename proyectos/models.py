from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='productos/')
    header_image   = models.ImageField(                              # NUEVO campo
                    upload_to='productos/headers/',
                    blank=True,
                    null=True,
                    help_text="Foto exclusiva para el header de detalle")
    categoria = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nombre
    
class ImagenProducto(models.Model):
    producto = models.ForeignKey(Producto, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos/')


class Mensaje(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField(max_length=100, blank=True)
    telefono = models.CharField(max_length=100)
    correo = models.EmailField(blank=True)
    mensaje = models.TextField()   
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Mensaje de {self.nombre}"
    
    
class ImagenCarrusel(models.Model):
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='fotos_proyectos/')  # Quedará en media/fotos_proyectos/
    orden = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.titulo

class Destacados(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='fotos_destacado/')

