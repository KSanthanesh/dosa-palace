from django.db import models
# from allauth.account.utils import user_display
# from django.conf import settings
from django.contrib.auth.models import User
# from django_currentuser.middleware import (get_current_user, get_current_authenticated_user)
# from django_currentuser.db.models import CurrentUserField

# register = template.Library()


# @register.simple_tag(name="user_display")
# def user_display_tag(user):

#     return user_display(user)

# Create your models here.


class Meals(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    preparation_time = models.IntegerField()
    image = models.ImageField(upload_to='media/', default=True)

    class Meta:
        verbose_name = 'meal'
        verbose_name_plural = 'meals'

    def __str__(self):
        return self.name


class Reserve(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, default="")
    # name = models.ForeignKey(User, on_delete=models.CASCADE)
    # name = CurrentUserField()
    phone_number = models.IntegerField()
    no_of_people = models.IntegerField()
    no_of_tables = models.IntegerField()
    date = models.DateField(null=True)
    time = models.TimeField(null=True)

    def __str__(self):
        return self.name
