from django.contrib import admin
from system.models import System, Vendor, PciDevice

admin.site.register(Vendor)
admin.site.register(System)
admin.site.register(PciDevice)