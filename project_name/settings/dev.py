# include all base settings
from .base import *

DEBUG = True

ALLOWED_HOSTS = []

# ========================
# SECRET_KEY 
# https://docs.djangoproject.com/en/1.10/ref/settings/#std:setting-SECRET_KEY
# ========================
# just a random string 
SECRET_KEY = 'z0y2wi6h0r&7qeaj5%wv35ktm+d-w%h9qzx3oxj96a9vfrn=s_'

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
