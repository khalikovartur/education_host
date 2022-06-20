from .base import *

DEBUG = False

ADMINS = (
    ('Artur K', 'khalikovartur7@gmail.com'),
)

ALLOWED_HOSTS = ['.educaproject.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'arturdb',
        'USER': 'artur',
        'PASSWORD': 'artur12345',
    }
}

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True