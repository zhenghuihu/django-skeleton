'''
local development settings
'''
# include all base settings
from .base import *                 # pylint: disable=W0401,W0614
# include credentials (not included in repo)
from . import credentials as crd    # pylint: disable=W0401,W0611

DEBUG = True

ALLOWED_HOSTS = []

# ========================
# SECRET_KEY 
# https://docs.djangoproject.com/en/1.10/ref/settings/#std:setting-SECRET_KEY
# ========================
SECRET_KEY = crd.SECRET_KEY

# ========================
# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
# ========================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'run', 'db.sqlite3'),
    }
}

# ========================
# logging configuration
# https://docs.djangoproject.com/en/1.10/topics/logging/
# ========================
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)-7s %(asctime)s %(module)-10s %(lineno)-3d %(message)s',
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
    },
    'handlers': {
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'django': {
            'handlers': ['console',],
            'propagate': False,
            'level': 'DEBUG',
        },
    },
}
