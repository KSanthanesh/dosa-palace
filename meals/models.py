"""
    Models datebase
"""
from django.db import models


class Meals(models.Model):
    """
    Meals details for User
    """
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    preparation_time = models.IntegerField()
    image = models.ImageField(upload_to='media/', default=True)

    class Meta:
        """
        Class Meta
        """
        verbose_name = 'meal'
        verbose_name_plural = 'meals'

    def __str__(self):
        return self.name


class Booking(models.Model):
    """
    User can Reserve a table for dining
    """
    visitor_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    no_of_people = models.IntegerField()
    date = models.DateField(null=True)
    time = models.TimeField(null=True)

    def __str__(self):
        return self.visitor_name
