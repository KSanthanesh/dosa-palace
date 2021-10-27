"""
Testing the models.py
"""

from django.test import TestCase
from .models import Meals, Booking
from django.contrib.auth.models import User


class TestModels(TestCase):
    """
    Test views for Meals class
    """

    def test_meals_method_returns(self):
        """
        Check the meals method returns in Meals class in models.
        """
        meal = Meals.objects.create(
            name='Rava Dosa', slug='rava-dosa', description='This is ravadosa',
            price=4.00, preparation_time=10, image='egg-dosa.jpg')
        self.assertEqual(str(meal.name), 'Rava Dosa')
        self.assertEqual(str(meal.slug), 'rava-dosa')
        self.assertEqual(str(meal.description), 'This is ravadosa')
        self.assertEqual(meal.price, 4.00)
        self.assertEqual(meal.preparation_time, 10)
        self.assertEqual(str(meal.image), 'egg-dosa.jpg')

    def test_meals_str_method_name_returns(self):
        """
        Check the Name field is string in Meals class in models.
        """

        meal = Meals.objects.create(
            name='Rava Dosa', slug='rava-dosa', description='This is ravadosa',
            price=4.00, preparation_time=10, image='egg-dosa.jpg')
        expected_string = str(meal.name)
        self.assertEqual(str(meal), expected_string)

    # def test_booking_method_returns(self):
    #     """
    #     Check the bookings method returns in Booking class in models.
    #     """
    #     booking = Booking.objects.create(
    #         visitor_name='Priya', user_name=id, phone_number=12345,
    #         no_of_people=2, date='2021-10-20', time='20:00:00')
    #     self.assertEqual(str(booking.visitor_name), 'Priya')
    #     self.assertEqual(booking.user_name, id)
    #     self.assertEqual(booking.phone_number, 12345)
    #     self.assertEqual(booking.no_of_people, 2)
    #     self.assertEqual(booking.date, '2021-10-20')
    #     self.assertEqual(booking.time, '20:00:00')
