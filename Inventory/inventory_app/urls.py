from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'index/$', views.index),
    url(r'login/$', views.get_login,name='login'),
    url(r'management/$',views.management_views, name='management'),
    url(r'logout/$', views.logout_views, name='logout'),
]
