# Standard Library
from genericpath import exists
import sys
from os import environ
from os.path import abspath, basename, dirname, join, normpath
from pathlib import Path
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent

DJANGO_ROOT = dirname(dirname(abspath(__file__)))

PROJECT_ROOT = dirname(DJANGO_ROOT)

SECRET_KEY = environ.get(
    'SECRET_KEY',
    'django-insecure-w3_n89^)(18q=kxl-f-o@7vme@7x&3$64hxcdn2w$3c2fcgzpl'
)

SITE_NAME = basename(DJANGO_ROOT)

STATIC_ROOT = join(PROJECT_ROOT, 'run', 'static')

MEDIA_ROOT = join(PROJECT_ROOT, 'run', 'images')

PROJECT_TEMPLATES = [
    join(PROJECT_ROOT, 'templates'),
]

PROJECT_TEMPLATES = [
    join(PROJECT_ROOT, 'templates'),
]

sys.path.append(normpath(join(PROJECT_ROOT, 'apps')))


BASE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
]

LOCAL_APPS = [
    'integration.orders',
    'integration.customer',
]

THIRD_APPS = [
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
]

INSTALLED_APPS = BASE_APPS + LOCAL_APPS + THIRD_APPS


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': PROJECT_TEMPLATES,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages'
            ],
        },
    },
]


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'NumericPasswordValidator',
    },
]


WSGI_APPLICATION = f'{SITE_NAME}.wsgi.application'

ROOT_URLCONF = f'{SITE_NAME}.urls'

STATIC_URL = '/static/'

MEDIA_URL = '/images/'

DEBUG = False

LANGUAGE_CODE = 'en-US'

TIME_ZONE = environ.get(
    'TIME_ZONE',
    'America/Bogota'
)

USE_I18N = True

USE_L10N = True

USE_TZ = True

# AUTH_USER_MODEL = ''

"""
CORS_ORIGIN_WHITELIST = [
    "http://localhost:8000",
    "http://localhost:3000",
    "http://18.213.118.152:8000"
]
"""

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True
}

LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s :: %(asctime)s :: '
                      '%(name)s :: %(process)d %(thread)d :: %(message)s'
        }
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        # INTEGRATION
        'mo_integration.chat': {
            'handlers': ['file'],
            'propagate': True,
            'level': "INFO"
        },
        # LIBRARIES
        'django': {
            'handlers': ['file'],
            'level': "INFO"
        }
    }
}
