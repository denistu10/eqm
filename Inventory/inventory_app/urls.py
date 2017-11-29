from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'index/$', views.index),
    url(r'login/$', views.get_login,name='login'),
    url(r'inventory/$',views.inventory_views, name='management'),
    url('csv/$', views.render_csv),
    url(r'logout/$', views.logout_views, name='logout'),
]
