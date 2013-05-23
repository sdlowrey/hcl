from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name
    
class Hardware(models.Model):
    vendor = models.ForeignKey(Vendor)
    product = models.CharField(max_length=50)
    endOfLife = models.BooleanField()

    def __unicode__(self):
        return "{} {}".format(self.vendor.name, self.product)

class System(Hardware):
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
    processor = models.CharField(max_length=50)
    formFactor = models.CharField(max_length=50, choices=FORM_FACTORS)
    expandable = models.BooleanField()


class PciDevice(Hardware):
    SIMPLE_TYPES = (    
        ('video', 'Video Controller'),
        ('network', 'Network Interface'),
        ('audio', 'Audio Controller'),
        ('storage', 'Storage/RAID Controller'),
        ('usb', 'USB Host Controller'),
        )
    system = models.ManyToManyField(System)
    removable = models.BooleanField()
    
    pciVendor = models.CharField(max_length=4)
    pciDevice = models.CharField(max_length=4)
    pciSubvendor = models.CharField(max_length=4, blank=True)
    pciSubdevice = models.CharField(max_length=4, blank=True)
    