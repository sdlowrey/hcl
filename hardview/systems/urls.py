from django.conf.urls.defaults import *
from django.views.generic import list_detail
from systems.models import Computer

computer_info = {
    'queryset': Computer.objects.all(),
}

urlpatterns = patterns('',
    (r'^$', list_detail.object_list, computer_info)
)
