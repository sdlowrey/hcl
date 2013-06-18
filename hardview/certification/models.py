from django.db import models
from hardware.models import SystemConfiguration
from software.models import SoftwareUpdate
from annotation.models import Annotation
     
class Certification(models.Model):
    """Assigns a certification state to a system and a software update.   
    """
    CERT_STATES = (
        ('certified', 'Certified'),
        ('limited', 'Certified with Limitations'),
        ('tested', 'Field Tested'),
        ('pending', 'Pending'),
        ('nocert', 'Not Certified'),
        )
    state = models.CharField(max_length=20, choices=CERT_STATES)
    system = models.ForeignKey(SystemConfiguration)
    software = models.ForeignKey(SoftwareUpdate)
    note = models.ManyToManyField(Annotation, blank=True)
    date = models.DateField()
    
    def __unicode__(self):
        return "{} {} {}".format(self.system, self.software, self.state)
