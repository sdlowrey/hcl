from django.contrib import admin
from software.models import SoftwareProduct, SoftwareUpdate

admin.site.register(SoftwareProduct)
admin.site.register(SoftwareUpdate)
