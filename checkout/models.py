from django.db import models
from ProfessionalServices.models import PServices
from django.contrib.auth.models import User

# Create your models here.
            
class Order(models.Model):
    """customer info model for orders"""
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=True)
    county = models.CharField(max_length=40, blank=False)
    date = models.DateField()
    remainingHours = models.IntegerField(blank=False)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    ProfService = models.ForeignKey(PServices, null=False, on_delete=models.CASCADE)
    
    
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive')
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Available'
    )

    def __str__(self):
        return "Package Id: {0}, Package: {1}, Purchase Date: {2}".format(self.id, self.ProfService, self.date)


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
    ProfService = models.ForeignKey(PServices, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(
            self.quantity, self.ProfService.name, self.ProfService.udPrice)

