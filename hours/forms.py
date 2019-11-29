from django import forms
from .models import Hour, HourComment


class CreateHourForm(forms.ModelForm):
    """Form to create hours"""
    class Meta:
        model = Hour
        fields = ('name', 'description')


class HourCommentForm(forms.ModelForm):
    """Form to create hour comments"""
    class Meta:
        model = HourComment
        fields = ('comment',)
