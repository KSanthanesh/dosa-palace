"""
Testing the views.py
"""

from django.test import TestCase
from .models import Meals
# from .models import Meals
# from .models import Reserve


class TestViews(TestCase):
    """
    TestViews
    """

    def test_home(self):
        """
    Home page Testing
    """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'meals/home.html')

    def test_get_meal_list_page(self):
        """
        Meals page Testing
        """
        response = self.client.get('/get_meal_list/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'meals/list.html')

    def test_get_meal_detail_page(self):
        """
        Meals page Testing
        """
        # m = Meals.objects.create(name='Atta Dosa')
        response = self.client.get('/get_meal_detail/{1}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'meals/detail.html')

    # def test_reservation_page(self):
    #     """
    #     Reservation page Testing
    #     """
    #     response = self.client.get('/accounts/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, '/accounts/signup.html')
