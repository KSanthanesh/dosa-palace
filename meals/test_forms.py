from django.test import TestCase
from .forms import ReserveForm

# Create your tests here.


class TestReserveForm(TestCase):

    def reserve_form_all_fields_required(self):
        form = ReserveForm({'all': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('all', form.errors.keys())
        self.assertEqual(form.errors['all'][0], 'This field is required.')
