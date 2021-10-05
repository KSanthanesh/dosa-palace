from django.shortcuts import render
from .models import Meals


def home(request):
    return render(request, 'meals/home.html')


def get_meal_list(request):
    meal_list = Meals.objects.all()

    context = {
        'meal_list': meal_list,
    }

    return render(request, 'meals/list.html', context)


def get_meal_detail(request, m_id):
    meal_detail = Meals.objects.get(id=m_id)

    context = {
        'meal_detail': meal_detail,
    }
    
    return render(request, 'meals/detail.html', context)


def contact(request):
    return render(request, 'meals/contact.html')


