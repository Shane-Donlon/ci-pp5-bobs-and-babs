from django import forms
from products.models import Order


class AdminOrderUpdateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
