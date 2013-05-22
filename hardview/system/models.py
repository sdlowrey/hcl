from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name
    
class System(models.Model):
    """Describes a product, but not a specific instance of that product.  
    Therefore, there are no instance-specific fields like  memory quantity,
    serial number, or SKU.
    """
    FORM_FACTORS = (
        ('sff', 'Small Form Factor PC'),
        ('desktop', 'Desktop PC'),
        ('minitower', 'Mini-Tower PC'),
        ('thinclient', 'Thin Client'),
        ('rack1u', '1U Rack Server'),
        ('rack2u', '2U Rack Server'),
        ('rack4u', '4U Rack Server'),
        ('other', 'Other Form Factor'),
        )
    vendor = models.ForeignKey(Vendor)
    name = models.CharField(max_length=50)

    processor = models.CharField(max_length=50)
    formfactor = models.CharField(max_length=50, choices=FORM_FACTORS)
    nprocessors = models.PositiveIntegerField()
    memCapacity = models.IntegerField(blank=True, null=True)
    nPciSlots = models.IntegerField()

    def __unicode__(self):
        return "{} {}".format(self.vendor.name, self.name)

class PciDevice(models.Model):
    SIMPLE_TYPES = (    
        ('video', 'Video Controller'),
        ('network', 'Network Interface'),
        ('audio', 'Audio Controller'),
        ('storage', 'Storage/RAID Controller'),
        ('usb', 'USB Host Controller'),
        )
    vendor = models.ForeignKey(Vendor)
    name = models.CharField(max_length=50)
    system = models.ManyToManyField(System)
    removable = models.BooleanField()
    pcivendor = models.CharField(max_length=4)
    pcidevice = models.CharField(max_length=4)
    pcisubvendor = models.CharField(max_length=4, blank=True)
    pcisubdevice = models.CharField(max_length=4, blank=True)
    
    def __unicode__(self):
        return "{} {}".format(self.vendor.name, self.name)
    