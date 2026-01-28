from .base import *
import os
from django.core.management.utils import get_random_secret_key


# -----------------------
# SECURITY
# -----------------------
# Secret key from environment or fallback to random key
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', get_random_secret_key())

DEBUG = False

# Replace with your domain(s) or server IPs
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', "*").split(',')

# -----------------------
# Security headers for production
# -----------------------
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'