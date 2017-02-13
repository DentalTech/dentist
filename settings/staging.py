from base import *
import dj_database_url

DEBUG = True

DATABASES['default'] = dj_database_url.config("<CLEARDB_DATABASE_URL>")


# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', '<your STRIPE_PUBLISHABLE key>')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', '<your STRIPE_SECRET key>')

