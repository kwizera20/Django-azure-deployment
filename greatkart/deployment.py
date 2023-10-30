import os
from .settings import *
from .settings import BASE_DIR

SECRET_KEY = os.environ.get('SECRET', 'default_secret_key')
ALLOWED_HOSTS = [os.environ.get('WEBSITE_HOSTNAME', 'example.com')]
CSRF_TRUSTED_ORIGINS = ['https://' + os.environ.get('WEBSITE_HOSTNAME', 'example.com')]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_session_timeout.middleware.SessionTimeoutMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

connection_string = os.environ.get('AZURE_POSTGRESQL_CONNECTIONSTRING', '')
parameters = {pair.split('=')[0]: pair.split('=')[1] for pair in connection_string.split()}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': parameters.get('dbname', 'default_dbname'),
        'USER': parameters.get('user', 'default_user'),
        'PASSWORD': parameters.get('password', 'default_password'),
        'HOST': parameters.get('host', 'localhost'),
    }
}
