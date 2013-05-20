# urls needed: add, <vendor>, <vendor>/<model
from django.conf.urls import patterns, include, url
from systems.views import list_all

urlpatterns = patterns('',
    url(r'^$', list_all),
)