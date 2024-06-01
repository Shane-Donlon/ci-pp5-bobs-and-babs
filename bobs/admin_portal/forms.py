from django import forms
from django.core.validators import RegexValidator
from django.forms import ModelForm
from products.models import Product


class AddProductForm(ModelForm):
    allergin_info = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder':
            "contains: nuts, dairy, gluten, may contain: peanuts",}),
        validators=[
            RegexValidator(
                regex='contains:|may contain:',
                message='Must contain "contains:" or "may contain:"',
                code='invalid_allergin_info'
            )
        ]
    )

    class Meta:
        model = Product
        fields = "__all__"

# Path: bobs/admin_portal/views.py
