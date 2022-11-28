# Standard Library
from os import environ
from decouple import config
from .base import *  # noqa

DEBUG = True
#ROOT_URLCONF = f'{SITE_NAME}.{SITE_NAME}.urls'


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


INSTALLED_APPS = BASE_APPS + LOCAL_APPS + THIRD_APPS  # noqa
