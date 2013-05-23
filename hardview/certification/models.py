from django.db import models
from system.models import System
from software.models import SoftwareUpdate

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
    system = models.ForeignKey(System)
    software = models.ForeignKey(SoftwareUpdate)
    
    def __unicode__(self):
        return "{} {} {}".format(self.system, self.software, self.state)
    
class Note(models.Model):
    """Annotations for certificates that may affect applicability.
    """
    certification = models.ManyToManyField(Certification)
    note = models.TextField()
