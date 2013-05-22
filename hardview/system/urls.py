from django.conf.urls.defaults import *
from django.views.generic import list_detail
from system.models import System

system_info = {
    'queryset': System.objects.all(),
}

urlpatterns = patterns('',
    (r'^$', list_detail.object_list, system_info)
)
