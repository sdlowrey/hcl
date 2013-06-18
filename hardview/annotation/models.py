from django.db import models

class Annotation(models.Model):
    """Dated notes.  Use 'brief' for display and 'full' for complete information"""
    brief = models.CharField(max_length=40)
    full = models.TextField(blank=True)
    dateAdded = models.DateTimeField()
    lastChanged = models.DateTimeField()
    
    def __unicode__(self):
        return "{}".format(self.brief)