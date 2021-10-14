"""
Testcase for forms.py
"""
from django.test import TestCase
from .forms import ReserveForm

# Create your tests here.


class TestReserveForm(TestCase):

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

    # def test_fields_are_explicit_in_form_metaclass(self):
    #     form = ReserveForm()
    #     self.assertEqual(form.Meta.fields, ['vistor_name', 'user_name'])
