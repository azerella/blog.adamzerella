import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.getenv('BAZ_SECRET_KEY', "abc123")

DEBUG = os.getenv('BAZ_DEBUG', True)

# Security settings
ALLOWED_HOSTS = os.getenv('BAZ_ALLOWED_HOSTS', [])
X_FRAME_OPTIONS = 'SAMEORIGIN'
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_PROXY_SSL_HEADER = None
SECURE_SSL_REDIRECT = False
SECURE_SSL_HOST = None
SECURE_BROWSER_XSS_FILTER = False
SECURE_CONTENT_TYPE_NOSNIFF = False
SECURE_HSTS_SECONDS = 0
SECURE_HSTS_PRELOAD = False
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
#---------------

# Email settings
EMAIL_HOST = None
EMAIL_PORT = 587
EMAIL_HOST_USER = None
EMAIL_HOST_PASSWORD = None
EMAIL_USE_TLS = True
EMAIL_TIMEOUT = 60
EMAIL_SSL_KEYFILE = None
EMAIL_SSL_CERTFILE = None
#---------------

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'app.apps.AppConfig'
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

ROOT_URLCONF = 'blogadamzerella.urls'

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
                'app.context_processors.signup_form'
            ]
        },
    },
]

WSGI_APPLICATION = 'blogadamzerella.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blogadamzerella',
        'HOST': '127.0.0.1',
        'PORT': os.getenv('BAZ_SQL_PORT', '3306'),
        'USER': os.getenv('BAZ_SQL_USER', 'root'),
        'PASSWORD': os.getenv('BAZ_SQL_PASS', 'root'),
        'TIME_ZONE': 'Australia/Sydney',
        'TEST': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'test_blogadamzerella'
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/2.0/topics/i18n/
LANGUAGE_CODE = 'en-au'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "static/")

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
