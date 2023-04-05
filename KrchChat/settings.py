"""
Django settings for KrchChat project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
import sys
import os.path
from pathlib import Path
import environ
import ast
import subprocess


def get_environ_vars():  # This is because the environment variables are set in this path in elasticbeanstalk
    # This method returns a dictionary of key value pairs
    completed_process = subprocess.run(
        ['/opt/elasticbeanstalk/bin/get-config', 'environment'],
        stdout=subprocess.PIPE,
        text=True,
        check=True
    )
    
    return ast.literal_eval(completed_process.stdout)




# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

# Initialise environment variables
envs = environ.Env()
envs.read_env()
env = {}
if envs("SECRET_KEY"):
    env = {
        "SECRET_KEY": envs("SECRET_KEY"),
        'DATABASE_NAME': envs('DATABASE_NAME'),
        'DATABASE_USER': envs('DATABASE_USER'),
        'DATABASE_PASS': envs('DATABASE_PASS'),
        'DATABASE_HOST': envs('DATABASE_HOST'),
        'DATABASE_PORT': envs('DATABASE_PORT'),
        'REDIS_HOST': envs("REDIS_HOST")
    }
else:
    env = get_environ_vars()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'krchchat_app',
    'channels',
    'crispy_forms',
    'crispy_bootstrap4'
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

ASGI_APPLICATION = 'KrchChat.asgi.application'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'KrchChat.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [Path(__file__).resolve().parent / 'templates'],
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

# WSGI_APPLICATION = 'KrchChat.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
# import mongoengine
# mongoengine.connect(db=DATABASE_NAME, host=DATABASE_HOST, username=USERNAME, password=PASSWORD)
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env['DATABASE_NAME'],
        'USER': env['DATABASE_USER'],
        'PASSWORD': env['DATABASE_PASS'],
        'HOST': env['DATABASE_HOST'],
        'PORT': env['DATABASE_PORT'],
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_ROOT = 'static'
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CHANNEL_LAYERS = {
        "default": {
            "BACKEND": "channels_redis.core.RedisChannelLayer",
            "CONFIG": {
                "hosts": [(env["REDIS_HOST"], 6379)],
            },
        },
    }
