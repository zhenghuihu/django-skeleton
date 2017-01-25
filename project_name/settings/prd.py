# include all base settings
from base import *

# disable debugging
DEBUG = False

# ========================
# SECRET_KEY 
# https://docs.djangoproject.com/en/1.10/ref/settings/#std:setting-SECRET_KEY
# ========================
# SECRET_KEY is read from file, not included in repo
SECRET_FILE = os.path.join(PROJECT_ROOT, 'run', 'SECRET.key')
SECRET_KEY = open(SECRET_FILE).read().strip()


# ========================
# STATIC_ROOT
# Collect static files here
# https://docs.djangoproject.com/en/1.10/ref/settings/#std:setting-STATIC_ROOT
# ========================
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'run', 'static')

# ========================
# Database override
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
# ========================
#DATABASES = {
#    'default': {
#    }
#}

# ========================
# logging configuration
# https://docs.djangoproject.com/en/1.10/topics/logging/
# ========================
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)-8s %(asctime)s %(module)-10s %(message)s',
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
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(PROJECT_ROOT, 'run', 'django.log'),
            'maxBytes': 10*1000*1000,  # 10M
            'backupCount': 3,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        '': {
            'handlers': ['file'],
            'propagate': True,
            'level': 'INFO',
        },
        'django': {
            'handlers': ['file',],
            'propagate': True,
            'level': 'INFO',
        },
    },
}
