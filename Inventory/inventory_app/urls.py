from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'index/$', views.index),
    url(r'login/$', views.get_login,name='login'),
]
