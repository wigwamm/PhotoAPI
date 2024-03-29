"""
Django settings for wigwamm_api project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g7!4r^ae&p62)7z9w+4$)u(t545*9bt9hli59j8(x+b$qntub%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'djcelery',

    'repixl',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'wigwamm_api.urls'

WSGI_APPLICATION = 'wigwamm_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'




# CELERY

BROKER_HOST = 'localhost'
BROKER_PORT = 5672
# BROKER_USER = ''
# BROKER_PASSWORD = ''
# BROKER_VHOST = ''
CELERY_BACKEND = 'amqp'
#CELERY_RESULT_DBURI = ''

import djcelery
djcelery.setup_loader() 


# DROPBOX

DROPBOX_APP_KEY = '5oqgo69g2ayjvzt'
DROPBOX_SECRET  = '3qtihkc4np23vn8'
DROPBOX_TOKEN   = 'b2Twyr030YEAAAAAAAAAAS1JR_CuCQ0QwleQG3Nxqq2Txvri4vOqKrkzcV8YNf5Q'
DROPBOX_USER_ID = '235337783'
DROPBOX_FOLDER  = '/api_test'


