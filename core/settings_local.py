# =============================================
# settings_local.py — Solo para desarrollo local
# Usa SQLite en vez de MySQL de PythonAnywhere
# =============================================
from .settings import *   # hereda todo de settings.py

# Sobreescribe la base de datos con SQLite
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Desactiva redirección HTTPS en local
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# Debug siempre ON en local
DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
