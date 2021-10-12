from django import forms
from .models import Booking, MasterTable


class ReserveForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = '__all__'

class MasterTableForm(forms.ModelForm):

    class Meta:
        model = MasterTable
        fields = '__all__'

