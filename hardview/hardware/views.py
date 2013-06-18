from django.views.generic import ListView
from hardware.models import Computer, PciDevice

class ComputerList(ListView):
    model = Computer
    
class PciDeviceList(ListView):
    model = PciDevice

            