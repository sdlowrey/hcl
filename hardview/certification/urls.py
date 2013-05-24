from django.conf.urls.defaults import patterns
from certification.views import CertificationList

urlpatterns = patterns('',
    (r'^$', CertificationList.as_view()),
)
