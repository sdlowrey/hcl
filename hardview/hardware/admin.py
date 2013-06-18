from django.contrib import admin
from hardware.models import Vendor, Computer, PciDevice, Peripheral, SystemConfiguration

admin.site.register(Vendor)
admin.site.register(Computer)
admin.site.register(PciDevice)
admin.site.register(Peripheral)
admin.site.register(SystemConfiguration)