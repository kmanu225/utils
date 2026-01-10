from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY
SECRET_KEY = 'django-insecure-#4+dnsy(w+6sc2-k=4peb&#6a$k+#g+w*4ndpd9^e*6&e+#q-k'
DEBUG = True
ALLOWED_HOSTS = []

# Installed apps (only what we need)
INSTALLED_APPS = [
    'django.contrib.staticfiles',  # needed for serving static files
    'core',                        # your PDF merger app
]

# Middleware (minimal for dev)
MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'config.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# No database needed
DATABASES = {}

# Static files
STATIC_URL = '/static/'

# Timezone & localization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Default auto field (not critical since no models)
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
