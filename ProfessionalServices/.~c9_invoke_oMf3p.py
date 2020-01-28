from django import forms

class RequestForm(forms.Form):
    """Form to allow users to request an hour of profesiionsl service support"""
    name = forms.CharField(required=True, max_length=75)
    email = forms.EmailField(required=True, max_length=75)
    widgets = {date = forms.DateInput(input_format=('%d %B, %Y'), attrs={'class': 'datepicker'}, required=True)},
    message = forms.CharField(widget=forms.Textarea, required=True, max_length=500)