"""
    meals app views.py
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Meals, Booking
from .forms import ReserveForm


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
    """
    for Meal details page.
    """
    meal_detail = Meals.objects.get(id=m_id)

    context = {
        'meal_detail': meal_detail,
    }
    # if meal_detail == "":
    #     return render(request, 'meals/home.html', context)
    # else:
    return render(request, 'meals/detail.html', context)


def contact(request):
    """
    contact us page used for user's enquiry.
    """
    return render(request, 'meals/contact.html')


def contact_reply(request):
    """
    Thanks Message will appear when the user use the contact us form.
    """
    return render(request, 'meals/contact_reply.html')


def add_reserve(request):
    """
    User can reserve a Table for dining.
    """
    if request.method == "POST":
        form = ReserveForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Booked the Table")
            return redirect('view_reserve')
    form = ReserveForm()

    context = {
            'form': form,
        }

    return render(request, 'meals/add_reserve.html', context)


def view_reserve(request):
    """
    User can view the reservation page, once they reserve a table for dining.
    """
    reserves = Booking.objects.all()
    context = {
        'reserves': reserves
    }
    # print("reserves", reserves)
    return render(request, 'meals/view_reserve.html', context)


def edit_reserve(request, meal_id):
    """
    User can update their details like name,phonenumber,persons,date and time
    """
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
    """
    User can delete their reservation for dining.
    """
    reservation = Booking.objects.get(id=meal_id)
    reservation.delete()
    messages.success(request, "You Cancelled the Reservation")
    return redirect("view_reserve")
