from django.db import models
from django.utils import timezone


class PServices(models.Model):
    """Professional Services model"""
    name = models.CharField(max_length=75, blank=False)
    description = models.TextField(max_length=500, blank=False)
    purchases = models.IntegerField(default=0)
    udPrice = models.IntegerField(blank=False)
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
    comment = models.TextField(max_length=256, blank=False)
    ProfService = models.ForeignKey(PServices)
    udPrice = models.IntegerField(blank=False)
    totalHours = models.IntegerField(blank=False)

    def __str__(self):
        return self.comment
