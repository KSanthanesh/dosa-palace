from django.test import TestCase
# from .models import Meals
# from .models import Reserve


class TestViews(TestCase):

    def test_home(self):
        response = self.client.get('meals/home')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'meals/home.html')
