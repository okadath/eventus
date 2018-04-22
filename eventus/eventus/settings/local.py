from .base import *
from unipath import Path
# Database 
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':'eventusdb',
        'USER':'eventususer',
        'PASSWORD':'Qwerty',
        'HOST':'localhost',
        'PORT':'5432',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL='/media/'
from unipath import Path
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
MEDIA_ROOT =Path(__file__).ancestor(3).child('media')
#MEDIA_ROOT=BASE_DIR.child('media')


