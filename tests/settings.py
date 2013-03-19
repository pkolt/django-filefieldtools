import os


BASE_DIR = os.path.dirname(__file__)
MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, '../../~temp/media'))
DEBUG = TEMPLATE_DEBUG = True
SECRET_KEY = 'my-secret-key'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

INSTALLED_APPS = (
    'filefieldtools',
    'tests.app',
)
