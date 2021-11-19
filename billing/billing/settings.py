"""
Django settings for billing project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-zphpt8@s!#t(^smcw^^v&6r4$@)z=^f++!nclr$^&yz(f-zd1_'
SESSION_COOKIE_NAME = 'billing_sessionid'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rele',
    'billing'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'billing.middleware.OAuthMiddleware',
]

ROOT_URLCONF = 'billing.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'billing.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# OAuth Settings
OAUTH_URL_WHITELISTS = []

OAUTH_CLIENT_NAME = 'myauth'

OAUTH_CLIENT = {
    'client_id': 'wTBeylRkIBdbCYflE9VvVBe5HNTSTiY5ycRUdniC',
    'client_secret': 'iWW9G3st3BGnmrOKu0UKeSWF8gP8uxFuZ10V4mJz4jHkwdeWur9e5bxngTMDOPE3nZon1DzBsj9IdF3smadFN6AmRkYUko4nrcAK6FQaiRfFDpZ1X9bj5DRgI7k79WqJ',
    'access_token_url': 'http://127.0.0.1:8080/o/token/',
    'authorize_url': 'http://127.0.0.1:8080/o/authorize/',
    'redirect_uri': 'http://127.0.0.1:8100/oauth/callback',
    'client_kwargs': {
        'scope': 'openid',
        'token_placement': 'header'
    },
    'userinfo_endpoint': 'http://127.0.0.1:8080/o/userinfo/',
}

CONN_MAX_AGE = 0
RELE = {
    'APP_NAME': 'djbilling',
    'SUB_PREFIX': 'djbilling',
    'GC_CREDENTIALS_PATH': 'goglia-dev-9a931575a10e.json',
    'MIDDLEWARE': [
        'rele.contrib.LoggingMiddleware',
        'rele.contrib.DjangoDBMiddleware',
    ],
}
