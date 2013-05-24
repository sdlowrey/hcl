from django.views.generic import ListView
from certification.models import Certification
from system.models import System

class SystemList(ListView):
    model = System
            