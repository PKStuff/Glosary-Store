from django import forms
from .models import Store, Purchase


class Store_form(forms.ModelForm):

    class Meta:

        model = Store
        fields = ['quantity']



