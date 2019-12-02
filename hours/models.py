from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Hour(models.Model):
    """Hour model"""
    name = models.CharField(max_length=75, blank=False)
    description = models.TextField(max_length=500, blank=False)
    purchases = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    author = models.ForeignKey(
        User,
        related_name='created_by',
        on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    comment_number = models.IntegerField(default=0)

    STATUS_CHOICES = (
        ('Available', 'Available'),
        ('In progress', 'In progress'),
        ('Current Unavailable', 'Current Unavailable'),
        ('Cancelled', 'Cancelled')
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
    author = models.ForeignKey(User)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment


class HourUpvote(models.Model):
    """ Model to purchase a hour """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hour = models.ForeignKey(Hour, on_delete=models.CASCADE)

    def __str__(self):
        return self.hour.title
