from .base import *


#dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
#load_dotenv(dotenv_path)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'En_dev_no_importa'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

SETTINGS_ENV = 'development'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'userlectaen',
        'USER':  os.getenv('DB_USER_DEV'),
        'PASSWORD':  os.getenv('DB_PASSWORD_DEV'),  
        'HOST':  os.getenv('DB_HOST_DEV'),
        'PORT':  os.getenv('DB_PORT_DEV'),
    },
    
    'lectaen': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'lectaen',
        'USER':  os.getenv('DB_USER_DEV'),
        'PASSWORD':  os.getenv('DB_PASSWORD_DEV'),  
        'HOST':  os.getenv('DB_HOST_DEV'),
        'PORT':  os.getenv('DB_PORT_DEV'),
    } ,
    'nwp_2': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nwp_lentes',
        'USER':  os.getenv('DB_USER_DEV'),
        'PASSWORD':  os.getenv('DB_PASSWORD_DEV'),  
        'HOST':  os.getenv('DB_HOST_DEV'),
        'PORT':  os.getenv('DB_PORT_DEV'),
    },
    'nwp_match': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nwp_match',
        'USER':  os.getenv('DB_USER_PROD'),
        'PASSWORD':  os.getenv('DB_PASSWORD_PROD'),
        'HOST':  os.getenv('DB_HOST_PROD'),
        'PORT':  os.getenv('DB_PORT_PROD'),
    },
    'nwp_csfs': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nwp_csfs',
        'USER':  os.getenv('DB_USER_PROD'),
        'PASSWORD':  os.getenv('DB_PASSWORD_PROD'),
        'HOST':  os.getenv('DB_HOST_PROD'),
        'PORT':  os.getenv('DB_PORT_PROD'),
    }

}

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, '..', 'static')
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')