from .general import *

DEBUG = True
SECRET_KEY = 'django-insecure-q6tqvp=a(2_ta&hkam38ttkfz1ogo)v1l$9nuof6bah0d%t76t'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lms_db',
        'USER': 'root',
        'PASSWORD': 'semicolon',
        'HOST': 'localhost'
    }
}
