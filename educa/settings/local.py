from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sglite3',
        'NAME': os.path.join(BASE_DIR, 'db.sglite3'),
    }
}