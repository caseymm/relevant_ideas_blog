from django.conf.urls import patterns, url

from blogApp import views

urlpatterns = patterns('',
    url(r'^$', views.all_posts, name='blogApp_home'),
    url(r'^(?P<pk>\d+)$', views.post, name='blogApp_post'),
    )