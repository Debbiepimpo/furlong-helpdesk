from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from checkout.models import Order


class Hour(models.Model):
    """Hour model"""
    name = models.TextField(max_length=500, blank=False)
    comments = models.TextField(max_length=500, blank=True)
    requested_hours = models.IntegerField(blank=False)
    requested_date = models.DateTimeField("YYYY-MM-DD HH:MM")
    order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, blank=True)
    

    STATUS_CHOICES = (
        ('Approved', 'Approved'),
        ('Pending', 'Pending'),
        ('Rejected', 'Rejected')
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    def __str__(self):
        return self.name