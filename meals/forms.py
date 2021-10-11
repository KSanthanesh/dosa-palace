from django import forms
from .models import Booking


class ReserveForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = '__all__'
