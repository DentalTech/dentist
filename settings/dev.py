from base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INSTALLED_APPS.append('debug_toolbar')

# Do I need to add this to middleware classes? See https://django-debug-toolbar.readthedocs.io/en/0.11.0/installation.htmlpp
MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

