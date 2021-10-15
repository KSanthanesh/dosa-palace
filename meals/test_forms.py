"""
Testcase for forms.py
"""
from django.test import TestCase
from .forms import ReserveForm

# Create your tests here.


class TestReserveForm(TestCase):
    """
    For Reservation Form
    """

    def test_visitor_name_is_required(self):
        """
        Visitor name is required
        """
        form = ReserveForm({'visitor_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('visitor_name', form.errors.keys())
        self.assertEqual(
            form.errors['visitor_name'][0], 'This field is required.')

    def test_user_name_is_required(self):
        """
        User name is required
        """
        form = ReserveForm({'user_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('user_name', form.errors.keys())
        self.assertEqual(
            form.errors['user_name'][0], 'This field is required.')

    def test_phone_number_is_required(self):
        """
        Phone Number is required
        """
        form = ReserveForm({'phone_number': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors.keys())
        self.assertEqual(
            form.errors['phone_number'][0], 'This field is required.')

    def test_no_of_people_is_required(self):
        """
        Number of People Field is required
        """
        form = ReserveForm({'no_of_people': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('no_of_people', form.errors.keys())
        self.assertEqual(
            form.errors['no_of_people'][0], 'This field is required.')

    def test_date_is_required(self):
        """
        Date Field is required
        """
        form = ReserveForm({'date': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('date', form.errors.keys())
        self.assertEqual(
            form.errors['date'][0], 'This field is required.')

    def test_time_is_required(self):
        """
        Time Field is required
        """
        form = ReserveForm({'time': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('time', form.errors.keys())
        self.assertEqual(
            form.errors['time'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        For meta fields
        """
        form = ReserveForm()
        self.assertEqual(form.Meta.fields, '__all__')
