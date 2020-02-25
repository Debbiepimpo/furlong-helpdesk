from django import forms
from .models import Hour

class HourForm(forms.ModelForm):
    class Meta:
        model = Hour
        fields = ('requested_hours', 'requested_date', 'order', 'comments', 'name')