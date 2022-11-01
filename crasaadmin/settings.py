from pathlib import Path
from django.contrib.messages import constants


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-z4l28e97#5(_38#(o-bb$65dy9ptjy5t+bwnb=9qc9+#d42kj0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'usuario',
    'unidade',
    'crispy_forms',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'crasaadmin.urls'

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

WSGI_APPLICATION = 'crasaadmin.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
        
        #'default': {
        #'ENGINE': 'django.db.backends.mysql',
        #'NAME': 'crasa',
		#'USER' : 'root',
		#'PASSWORD' : '',
		#'HOST' : '127.0.0.1',
		#'PORT' : '3306',
        
        #}
    

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

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True




STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "static_cdn"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

#LOGIN_REDIRECT_URL = 'usuario:login'
LOGIN_URL = "login/"


MESSAGES_TAGS = {
    constants.DEBUG: 'alert-info',
    constants.ERROR: 'alert-danger',
    constants.INFO: 'alert-info',
    constants.SUCCESS: 'alert-success',
    constants.WARNING: 'alert-warning',

}

SESSION_COOKIE_AGE = 3600

SESSION_SAVE_EVERY_REQUEST = True


#EMAIL_HOST = "SMTPCORP.PRODAM"
#EMAIL_PORT = "25"
#EMAIL_HOST_USER = "admin"
#EMAIL_HOST_PASSWORD = ""

EMAIL_HOST = "smtp.email.sa-saopaulo-1.oci.oraclecloud.com"
EMAIL_PORT = "587"
EMAIL_HOST_USER = "ocid1.user.oc1..aaaaaaaan43kkrz5frw6cwd555mulm7v6ylztb2xmasnnzpcw7be3nrnj34a@ocid1.tenancy.oc1..aaaaaaaai7a72s5jgxce6rik7qna2nx2j3flclxvvrkg3mojvxmrjz3hmf6q.jo.com"
EMAIL_HOST_PASSWORD = "MkVFPT-w4(3(xuy_2J9r"
EMAIL_USE_TLS = True

PASSWORD_RESET_TIMEOUT = 3600

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_FILE_PATH = BASE_DIR / 'emails'



#SESSION_SERIALIZER = 'django.contrib.sessions.serialiers.PickleSerializer'