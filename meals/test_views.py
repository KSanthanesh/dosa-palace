"""
Testing the views.py
"""

from django.test import TestCase
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
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'meals/home.html')

    def test_get_meal_list_page(self):
        """
        Meals page Testing
        """
        response = self.client.get('get_meal_list/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'meals/list.html')

    def test_get_meal_detail_page(self):
        """
        Meals page Testing
        """
        response = self.client.get('get_meal_detail/<int:m_id>')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'meals/detail.html')
