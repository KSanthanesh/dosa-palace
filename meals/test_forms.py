from django.test import TestCase
from .forms import ReserveForm

# Create your tests here.


class TestReserveForm(TestCase):

    def test_reserve_form_all_fields_required(self):
        form = ReserveForm({'vistor_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('vistor_name', form.errors.keys())
        self.assertEqual(form.errors['vistor_name'][0], 'This field is required.')

        form = ReserveForm({'user_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('user_name', form.errors.keys())
        self.assertEqual(form.errors['user_name'][0], 'This field is required.')

    
    # def test_done_field_is_not_required(self):
    #     form = ReserveForm({'vistor_name': 'Test Todo Item'})
    #     self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ReserveForm()
        self.assertEqual(form.Meta.fields, ['vistor_name', 'user_name'])
