from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class PServices(models.Model):
    """Professional Services model"""
    name = models.CharField(max_length=75, blank=False)
    description = models.TextField(max_length=500, blank=False)
    upvotes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    author = models.ForeignKey(User)
    created_date = models.DateTimeField(auto_now_add=True)
    

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
    ProfService = models.ForeignKey(PServices)
    author = models.ForeignKey(User)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
