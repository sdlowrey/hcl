from django.db import models

class SoftwareProduct(models.Model):
    name = models.CharField(max_length=80)
    version = models.CharField(max_length=10)
    
    def __unicode__(self):
        return "{} {}".format(self.name, self.version)
    
class SoftwareUpdate(models.Model):
    product = models.ForeignKey(SoftwareProduct)
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return "{} {}-{}".format(self.product.name, self.product.version, self.name)