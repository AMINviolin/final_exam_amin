from config.settings import *


SECRET_KEY = '(8v857f95uihigiogijijjjjfssiijfjiooruaslIAJNHVzd(hhd5ll)2bo@9bga%std2daa7a!s!2e$y76jb%'
DEBUG = False
ALLOWED_HOSTS = ['mortalblogs.ir','www.mortalblogs.ir']

# STATIC_ROOT = BASE_DIR/'/static'
# MEDIA_ROOT = BASE_DIR/'media'

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'mydb',
		'USER': 'root',
		'PASSWORD': 'admin',
		'HOST':'localhost',
		'PORT':'3306',
	}
}





EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'mail.mortalblogs.ir'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'mortaled@mortalblogs.ir'
EMAIL_HOST_PASSWORD ='aminem.88.88'
DEFAULT_FROM_EMAIL = 'mortaled@mortalblogs.ir'


CSRF_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = 'Strict'
SESSION_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True
X_FRAME_OPTIONS = 'DENY'
SECURE_HSTS_SECONDS = 15768000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
CSP_DEFAULT_SRC = ("'none'",)
CSP_STYLE_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'",)
CSP_FONT_SRC = ("'self'",)
CSP_IMG_SRC = ("'self'",)