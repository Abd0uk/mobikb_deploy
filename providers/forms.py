from django import forms
from .models import Operator, Network, CountryData, CountryField

class OperatorForm(forms.ModelForm):
    class Meta:
        model = Operator
        fields = '__all__'
        