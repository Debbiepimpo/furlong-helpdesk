from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'
    
class RequestForm(forms.Form):
    """Form to allow users to request an hour of profesional service support"""
    name = forms.CharField(required=True, max_length=75)
    email = forms.EmailField(required=True, max_length=75)
    subject = forms.CharField(required=True, max_length=75)
    date_required = forms.DateField(widget=DateInput)