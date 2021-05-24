# Перенос секретных данных в файл, который не выкладивать в открытый доступ

from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'b4b-ryh%ecbu9)^fgn#9%#f-o1=jsdvy8948v5%98czqno@=%%l'
SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY', 'b4b-ryh%ecbu9)^fgn#9%#f-o1=jsdvy8948v5%98czqno@=%%l')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = bool(os.environ.get('DJANGO_DEBUG', True))

ALLOWED_HOSTS = ['127.0.0.1']


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'volodimirsavin56@gmail.com'


EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD_ENV', 'yrtyeye')

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ.get(
    'SOCIAL_AUTH_GOOGLE_OAUTH2_KEY_ENV', 'yrtyeye')

SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ.get(
    'SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET_ENV', 'yrtyeye')

RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY_ENV', 'yrtyeye')

RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY_ENV', 'yrtyeye')
