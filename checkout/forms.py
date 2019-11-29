from django import forms
from .models import Order


class MakePaymentForm(forms.Form):
    """Form to take users payment information"""

    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2019, 2050)]

    credit_card_number = forms.CharField(
        label='Credit card number',
        required=False,
        min_length=16,
        max_length=16,
        widget=forms.TextInput(attrs={
            'pattern':
            '[0-9]{4} *[0-9]{4} *[0-9]{4} *[0-9]{4}',
            'placeholder':
            '4242 4242 4242 4242',
            'required': True}))
    cvv = forms.CharField(
        label='Security code (CVV)',
        min_length=3, max_length=3, required=False,
        widget=forms.TextInput(attrs={'required': 'True'}))
    expiry_month = forms.ChoiceField(
        label='Month',
        choices=MONTH_CHOICES,
        required=False)
    expiry_year = forms.ChoiceField(
        label='Year',
        choices=YEAR_CHOICES,
        required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):
    """Form to take users personal info prior to payment"""

    class Meta:
        model = Order
        fields = (
            'full_name', 'phone_number', 'country', 'postcode',
            'town_or_city', 'street_address1', 'street_address2',
            'county'
        )
