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


INSTALLED_APPS = [ <br/>
    'django.contrib.admin', <br/>
    'django.contrib.auth',<br/>
    'django.contrib.contenttypes',<br/>
    'django.contrib.sessions',<br/>
    'django.contrib.messages',<br/>
    'django.contrib.staticfiles',<br/>
    'rest_framework',<br/>
    'rest_framework.authtoken',<br/>
    'iman',<br/>
    ...<br/>
    ...<br/>
]<br/>

##Migrations

run ./manage.py makemigrations && ./manage.py migrate