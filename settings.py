# Django settings for sb project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('yury', 'yury@yury.name'),
)

MANAGERS = ADMINS

TIME_ZONE = 'America/Los_Angeles'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = False

#MEDIA_ROOT = '/home/sb/img/'
#MEDIA_URL = ''

ADMIN_MEDIA_PREFIX = '/admin-media/'

SECRET_KEY = 'i9s_van!p0*2kv2@kax(wg^uz!ixxx_mkg#!96-6egq4y$v%uw'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    '/home/sb/templates/'
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
)

try:
    from settings_local import *
except ImportError:
    import sys
    sys.stderr.write('Unable to read settings_local.py\n')
    sys.exit(1)

try:
    INSTALLED_APPS += ADDITIONAL_APPS
except NameError:
    pass