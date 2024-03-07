from .base import * # noqa
from .base import env

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("EMAIL_HOST", default="django-insecure-l8$i=*+66-9*g24bb-#2!7-sk&u&q_z0z*ecf&9u&ae$p_bwfl")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DJANGO_DEBUG", True)

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]

DOMAIN = env("DOMAIN")
SITE_NAME = "EGO Motors"