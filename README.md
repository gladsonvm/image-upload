# image-upload
An api to C/R/U/D images using Django Rest Framework
##Install using pip
pip install git+git://github.com/gladsonvm/image-upload.git
##urls.py
Add
urlpatterns += url(r'^iman/', include('iman.urls', namespace='iman')),
 to your urls.py

##Installed Apps
Add
'iman' to installed apps in settings.py


INSTALLED_APPS = [ \
    'django.contrib.admin',\
    'django.contrib.auth',\
    'django.contrib.contenttypes',\
    'django.contrib.sessions',\
    'django.contrib.messages',\
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'iman',
    ...
    ...
]

##Migrations

run ./manage.py makemigrations && ./manage.py migrate