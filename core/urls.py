# core/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pathlib import Path

from proyectos.views import robots_txt, sitemap_xml

urlpatterns = [
    path('admin/', admin.site.urls),
    path('robots.txt', robots_txt, name='robots_txt'),
    path('sitemap.xml', sitemap_xml, name='sitemap_xml'),
    path('', include('proyectos.urls')),
]

# Sirve MEDIA en DEBUG
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Sirve STATIC en DEBUG
if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=Path(__file__).resolve().parent.parent / 'proyectos' / 'static'
    )
