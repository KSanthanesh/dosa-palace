from django.shortcuts import render
from .models import Meals


def home(request):
    return render(request, 'meals/home.html')
