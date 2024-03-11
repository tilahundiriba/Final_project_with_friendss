"""
Django settings for HMS_project project.

Generated by 'django-admin startproject' using Django 5.0.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR ,'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
MEDIA_DIR = os.path.join(BASE_DIR ,'media')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-p9r%ow-iook*^x(p=8=d(@n0*858!i5jjqx3&)82*@kanjq9m('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # Use SMTP as the email backend
# EMAIL_HOST = 'smtp.gmail.com'  # Specify your email host
# EMAIL_PORT = 587  # Specify the port for your email host
# EMAIL_USE_TLS = True  # Enable TLS encryption for the connection
# EMAIL_HOST_USER = 'getayemuluken9@gmail.com'  # Specify the email address to use for sending email
# EMAIL_HOST_PASSWORD = 'jdqs ezos ffnq jxkc'  # Specify the email password

# # Default email address settings
# DEFAULT_FROM_EMAIL = 'your_email@example.com'  # Specify the default "from" address for outgoing e
# SERVER_EMAIL = 'your_email@example.com'  # Specify the email address used as the "from" address fo

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
       'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'admin_app',
    'nurse_app',
    'doctor_app',
    'casher_app',
    'receptionist_app',
   'laboratory_app'
    #    'channels',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
]
CRISPY_TEMPLATE_PACK = 'bootstrap4'
ROOT_URLCONF = 'HMS_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR,],
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
ASGI_APPLICATION = 'HMS_project.asgi.application'


# 👇 5. Add the below line for channel layer
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': "channels.layers.InMemoryChannelLayer"
    }
}

WSGI_APPLICATION = 'HMS_project.wsgi.application'



# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE':'django.db.backends.postgresql',
#         'NAME':'malu',
#         'USER':'postgres',
#         'PASSWORD':'1234',
#         'HOST':'localhost',
#         'PORT':'5050',
#     }
# }
# 
# DATABASES = {
#     'default': {
#         'ENGINE':'django.db.backends.postgresql',
#         'NAME':'malu',
#         'USER':'postgres',
#         'PASSWORD':'1234',
#         'HOST':'localhost',
#         'PORT':'5050',
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE':'django.db.backends.postgresql',
#         'NAME':'mg',
#         'USER':'postgres',
#         'PASSWORD':'362588',
#          'HOST':'localhost',
#          'PORT':'5432',
#    }}
# DATABASES = {
#     'default': {
#         'ENGINE':'django.db.backends.postgresql',
#         'NAME':'newBD',
#         'USER':'tilish',
#         'PASSWORD':'14241224',

#         'HOST':'localhost',
#         'PORT':'5432',
#     }
# }
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.sqlite3',
       'NAME': BASE_DIR / 'db.sqlite3',  # Adjust the path to your SQLite database file
   }
}
# 
# DATABASES = {
#     'default': {
#         'ENGINE':'django.db.backends.postgresql',
#         'NAME':'nf',
#         'USER':'postgres',
#         'PASSWORD':'362588',
#         'HOST':'localhost',
#         'PORT':'5432',
#     }
# }
# 

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/


STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR /'static/'
]
# MEDIA_ROOT = MEDIA_DIR
# MEDIA_URL = 'media/'

MEDIA_URL = '/media/'
MEDIA_ROOT = MEDIA_DIR
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER ='fikefiresew1234@gmail.com'
EMAIL_HOST_PASSWORD ='minyvxbzjtyxxwnu'
