from django.views.generic import ListView
from certification.models import Certification

class CertificationList(ListView):
    model = Certification
    
    
    