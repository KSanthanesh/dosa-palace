"""
Testing the views.py
"""

from django.test import TestCase
# from .models import Meals
from .models import Meals, Booking



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

    # def test_get_meal_detail_page(self):
    #     """
    #     Meals page Testing
    #     """
    #     m = Meals.objects.create(name='Atta Dosa', slug='atta-dosa', description= 'This is atta dosa', price='4.00', preparation_time='10')
    #     response = self.client.get('/get_meal_detail/{m.id}')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'meals/detail.html')

    # def test_can_get_meal_detail_page(self):
    #     """
    #     Meals page Testing
    #     """
    #     # m = Meals.objects.create(name='Atta Dosa')
    #     m = Meals.objects.create(name='Atta Dosa', slug='atta-dosa', description= 'This is atta dosa', price='4.00', preparation_time='10')
    #     response = self.client.get(f'/get_meal_detail/{m.id}')
    #     self.assertTemplateUsed(response, 'meals/detail.html')

    def test_reservation_page(self):
        """
        Reservation page Testing
        """
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/signup.html')

    def test_contact_page(self):
        """
        Reservation page Testing
        """
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'meals/contact.html')

    def test_contact_reply_page(self):
        """
        Thanks message when user uses the contact form page testing
        """
        response = self.client.get('/contact_reply/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'meals/contact_reply.html')

    def test_add_reserve_page(self):
        """
        Add a reservation table for dining page testing
        """
        response = self.client.get('/add_reserve/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'meals/add_reserve.html')

    def test_can_add_reserve(self):
        """
        User enter their details in the add reserve form, it will redirect
        to Reservation view page
        """
        response = self.client.post('/add_reserve/', {
            'visitor_name': 'Priya', 'user_name': 'dosapalace', 'phone_number': '67890',
            'no_of_people': '5', 'date': '2021-10-20', 'time': '20:00:00'})
        self.assertRedirects(response, '/meals/view_reserve/')

    def test_view_reserve_page(self):
        """
        Reservation view for dining page testing
        """
        response = self.client.get('/view_reserve/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'meals/view_reserve.html')

    def test_edit_reserve_page(self):
        """
        Edit reservation for dining page testing
        """
        meal = Booking.objects.create(visitor_name='Priya', user_name='dosapalace', phone_number='12345', no_of_people='2', date='2021-10-20', time='20:00:00')
        response = self.client.get(f'/edit/{meal.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'meals/edit_reserve.html')
