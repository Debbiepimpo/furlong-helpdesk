from django.db import models


class PServices(models.Model):
    """Professional Services model"""
    name = models.CharField(max_length=75, blank=False)
    description = models.TextField(max_length=500, blank=False)
    purchases = models.IntegerField(default=0)
    udPrice =  models.DecimalField(max_digits=8, decimal_places=2)
    totalHours = models.IntegerField(blank=False)

    STATUS_CHOICES = (
        ('Available', 'Available'),
        ('Current Unavailable', 'Current Unavailable')
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Available'
    )

    def __str__(self):
        return self.name


class PServices_Bought(models.Model):
    """Professional Services Bought model"""
    name = models.CharField(max_length=75, blank=False)
    description = models.TextField(max_length=500, blank=False)
    ProfService = models.ForeignKey(PServices)
    totalHours = models.IntegerField(blank=False)

    def __str__(self):
        return self.name
