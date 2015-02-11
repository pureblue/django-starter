from starter.settings.base import *

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
INTERNAL_IPS = ('127.0.0.1', )
DEBUG = True
TEMPLATE_DEBUG = DEBUG
MEDIA_ROOT = os.path.join(BASE_DIR, os.pardir, 'uploads')
MEDIA_URL = '/uploads/'
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, os.pardir, 'static'),)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)