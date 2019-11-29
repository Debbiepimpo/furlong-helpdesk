from django import forms
from .models import PServices, PServices_Bought


class CreatePServicesForm(forms.ModelForm):
    """Form to create ProfessionalService requests"""
    class Meta:
        model = PServices
        fields = ('name', 'description')


class PServicesCommentForm(forms.ModelForm):
    """Form to create ProfessionalService comments"""
    class Meta:
        model = PServices_Bought
        fields = ('comment',)
