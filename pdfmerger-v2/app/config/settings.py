from pathlib import Path
import os
from django.core.management.utils import get_random_secret_key

# -----------------------
# Paths
# -----------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------
# SECURITY
# -----------------------
# Secret key from environment or fallback to random key
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', get_random_secret_key())

DEBUG = False

# Replace with your domain(s) or server IPs
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', "*").split(',')

# -----------------------
# Installed apps
# -----------------------
INSTALLED_APPS = [
    'django.contrib.staticfiles',  # required for serving static files
    'core',                        # your PDF merger app
]

# -----------------------
# Middleware
# -----------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # <-- WhiteNoise for static files
    'django.middleware.common.CommonMiddleware',
]

# -----------------------
# URLs & WSGI
# -----------------------
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'

# -----------------------
# Templates
# -----------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'core/templates'],  # folder for your HTML templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
            ],
        },
    },
]

# -----------------------
# DATABASE
# -----------------------
# No database needed
DATABASES = {}

# -----------------------
# Static files (for production)
# -----------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # where collectstatic will put files

# -----------------------
# Security headers for production
# -----------------------
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'

# -----------------------
# Timezone & localization
# -----------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# -----------------------
# Default auto field (irrelevant since no models)
# -----------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
