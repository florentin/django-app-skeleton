from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

from django.contrib import auth
from django.contrib.auth import authenticate, login

from django.views.generic.simple import direct_to_template
from django.shortcuts import redirect

from . import views

urlpatterns = patterns('',
    url(r'^view/(?P<pk>\d+)/$', views.view, kwargs={}, name="f"),
)