from django.db import models
from system.models import System
from software.models import SoftwareUpdate

class Certification(models.Model):
    CERT_TYPES = (
        ('certified', 'Certified'),
        ('limited', 'Certified with Limitations'),
        ('tested', 'Field Tested'),
        ('pending', 'Pending'),
        ('nocert', 'Not Certified'),
        )
    type = models.CharField(max_length=20, choices=CERT_TYPES)
    system = models.ForeignKey(System)
    software = models.ForeignKey(SoftwareUpdate)
    notes = models.TextField()
    
    def __unicode__(self):
        return "{} {} {}".format(self.system, self.software, self.type)