from django import forms
from django.forms import ModelForm
from products.models import ShippingInformation

from .counties import COUNTIES

COUNTY_CHOICES = [(county, county) for county in COUNTIES]


class ShippingInformationFrom(ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'autocomplete':
                                                        'given-name',
                                                               'placeholder':
                                                                   'John'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'autocomplete':
                                                              'family-name',
                                                              'placeholder':
                                                              'Doe'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'autocomplete':
                                                            'email',
                                                            'placeholder':
                                                            'john.doe@example'
                                                            '.com'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'autocomplete':
                                                            'street-address',
                                                            'placeholder':
                                                                'Address'}))
    town = forms.CharField(widget=forms.TextInput(attrs={'autocomplete':
                                                         'address-level2',
                                                         'placeholder':
                                                             'Town'}))
    county = forms.ChoiceField(choices=COUNTY_CHOICES,
                               widget=forms.Select(attrs={
                                            'autocomplete': 'address-level1',
                               }))
    eircode = forms.CharField(max_length=8,
                              widget=forms.TextInput(attrs={'autocomplete':
                                                            'postal-code',
                                                     'pattern':
                                                            '[A-Za-z0-9]{3}\s*'
                                                            '[A-Za-z0-9]{4}',
                                                            'placeholder':
                                                            'A65 F4E2'}))
    phone = forms.CharField(
             max_length=12,
             widget=forms.TextInput(attrs={
                'autocomplete': 'tel',
                'pattern': '[353]{3}[0-9]{9}', 'placeholder': '353881234567',
                'type': 'tel'
                })
    )

    class Meta:
        model = ShippingInformation
        fields = ['first_name', 'last_name', 'email', 'address', 'town',
                  'county', 'eircode', 'phone']
        attrs = {'autocomplete': 'shipping', 'class': 'form-control'}
        exclude = ['order', "customer"]
