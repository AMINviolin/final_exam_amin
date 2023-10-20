from config.settings import *
import os


SECRET_KEY = '(8v857f95uzd(hhd5ll)2bo@9bga%std2daa7a!s!2e$y76jb%'
DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


STATIC_ROOT = os.path.join(BASE_DIR, '/static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
STATICFILES_DIRS = [
    BASE_DIR/'static/',
    BASE_DIR/'media',
]


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
