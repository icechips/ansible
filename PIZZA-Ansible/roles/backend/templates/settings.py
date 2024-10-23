"""
Django settings for eBackendProject project.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from __future__ import absolute_import
import os
import socket
from six import unichr
import ipaddress

REMOTE_DEBUG = os.environ.get('REMOTE_DEBUG', False)

# Django Properties
ALLOWED_HOSTS = ['*']
DEBUG = False
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = ["https://{{ pizza_site_domain }}"]
DEBUG={{ gunicorn_debug }}
PROTOCOL_PREFIX = 'https://'
HOSTNAME = '{{ pizza_site_domain }}'
FRONTEND_ADDRESS = PROTOCOL_PREFIX + HOSTNAME + '/#/'
BACKEND_ADDRESS = PROTOCOL_PREFIX + HOSTNAME
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '{{ django_secret_key }}'

# Database Properties
DATABASE_HOST = '{{ ebackend_db_host }}'
DATABASE_NAME = '{{ ebackend_db_name }}'
DATABASE_USER = '{{ ebackend_db_user }}'
DATABASE_PASSWORD = '{{ ebackend_db_password }}'
DATABASE_PORT = '3306'
DB_CONN_MAX_AGE = 60

# Application definition
INSTALLED_APPS = (
    'django.contrib.humanize',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'ebackendapp',
    'django.contrib.admin',
    'eav',
    'requests',
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
)

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'ebackendproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ebackendproject.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DATABASE_NAME,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': DATABASE_HOST,
        'PORT': DATABASE_PORT,
        'CONN_MAX_AGE': DB_CONN_MAX_AGE,
        'OPTIONS': {
            'charset': 'utf8mb4'
        }
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Toronto'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = 'static'

SITE_ID = 1

STATICFILES_DIRS = [
    'bower_components/',
    'code_images/',
    'ebackendapp/static/',
]

CODE_IMAGES_DIR = 'code_images'

#
# EMAIL SETTINGS
#
EMAIL_HOST = '{{ mail_relayhost }}'
EMAIL_PORT = 25
EMAIL_FROM_NAME = 'Pizza Shop'
EMAIL_FROM = 'pizza.shop@pizza.ca'
DEFAULT_FROM_EMAIL = 'pizza.shop@pizza.ca'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_MODEL_SERIALIZER_CLASS': 'drf_toolbox.serializers.ModelSerializer',
    'PAGINATE_BY': None,
}

REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'ebackendapp.rest.models.UserDetailsSerializer',
}

if REMOTE_DEBUG:
    LOGGING_FILE = 'ebackendapp.remote.log'
else:
    LOGGING_FILE = 'ebackendapp.log'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR + '/logs/' + LOGGING_FILE,
            'formatter': 'verbose'
        },
        'security_file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR + '/logs/ebackendapp_security.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'propagate': True,
            'level': 'INFO',
        },
        'ebackendapp': {
            'handlers': ['file'],
            'level': 'INFO',
        },
        'security': {
            'handlers': ['security_file'],
            'level': 'INFO',
        },
    }
}

REDEMPTION_CODE_CHAR_COUNT = 20
REDEMPTION_CODE_DISPLAY_DIVISOR = 4
REDEMPTION_CODE_DISPLAY_DELIMITER = "-"
REDEMPTION_CODE_STRIP_CHARS = ['-', ' ', '=', '_', '+', '.', '[', ']', '<', '>', '/', unichr(0o020)]
QR_JS_SCAN_PREFIX = '<scqr'
QR_JS_SCAN_SUFFIX = '>'

TRANSACTION_PAGING_MAX_COUNT = 500