from base import *
import dj_database_url


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

CLEAR_DB_URL = os.environ.get("CLEARDB_DATABASE_URL", "")

DATABASES['default'] = dj_database_url.parse(CLEAR_DB_URL)

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_VD1FVRfbUP6JqJVoHfkcKCZ4')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_n8TB3tJYW7cNBjkopYL3aKm1')


