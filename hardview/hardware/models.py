from django.db import models
from annotation.models import Annotation

class Vendor(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class Hardware(models.Model):
    vendor = models.ForeignKey(Vendor)
    product = models.CharField(max_length=50)
    released = models.DateField()
    ended = models.DateField()
    note = models.ManyToManyField(Annotation)
    
    def __unicode__(self):
        return "{} {}".format(self.vendor.name, self.product)

class PciDevice(Hardware):
    PRIMARY_FUNCTIONS = (    
        ('video',   'Video Controller'),
        ('network', 'Network Interface'),
        ('audio',   'Audio Controller'),
        ('storage', 'Storage Controller'),
        ('usb',     'USB Host Controller'),
        )
    removable = models.BooleanField()
    primaryFunction = models.CharField(max_length=10, choices=PRIMARY_FUNCTIONS)
    pciVendor = models.CharField(max_length=4)
    pciDevice = models.CharField(max_length=4)
    pciSubvendor = models.CharField(max_length=4, blank=True)
    pciSubdevice = models.CharField(max_length=4, blank=True)

class Computer(Hardware):
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
    formFactor = models.CharField(max_length=50, choices=FORM_FACTORS)
    integratedPciDevice = models.ManyToManyField(PciDevice)

class Peripheral(Hardware):
    PRIMARY_FUNCTIONS = (
        ('storage', 'Storage'),
        ('smartcard', 'Smart Card Reader'),
        ('printer', 'Printer'),
        ('webcam', 'Video Camera'),
        ('touch', 'Touch Screen'),
        ('pedal', 'Foot Pedal')
    )
    primaryFunction = models.CharField(max_length=10, choices=PRIMARY_FUNCTIONS)

class SystemConfiguration(models.Model):
    """A combination of a computer and zero or more removable devices that
    make up a tested system."""
    computer = models.ForeignKey(Computer)
    pciDevice = models.ManyToManyField(PciDevice)
    note = models.ManyToManyField(Annotation)

    