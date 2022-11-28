# Standard Library
from decouple import config
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", cast=bool)

ALLOWED_HOSTS = ['18.213.118.152']

DATABASES = {
    "default":
        {
            "ENGINE": 'django.db.backends.mysql',
            "NAME": config("DB_NAME"),
            "USER": config("DB_USER"),
            "PASSWORD": config("DB_PASSWORD"),
            "HOST": config("DB_HOST"),
            "PORT": 3306
        }
}

ROOT_URLCONF = f'{SITE_NAME}.urls'

INSTALLED_APPS = BASE_APPS + LOCAL_APPS + THIRD_APPS
