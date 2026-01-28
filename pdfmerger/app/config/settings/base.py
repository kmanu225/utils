from pathlib import Path

# -----------------------
# Paths
# -----------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------
# SECURITY
# -----------------------
SECRET_KEY = 'django-insecure-#4+dnsy(w+6sc2-k=4peb&#6a$k+#g+w*4ndpd9^e*6&e+#q-k'


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
    'whitenoise.middleware.WhiteNoiseMiddleware',
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
STATIC_ROOT = BASE_DIR / 'staticfiles'

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
