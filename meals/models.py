from django.db import models

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
    # username = models.CharField(max_length=50)
    name = models.CharField(max_length=50, unique=True)
    phone_number = models.IntegerField()
    no_of_people = models.IntegerField()
    no_of_tables = models.IntegerField()

    def __str__(self):
        return self.phone_number
