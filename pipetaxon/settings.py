import os
import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# False if not in os.environ because of casting above
DEBUG = env('DEBUG')

# Raises Django's ImproperlyConfigured
# exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'rest_framework.authtoken',
    'taxonomy',
    'genomes',
    'rest_framework',
    'django_extensions',
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

ROOT_URLCONF = 'pipetaxon.urls'

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
WSGI_APPLICATION = 'pipetaxon.wsgi.application'

# Parse database connection url strings
# like psql://user:pass@127.0.0.1:8458/db
DATABASES = {
    # read os.environ['DATABASE_URL'] and raises
    # ImproperlyConfigured exception if not found
    #
    # The db() method is an alias for db_url().
    'default': env.db(),

    # read os.environ['SQLITE_URL']
    'extra': env.db_url(
        'SQLITE_URL',
        default='sqlite:////tmp/pipetaxon-sqlite.db'
    )
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
STATIC_ROOT = "static/"

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),

    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100,
    'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.JSONRenderer',
    ),
}

VALID_RANKS = []


# NCBI
# Application specific settings
NCBI_LOCAL_DIR = os.path.join( BASE_DIR, 'data')
DATA_DIR = NCBI_LOCAL_DIR

#new NCBI setup
NCBI_FTP = "https://ftp.ncbi.nlm.nih.gov"
NCBI_ASSEMBLY_SUMMARY = NCBI_FTP + "/genomes/ASSEMBLY_REPORTS/assembly_summary_genbank.txt"

NCBI_ASSEMBLY_BASE = "https://ftp.ncbi.nlm.nih.gov/genomes/all"

NCBI_GENOME_REPORTS_PROKARYOTES = "https://ftp.ncbi.nlm.nih.gov/genomes/GENOME_REPORTS/prokaryotes.txt"
LOCAL_GENOME_REPORTS_PROKARYOTES = os.path.join(DATA_DIR,'GENOME_REPORTS','prokaryotes.txt')

NCBI_ANI_REPORT_PROKARYOTES = "https://ftp.ncbi.nlm.nih.gov/genomes/ASSEMBLY_REPORTS/ANI_report_prokaryotes.txt"
LOCAL_ANI_REPORT_PROKARYOTES = os.path.join(DATA_DIR,'ASSEMBLY_REPORTS','ANI_report_prokaryotes.txt')

NCBI_ASSEMBLY_SUMMARY = "https://ftp.ncbi.nlm.nih.gov/genomes/ASSEMBLY_REPORTS/assembly_summary_genbank.txt"
LOCAL_ASSEMBLY_SUMMARY = os.path.join(DATA_DIR,'ASSEMBLY_REPORTS','assembly_summary_genbank.txt')

NCBI_TAXONOMY_BASE = "rsync://ftp.ncbi.nlm.nih.gov/pub/taxonomy/new_taxdump"
NCBI_NEW_TAXONOMY_DUMP = "new_taxdump.tar.gz"
LOCAL_TAXONOMY_DIR = os.path.join( DATA_DIR, 'taxonomy')

LOG_ROOT=BASE_DIR
LOG_FILE="pipetaxon.log"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)s %(module)s:%(lineno)d %(message)s'
        },
        'standard': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)d ] %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'simple': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'logfile': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_ROOT,LOG_FILE),
            'maxBytes': 1000000,
            'backupCount': 4,
            'formatter': 'standard',
        },
    },
    'loggers': {
        'django': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': True,
        },
        'commands': {
            'level': 'INFO',
            'handlers': ['console'],
            'propagate': True,
        },
        'rq_scheduler': {
            'handlers': ['logfile'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}
