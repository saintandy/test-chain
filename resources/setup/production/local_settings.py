DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1+1a3v&74_f^!z18)v$tnksy_c2sh6d367$0d_3log!+8clk%6'

ALLOWED_HOSTS = ['']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'CONN_MAX_AGE': 600,
    },
}