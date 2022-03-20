from django.contrib import admin
from django.urls import path
from django.urls import re_path
from . import views
# from django.conf.urls.defaults import handler404, handler500
# from django.conf.urls import handler404
# from you_dow.views import error
app_name = 'downloader'

urlpatterns = [
    path('', views.home, name='homepage'),

    path('submit', views.submit, name='submit'),
    path('downloading', views.downloading, name='downloading'),
    path('s', views.playlist_download, name='playlist_download'),

]
