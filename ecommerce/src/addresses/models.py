from django.db import models
from billing.models import BillingProfile
# Create your models here.

ADDRESS_TYPES = (
    ('billing', 'Billing'),
    ('shipping', 'Shipping')
)

class Address(models.Model):
    billing_profile = models.ForeignKey(BillingProfile)
    address_type    = models.CharField(max_length=120,choices=ADDRESS_TYPES)
    address_line_1  = models.CharField(max_length=120)
    address_line_2  = models.CharField(max_length=120,null=True,blank=True)
    city            = models.CharField(max_length=120)
    country         = models.CharField(max_length=120,default="India")
    state           = models.CharField(max_length=120)
    postal_code     = models.CharField(max_length=120)

    def __str__(self):
        return str(self.billing_profile)

    def get_address(self):
        return "{line1}\n{line2}\n{line3}\n{line4}, \n{line5}\n{line6}".format(
            line1 = self.address_line_1,
            line2 = self.address_line_2 or "",
            line3 = self.city,
            line4 = self.state,
            line5 = self.postal_code,
            line6 = self.country
        )