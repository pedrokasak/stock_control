import os
from pathlib import Path
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-hcjikj=ua*%hq+_8@46$yi8k^2=+k3u2x3g^j!ye)oodfu6u1r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'RENDER' not in os.environ
# DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'store.apps.StoreConfig',
    'pages.apps.PagesConfig',
    'customers.apps.CustomersConfig',
    'suppliers.apps.SuppliersConfig',
    'products.apps.ProductsConfig',
    'rest_framework',
    'drf_spectacular',
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

ROOT_URLCONF = 'core.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# BD MySQL
# DATABASES = {
#     'default': {
#       #'ENGINE': 'django.db.backends.postgresql',
# 'NAME': config('NAME'),
# 'USER': config('USER'),
# 'PASSWORD': config('PASSWORD'),
# 'HOST': 'db',   # Or an IP Address that your DB is hosted on
# 'PORT': '5432',
#     }
# }

# default_db_url = 'sqlite:///' + str(BASE_DIR / 'db.sqlite3')
#
# parse_database = partial(dj_database_url.parse, conn_max_age=600)

# 'default': config('DATABASE_URL', default=default_db_url, cast=parse_database)
# DATABASES = {
#     'default': config('DATABASE_URL', default=default_db_url, cast=parse_database)
# }

# DATABASE = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'BASE': BASE_DIR / 'db.sqlite3'
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'stock_manager',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'PORT': '5432'
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


FIXTURE_DIRS = (os.path.join(BASE_DIR, 'core', 'fixtures'),)
STATIC_URL = '/static/'


if not DEBUG:    # Tell Django to copy statics to the `staticfiles` directory
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
else:
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'templates', 'static')]
    # PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    # STATIC_ROOT = os.path.join(PROJECT_ROOT, 'templates', 'staticfiles')


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'templates', 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    # YOUR SETTINGS
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Stock Control API',
    'DESCRIPTION': 'Your project description',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS
}