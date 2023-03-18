from settings_configs import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-e*x_+p(9^&i!y$mq=ik%hi0@+7xks4gbf26*l+)#4k_k3n0)#^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

AUTH_USER_MODEL = 'contents.User'

ROOT_URLCONF = 'DjSignals.urls'

WSGI_APPLICATION = 'DjSignals.wsgi.application'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
