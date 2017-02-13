from base import *
import dj_database_url

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', '<your STRIPE_PUBLISHABLE key>')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', '<your STRIPE_SECRET key>')

DATABASES['default'] = dj_database_url.config("mysql://bc5cb537891e4a:0e9e66b7@eu-cdbr-west-01.cleardb.com/heroku_27041bcc28780b7?reconnect=true")