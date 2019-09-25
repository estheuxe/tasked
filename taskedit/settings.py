import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'v9t97ttqhcl8a53b-9%)gpyuwcs06rwpv94u$ibsa9m7%kqb3v'

''' tokens & keys & pws '''

APP_ID = '11630581252b45c8b3d7459720ed2af1'
APP_PW = 'c200a37d97064c03ab55b1a1a5a28402'
TRELLO_KEY = '27138010bc3a442737533781e5029962'
TRELLO_TOKEN = '0ab806b21beb8db46ff186fb60c364843b541b100249ba7d36cc41f35472ca93'

''' URLs '''

URL = 'https://oauth.yandex.ru/authorize?response_type=token&client_id=' + APP_ID

URL_FOR_CARD = 'https://api.trello.com/1/cards/{id}'
URL_CARDS = 'https://api.trello.com/1/lists/{id}/cards'
URL_LISTS = 'https://api.trello.com/1/boards/{id}/lists'
URL_BOARDS = 'https://api.trello.com/1/members/me/boards'
POST_TRELLO_URL = 'https://api.trello.com/1/cards'

YT_URL_CARDS = 'https://estheuxework.myjetbrains.com/youtrack/api/issues'
YT_URL_CARD_EDIT = 'https://estheuxework.myjetbrains.com/youtrack/api/issues/{id}'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework'
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

ROOT_URLCONF = 'taskedit.urls'

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

WSGI_APPLICATION = 'taskedit.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'