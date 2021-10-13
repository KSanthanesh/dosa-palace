"""
    meals app views.py
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Meals, Booking, MasterTable
from .forms import ReserveForm, MasterTableForm


def home(request):
    """
        for home page
    """
    return render(request, 'meals/home.html')


def get_meal_list(request):
    """
    for Meals page
    """
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


def contact_reply(request):
    return render(request, 'meals/contact_reply.html')


def add_reserve(request):
    table_count = MasterTable.objects.all()
    if request.method == "POST":
        form = ReserveForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Booked the Table")
            return redirect('view_reserve')
    form = ReserveForm()

    context = {
            'form': form,
            'table_count': table_count,
        }

    return render(request, 'meals/add_reserve.html', context)


def get_total_tables(request):
    table_count = MasterTable.objects.all()

    context = {
        'table_count': table_count,
    }

    return render(request, 'meals/table_count.html', context)


def view_reserve(request):
    reserves = Booking.objects.all()
    context = {
        'reserves': reserves
        }
    print("reserves", reserves)
    return render(request, 'meals/view_reserve.html', context)


def user_list(request):
    ul = Booking.objects.all()
    context = {
        'ul': ul
        }
    return render(request, 'meals/user_list.html', context)


def edit_reserve(request, meal_id):
    reservation = get_object_or_404(Booking, id=meal_id)

    if request.method == "POST":
        form = ReserveForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('view_reserve')

    form = ReserveForm(instance=reservation)
    context = {
            'form': form
        }

    return render(request, 'meals/edit_reserve.html', context)


def delete_reserve(request, meal_id):
    reservation = Booking.objects.get(id=meal_id)
    reservation.delete()
    return redirect("view_reserve")


def handler404(request, exception):
    return render(request, 'meals/404.html', status=404)