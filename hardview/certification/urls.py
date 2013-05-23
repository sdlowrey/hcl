from django.conf.urls.defaults import patterns
from certification.models import Certification
from certification.views import CertificationList

cert_info = {
    'queryset': Certification.objects.all(),
}

urlpatterns = patterns('certification.views',
    (r'^$', CertificationList.as_view()),
)
