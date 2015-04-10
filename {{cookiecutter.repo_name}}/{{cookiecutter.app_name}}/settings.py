"""
Django settings for {{ cookiecutter.app_name }} project.
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import excavator
import dj_database_url
import django_cache_url


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = excavator.env_string('DJANGO_SECRET_KEY', required=True)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = excavator.env_bool('DJANGO_DEBUG', default=False)

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = excavator.env_list('DJANGO_ALLOWED_HOSTS', '')


# Application definition

INSTALLED_APPS = (
    'rest_framework',
    '{{ cookiecutter.app_name }}',
)

MIDDLEWARE_CLASSES = []

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ]
        # Fill me in
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

ROOT_URLCONF = '{{ cookiecutter.app_name }}.urls'

WSGI_APPLICATION = '{{ cookiecutter.app_name }}.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASE_URL = excavator.env_string('DATABASE_URL', required=True)
DATABASES = {
    'default': dj_database_url.parse(DATABASE_URL),
}
DATABASES['default'].setdefault('ATOMIC_REQUESTS', True)

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

CACHES = {'default': django_cache_url.config()}
