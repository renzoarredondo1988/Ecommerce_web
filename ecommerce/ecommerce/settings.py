"""
Django settings for ecommerce project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)ytj@61vs@7zif$0^ddy#d&fm#0=$sssnfljz$k3anrwnr+6gc'

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
    'GestionUsuarios',
    'Productos',
    'Carrito',
    'InterfazGeneral',
    'PagosyPedidos',
    'pagos',
    

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates',], #le indicamos que busque en los templates del proyecto y las apps
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'Carrito.context_processors.auth_and_cart_info',
                
            ],
        },
    },
]

WSGI_APPLICATION = 'ecommerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/


STATIC_URL = '/static/' #la primer barra hace referencia a una URL absoluta (fuera de todo), para archivos estaticos
#le estás diciendo a Django que esta es la ruta base desde el dominio raíz.
MEDIA_URL = '/media/' #Idem anterior, pero aqui hace ref. a archivos del tipo imagenes, videos, etc

# MEDIA_ROOT = BASE_DIR / 'media'
# STATIC_URL = '/static/'
# STATICFILES_DIRS = [
#     BASE_DIR / 'static',
# ]


"""STATICFILES_DIRS = [ #agregamos las rutas del proyecto y de la aplicacion
    BASE_DIR / 'static',
    BASE_DIR / 'GestionUsuarios/static',
    BASE_DIR / 'InterfazGeneral/static',
    BASE_DIR / 'PagosyPedidos/static',
    BASE_DIR / 'Productos/static',
    BASE_DIR / 'Carrito/static',
]"""



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MEDIA_URL = '/media/'  # URL a través de la cual se accederán los archivos de medios
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Ruta física donde se almacenarán los archivos

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#INTEGRACION DE MERCADOPAGO
MERCADO_PAGO_ACCESS_TOKEN = 'APP_USR-5285721843882809-101119-da1cfb4649ba02083771e8f3bf6a83ad-238786920'
MERCADO_PAGO_PUBLIC_KEY = 'APP_USR-3a6866da-6e61-4cc3-9215-4b3e6d9fec70'


# settings.py
#SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Almacenará la sesión en la base de datos
SESSION_COOKIE_NAME = 'sessionid'  # Nombre del cookie que usará para almacenar la sesión
SESSION_COOKIE_AGE = 1800  # La sesión durará una hora