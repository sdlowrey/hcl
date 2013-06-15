from django.conf.urls.defaults import *
from hardware.views import ComputerList

urlpatterns = patterns('',
    (r'^$', ComputerList.as_view())
)
