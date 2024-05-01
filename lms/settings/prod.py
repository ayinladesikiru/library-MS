import os
from .general import *


DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['beedex.pythonanywhere.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'beedex$default',
        'USER': 'beedex',
        'PASSWORD': 'library-MS-DB',
        'HOST': 'beedex.mysql.pythonanywhere-services.co',
    }
}
