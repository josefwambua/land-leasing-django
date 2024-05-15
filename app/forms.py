from django import forms
from .models import Lease

class LeaseForm(forms.ModelForm):
    class Meta:
        model = Lease
        fields = ['land', 'start_date', 'end_date']