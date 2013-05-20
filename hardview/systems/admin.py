from django.contrib import admin
from systems.models import Computer, Vendor, PciDevice

admin.site.register(Vendor)
admin.site.register(Computer)
admin.site.register(PciDevice)