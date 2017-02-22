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

INTERNAL_IPS = ('127.0.0.1')

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_VD1FVRfbUP6JqJVoHfkcKCZ4')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_n8TB3tJYW7cNBjkopYL3aKm1')

