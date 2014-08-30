"""
Django settings for beeport project.

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
SECRET_KEY = '6i2fs)q($oj-fgugtv@5qtv1@!+cwz!v(m1g*s&8wop(q68-(5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, 'template/'),
)


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'management',
    'django_oneall',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'beeport.urls'

WSGI_APPLICATION = 'beeport.wsgi.application'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'django_oneall.auth.OneAllAuthBackend',
)


ONEALL_SITE_NAME = 'beeport'
ONEALL_PRIVATE_KEY = 'ef4f252b-4af8-4263-8590-da2ec2ab628d'
ONEALL_PUBLIC_KEY = 'c0ace20c-ea0c-433d-ac83-34fe362abb23'


# This setting lets you decide which identity data you want stored in the User model.
# The keys stand for the fields in the User model, while the values are the expressions that will be evaluated
# as attributes of the identity object as received from OneAll. There can be more than one identity expression,
# in case different authentication providers have different data structures.
# Note that the usernames will default to the user_token, which is a UUID. You can override it with any other
# unique identity information
ONEALL_CACHE_FIELDS = {
    'username': ('user_token',),
    'email': ('emails[0].value',),
    'first_name': ('name.givenName',),
    'last_name': ('name.familyName',),
}

# User identity is always cached on first authentication. However, if you want to spare an API call for users
# who are already known to your Django app, you can disable the refresh of cache for the second time they
# connect and onward.
ONEALL_REFRESH_CACHE_ON_AUTH = True

# The OneAll cache table in the DB, where cached identities are stored
ONEALL_CACHE_TABLE = 'oneall_cache'

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

LANGUAGE_CODE = 'tr-TR'
TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_URL = '/template/static/'

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(
        os.path.dirname(__file__),
        'template/static',
    ),
)

MEDIA_ROOT = '/Users/mertsaygi/Desktop/Beeport/beeport/uploads'
MEDIA_URL = 'http://127.0.0.1:8000/uploads/'

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"