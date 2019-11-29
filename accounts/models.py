from django.db import models


# Create your models here.
class Order(models.Model):
    """Customer order model"""
    name = models.CharField(max_length=50, blank=False)
    email = models.CharField(max_length=20, blank=False)
    subject = models.CharField(max_length=40, blank=False)
    comment = models.CharField(max_length=150, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)
