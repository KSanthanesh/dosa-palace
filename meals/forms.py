"""
    Reservation Form
"""

from django import forms
from .models import Booking


class ReserveForm(forms.ModelForm):
    """
    ReserveForm for Add and Edit Reservation
    """

    class Meta:
        """
        Class Meta
        """
        model = Booking
        fields = '__all__'
