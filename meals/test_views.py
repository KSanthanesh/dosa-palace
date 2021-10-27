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

    def test_get_meal_detail_page(self):
        """
        Meals detail page Testing
        """
        meal = Meals.objects.create(
            name='Atta Dosa', slug='atta-dosa', description='This is attadosa',
            price='4.00', preparation_time='10', image='atta_dosa.jpg')
        response = self.client.get(f'/get_meal_detail/{meal.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'meals/detail.html')

    def test_reservation_page(self):
        """
        Reservation page Testing
        """
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/signup.html')

    def test_contact_page(self):
        """
        Contact Us page Testing
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

    # def test_can_add_reserve(self):
    #     """
    #     User enter their details in the add reserve form, it will redirect
    #     to Reservation view page
    #     """
    #     response = self.client.post('/add_reserve/', {'visitor_name': 'Priya', 'user_name': 'dosapalace', 'phone_number': '67890', 'no_of_people': '5', 'date': '2021-10-20', 'time': '20:00:00'})  # noqa: E501
    #     self.assertRedirects(response, '/meals/view_reserve/')

    def test_view_reserve_page(self):
        """
        Reservation view for dining page testing
        """
        response = self.client.get('/view_reserve/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'meals/view_reserve.html')

    # def test_edit_reserve_page(self):
    #     """
    #     Edit reservation page open testing
    #     """
    #     meal = Booking.objects.create(
    #         visitor_name='Priya', user_name='dosapalace', phone_number='12345',
    #         no_of_people='2', date='2021-10-20', time='20:00:00')
    #     response = self.client.get(f'/edit/{meal.id}')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'meals/edit_reserve.html')

    # def test_can_edit_reserve_page(self):
    #     """
    #     Edit reservation page can edit the user details for dining testing
    #     """
    #     meal = Booking.objects.create(
    #         visitor_name='Priya', user_name='dosapalace', phone_number='12345',
    #         no_of_people='2', date='2021-10-20', time='20:00:00')
    #     response = self.client.post(f'/edit/{meal.id}', {'visitor_name': 'Devi', 'user_name': 'dosapalace', 'phone_number': '12345', 'no_of_people': '2', 'date': '2021-10-20', 'time': '20:00:00'})  # noqa: E501
    #     updated_meal = Booking.objects.get(id=meal.id)
    #     print(updated_meal.visitor_name)
    #     self.assertEqual(updated_meal.visitor_name, 'Devi')
    #     self.assertRedirects(response, '/meals/view_reserve/')

    # def test_can_delete_reservation(self):
    #     """
    #     Delete option can delete the user details for dining
    #     """
    #     meal = Booking.objects.create(
    #         visitor_name='Priya', user_name='dosapalace', phone_number='12345',
    #         no_of_people='2', date='2021-10-20', time='20:00:00')
    #     response = self.client.get(f'/delete/{meal.id}')
    #     self.assertRedirects(response, '/meals/view_reserve/')
    #     existing_meals = Booking.objects.filter(id=meal.id)
    #     self.assertEqual(len(existing_meals), 0)
