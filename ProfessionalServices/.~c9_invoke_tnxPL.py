from django import forms
from django.utils.timezone import datetime
from django.core.exceptions import ValidationError
from checkout.models import Order
from ProfessionalServices.models import PServices
from datetime import date

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'
    
class RequestForm(forms.Form):
    """Form to allow users to request an hour of profesional service support"""
    name = forms.CharField(required=True, max_length=75)
    email = forms.EmailField(required=True, max_length=75)
    subject = forms.CharField(required=True, max_length=75)
    date_required = forms.DateField(widget=DateInput)
    start_time  = forms.TimeField(widget=TimeInput)
    finish_time  = forms.TimeField(widget=TimeInput)
    
    orders = Order.objects.filter(user_id=request.user.id).order_by('-id').exclude(status='Inactive')
    ProfessionalServices = []
    for order in orders:
        ProfessionalServices.append(get_object_or_404(PServices, pk=order.ProfService_id))
    PACKAGE_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive')
    )
    package = forms.ChoiceField(choices=PACKAGE_CHOICES, widget=forms.Select(),
                              required=True)
        
    def clean(self):
        end = self.cleaned_data.get("finish_time")
        start = self.cleaned_data.get("start_time")
        date = self.cleaned_data.get("date_required")
        if end <= start:
            raise ValidationError('Ending times must after starting times')
        if date <= datetime.now().date():
            raise ValidationError('requested date must after today')

    def __init__(self, user, *args, **kwargs):
        super(waypointForm, self).__init__(*args, **kwargs)
        self.fields['waypoints'] = forms.ChoiceField(
            choices=[(service.id, str(service)) for service in Waypoint.objects.filter(user=user)]
        )