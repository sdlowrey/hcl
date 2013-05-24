from django.conf.urls.defaults import *
from system.views import SystemList

urlpatterns = patterns('',
    (r'^$', SystemList.as_view()),
    (r'^vendor/([\w-]+)$', SystemList.as_view())
)
