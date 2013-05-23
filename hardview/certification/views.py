from django.http import HttpResponse
from django.views.generic import ListView
from certification.models import Certification

def cert_matrix(request, **kwargs):
    out='<h1>debug</h1> queryset: {}'.format(kwargs['queryset'])
    #for thing in request:
    #    out += '<br>' + thing
    return HttpResponse(out)

class CertificationList(ListView):
    model = Certification