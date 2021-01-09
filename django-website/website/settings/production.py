from .base import *

DEBUG = False

SECRET_KEY =  env.str('SECRET_KEY')

WAGTAIL_ADMIN_URL = env.str('WAGTAIL_ADMIN_URL')
DJANGO_ADMIN_URL = env.str('DJANO_ADMIN_URL')

try:
    from .local import *
except ImportError:
    pass
