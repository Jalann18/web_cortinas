from django.urls import path
from . import views  # Importamos las vistas de esta app

urlpatterns = [
    path('', views.home, name='home'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
]
