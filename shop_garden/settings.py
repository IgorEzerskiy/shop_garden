"""
Django setting`s for shop_garden project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import platform
from pathlib import Path
import os
from shop_main_app.telegram_bot import InfoBot
import environ
import mimetypes

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!

INTERNAL_IPS = ['127.0.0.1']

# DEBUG = env("DEBUG")
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "0.0.0.0"]

if env("ALLOWED_HOSTS") is not None:
    try:
        ALLOWED_HOSTS += env("ALLOWED_HOSTS").split(",")
    except Exception as ex:
        print("Cant set ALLOWED_HOSTS, using default instead" + '/n' + f'{ex}')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop_main_app',
    'options_app',
    'cart_app',
    'orders',
    'phonenumber_field',
    'tinymce',
    'debug_toolbar',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'shop_garden.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'shop_main_app.context_processors.category_list',
                'options_app.context_processors.footer_info',
                'cart_app.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'shop_garden.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

if DEBUG is True:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': env('DB_NAME'),
            'USER': env('DB_USER'),
            'PASSWORD': env('DB_PASSWORD'),
            'HOST': env('DB_HOST'),
            'PORT': env('DB_PORT'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': env('POSTGRES_NAME'),
            'USER': env('POSTGRES_USER'),
            'PASSWORD': env('POSTGRES_PASSWORD'),
            'HOST': env('POSTGRES_HOST'),
            'PORT': env('POSTGRES_PORT'),
        }
    }

AUTHENTICATION_BACKENDS = ['shop_main_app.backends.EmailBackend']

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'uk'
LANGUAGES = [
    ('uk', 'Українська'),
    ('en', 'English'),
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

CART_SESSION_ID = 'cart'

# Static files (CSS, JavaScript, Images) for dev and prod environment
# https://docs.djangoproject.com/en/4.2/howto/static-files/

if DEBUG is True:
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [os.path.join(BASE_DIR, "shop_garden/static")]
else:
    STATIC_URL = "/static_prod/"
    STATIC_ROOT = BASE_DIR / "storage/static_prod"
    STATICFILES_DIRS = [os.path.join(BASE_DIR, "shop_garden/static")]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Media files for dev and prod environment
if DEBUG is True:
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'shop_garden/media')
else:
    MEDIA_URL = '/media_prod/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'storage/media_prod')

AUTH_USER_MODEL = 'shop_main_app.User'

# Telegram bot

TELEGRAM_BOT_API_TOKEN = env('TELEGRAM_API_TOKEN')
CHANEL_ID = env('TELEGRAM_CHANEL_ID')

# async single tone telegram bot

INFO_BOT = InfoBot(api_token=TELEGRAM_BOT_API_TOKEN,
                   chanel_id=CHANEL_ID)

# Celery/Redis

CELERY_BROKER_URL = env("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = env("CELERY_RESULT_BACKEND")

# WKHTMLTOPDF_PATH (https://wkhtmltopdf.org/downloads.html)

if platform.system() == 'Windows':
    WKHTMLTOPDF_PATH = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
else:
    WKHTMLTOPDF_PATH = rf"{env('WKHTMLTOPDF_PATH')}"

# Debug toolbar conf
mimetypes.add_type("application/javascript", ".js", True)

DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False,
}

# email notification credentials

SMTP_SERVER = env('SMTP_SERVER')
SMTP_PORT = env('SMTP_PORT')
SMTP_EMAIL_USERNAME = env('SMTP_EMAIL_USERNAME')
SMTP_EMAIL_PASSWORD = env('SMTP_EMAIL_PASSWORD')
