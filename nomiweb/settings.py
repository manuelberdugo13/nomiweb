"""
Django settings for nomiweb project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from django.urls import reverse_lazy

from .db_credentials import DB_PASSWORD


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-svftih64!=7dd*aj*3)bf$&@l%b^j2uc5qhnn7y7v2%7#7lhau'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    
    # Generated applications
    'apps.login', 
    'apps.employees',     # Employees application
    'apps.companies',     # Companies application
    'apps.administrator',
    # 'apps.payroll',       # Payroll application
    # 'apps.api_database',  # API database applicatio#n
    # Django REST Framework
    'rest_framework',
    # Crispy Forms
    'crispy_forms',
    "crispy_bootstrap5",
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize', #Para poner puntos en numeros para separar miles
    'import_export',
    
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    
    
    ## debug 
    'debug_toolbar',
]

INTERNAL_IPS = [
    '127.0.0.1',
]


CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'

CRISPY_TEMPLATE_PACK = 'bootstrap5'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'apps.login.middlewares.DatabaseRouterMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]



ROOT_URLCONF = 'nomiweb.urls'




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


WSGI_APPLICATION = 'nomiweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


DATABASE_ROUTERS = [
    'nomiweb.db_routers.routers.DatabaseRouter'
]

AUTHENTICATION_BACKENDS = [
    'apps.components.custom_auth_backend.CustomAuthBackend',
    'django.contrib.auth.backends.ModelBackend',  # Esto es opcional, pero es una buena práctica
]

SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # O el backend que estés usando
SESSION_COOKIE_AGE = 1209600  # Duración de la sesión en segundos (2 semanas)
SESSION_SAVE_EVERY_REQUEST = True  # Guardar la sesión en cada solicitud
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # No expirar la sesión al cerrar el navegador


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'userlectaen',
        'USER': 'devdjango',
        'PASSWORD': DB_PASSWORD,  
        'HOST': 'devatiempo.cqfpcv4ejul5.us-east-1.rds.amazonaws.com',
        'PORT': '5432',
    },
    
    'lectaen': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'lectaen',
        'USER': 'devdjango',
        'PASSWORD': DB_PASSWORD,  
        'HOST': 'devatiempo.cqfpcv4ejul5.us-east-1.rds.amazonaws.com',
        'PORT': '5432',
    } ,
    'nwp_2': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nwp_lentes',
        'USER': 'devdjango',
        'PASSWORD': DB_PASSWORD,  
        'HOST': 'devatiempo.cqfpcv4ejul5.us-east-1.rds.amazonaws.com',
        'PORT': '5432',
    } 
    
}




# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.nomiweb.co'
EMAIL_PORT = 465
EMAIL_USE_TLS = False
EMAIL_HOST_USER = 'no-responder@nomiweb.co'
EMAIL_HOST_PASSWORD = '5zySp3D{iad]'
EMAIL_USE_SSL = True
EMAIL_TIMEOUT = None
EMAIL_SSL_KEYFILE = None
EMAIL_SSL_CERTFILE = None
EMAIL_SSL_CAFILE = None
EMAIL_SSL_CERT_SUBJ = None
EMAIL_SSL_CERT_PASSWD = None
EMAIL_SSL_CIPHER = None
EMAIL_USE_LOCALTIME = False
EMAIL_FILE_PATH = None
EMAIL_FROM = None
EMAIL_SUBJECT_PREFIX = '[Django] '


# EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
# EMAIL_HOST_USER = '0696ea5c99b771'
# EMAIL_HOST_PASSWORD = 'be56bf78c3f67f'
# EMAIL_PORT = '2525'


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#AUTH_USER_MODEL = 'login.CustomUser'