from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b4b-ryh%ecbu9)^fgn#9%#f-o1=fgri6k8ov5%98czqno@=%%l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'volodimirsavin56@gmail.com'
EMAIL_HOST_PASSWORD = 'dcphxqmxdtscgsyf'


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '1073164246431-cdfuilo7a49k52qt9rm1r4skgb5t5j6g.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'j2Wy_oKp4CPNLRy3tPtoSpO2'
