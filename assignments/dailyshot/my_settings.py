DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'assignments',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': 3306,
        'OPTIONS': {'charset': 'utf8mb4'}
    }
}
SECRET_KEY = 'django-insecure-tq@@+j=#ogi_ul8iy-79anbup4n9r(6v__ncsxf3e(p0@@44aa'

ALGORITHM = "HS256"