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

    # def double_booking(self):
    #     double_booking = super(ReserveForm, self).clean()
    #     visitor_name = double_booking.get('visitor_name')
    #     date = double_booking.get('date')
    #     try:
    #         Booking.objects.get(visitor_name=visitor_name, date=date)
    #     except Booking.DoesNotExist:
    #         return double_booking
    #     else:
    #         raise ValidationError('Already Bookedthe Same Name in Same Date, Please enter another Name')
