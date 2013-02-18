import os

MYSITE_ROOT = os.path.dirname(__file__)

MEDIA_ROOT = os.path.join(MYSITE_ROOT, '~media')

DEBUG = True

SECRET_KEY = 'my-secret-key'

TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

INSTALLED_APPS = (
    'tests.app',
)
