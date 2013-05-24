from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from certification.models import Certification
from system.models import System, Vendor

class SystemList(ListView):
    model = System
    
    def get_queryset(self):
        self.vendor = get_object_or_404(Vendor, name=self.args[0])
        return System.objects.filter(vendor=self.vendor)