from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Hour(models.Model):
    """Hour model"""
    name = models.CharField(max_length=75, blank=False)
    description = models.TextField(max_length=500, blank=False)
    purchases = models.IntegerField(default=0)
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


class HourComment(models.Model):
    """Hour comment model"""
    comment = models.TextField(max_length=256, blank=False)
    hour = models.ForeignKey(Hour)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment


class HourUpvote(models.Model):
    """ Model to purchase a hour """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hour = models.ForeignKey(Hour, on_delete=models.CASCADE)

    def __str__(self):
        return self.hour.title
