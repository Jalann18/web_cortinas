from django.shortcuts import render
from .models import Producto, ImagenCarrusel, Destacados
from .forms import MensajeForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

def home(request):
    form = MensajeForm()

    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mensaje enviado correctamente.')
            return redirect('home')  # Redirige después de enviar el formulario (buena práctica)

    # 🔥 Aquí ordenamos correctamente las imágenes del carrusel
    imagenes = ImagenCarrusel.objects.all().order_by('orden')
    productos = Producto.objects.all()
    destacados = Destacados.objects.all()

    return render(request, 'proyectos/home.html', {
        'form': form,
        'imagenes': imagenes,
        'productos': productos,
        'destacados': destacados,
    })

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    imagenes = producto.imagenes.all()  # gracias al related_name='imagenes'
    return render(request, 'proyectos/detalle_producto.html', {
        'producto': producto,
        'imagenes': imagenes
    })
